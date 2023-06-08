from PIL import ImageDraw
from PyQt6.QtCore import Qt, QPointF, QPoint, QSize, QRect, QThread, QObject, pyqtSignal, QTimer, QRunnable, QThreadPool
from PyQt6.QtGui import QPainter, QPainterPath, QColor, QPen, QImage
from airunner.models.linedata import LineData
from PIL import Image


class RasterizationWorker(QObject):
    finished = pyqtSignal()

    def __init__(self, *args, **kwargs):
        self.convert_pixmap_to_pil_image = kwargs.pop('convert_pixmap_to_pil_image')
        self.img = kwargs.pop('img')
        self.top = kwargs.pop('top')
        self.left = kwargs.pop('left')
        self.bottom = kwargs.pop('bottom')
        self.right = kwargs.pop('right')
        super().__init__(*args)

    def run(self):
        self.convert_pixmap_to_pil_image(self.img, self.top, self.left, self.bottom, self.right)
        self.finished.emit()


class RasterizationTask(QRunnable):
    def __init__(self, worker):
        super().__init__()
        self.worker = worker

    def run(self):
        self.worker.run()


class CanvasBrushesMixin:
    _point = None
    active_canvas_rect = QRect(0, 0, 0, 0)
    color = None
    line_width = None
    left_line_extremity = None
    right_line_extremity = None
    top_line_extremity = None
    bottom_line_extremity = None
    last_left = 0
    last_top = 0
    min_x = 0
    min_y = 0
    last_pos = None
    thread = None
    worker = None
    started = True

    @property
    def is_drawing(self):
        return self.left_mouse_button_down or self.right_mouse_button_down

    @property
    def primary_color(self):
        return QColor(self.settings_manager.settings.primary_color.get())

    def initialize(self):
        self.thread_pool = QThreadPool()
        self.thread_pool.setMaxThreadCount(4)

    def draw(self, layer, index):
        path = QPainterPath()
        painter = None
        for line in layer.lines:
            pen = line.pen
            pen.setCapStyle(Qt.PenCapStyle.RoundCap)
            pen.setJoinStyle(Qt.PenJoinStyle.RoundJoin)
            if self.line_width is None or self.line_width != line.width:
                self.line_width = line.width
                self.draw_path(path, painter)
                painter = None
            if self.color is None or self.color != line.color:
                self.color = line.color
                self.draw_path(path, painter)
                painter = None
            if not painter:
                painter = QPainter(self.canvas_container)
                painter.setBrush(self.brush)
                painter.setRenderHint(QPainter.RenderHint.Antialiasing)
                path = QPainterPath()
            painter.setPen(pen)

            start = QPointF(line.start_point.x() + self.pos_x, line.start_point.y() + self.pos_y)
            end = QPointF(line.end_point.x() + self.pos_x, line.end_point.y() + self.pos_y)

            # also apply the layer offset
            offset = QPointF(self.current_layer.offset.x(), self.current_layer.offset.y())
            start += offset
            end += offset

            # calculate control points for the Bezier curve
            dx = end.x() - start.x()
            dy = end.y() - start.y()
            ctrl1 = QPointF(start.x() + dx / 3, start.y() + dy / 3)
            ctrl2 = QPointF(end.x() - dx / 3, end.y() - dy / 3)

            # add the curve to the path
            path.moveTo(start)
            path.cubicTo(ctrl1, ctrl2, end)

        # draw the entire line with a single drawPath call
        self.draw_path(path, painter)

        # max_lines = 20
        # if (
        #     self.is_drawing and len(self.current_layer.lines) > max_lines
        # ):
        #     self.rasterize_lines()
        # self.rasterize_lines()

    def draw_path(self, path, painter):
        if painter:
            painter.drawPath(path)
            painter.end()

    def handle_erase(self, event):
        self.is_erasing = True
        brush_size = int(self.settings_manager.settings.mask_brush_size.get() / 2)
        image = self.current_layer.images[0].image if len(self.current_layer.images) > 0 else None
        image_pos = self.current_layer.images[0].position if len(self.current_layer.images) > 0 else None
        if image is None:
            return
        start = event.pos() - QPoint(self.pos_x, self.pos_y) - image_pos
        if image:
            image = image.copy()
            draw = ImageDraw.Draw(image)
            if self.last_pos is None:
                self.last_pos = start
            draw.line([
                self.last_pos.x(),
                self.last_pos.y(),
                start.x(),
                start.y()
            ], fill=(0, 0, 0, 0), width=brush_size*2, joint="curve")
            draw.ellipse((
                start.x() - brush_size,
                start.y() - brush_size,
                start.x() + brush_size,
                start.y() + brush_size
            ), fill=(0, 0, 0, 0))
            self.current_layer.images[0].image = image
            self.last_pos = start
            self.update()
        self.update()

    def pen(self, event):
        brush_color = "#ffffff"
        if event.button() == Qt.MouseButton.LeftButton or Qt.MouseButton.LeftButton in event.buttons():
            brush_color = self.settings_manager.settings.primary_color.get()
        brush_color = QColor(brush_color)
        pen = QPen(
            brush_color,
            self.settings_manager.settings.mask_brush_size.get()
        )
        return pen

    def handle_draw(self, event):
        start = event.pos() - QPoint(self.pos_x, self.pos_y)
        pen = self.pen(event)
        if len(self.current_layer.lines) > 0:
            previous = LineData(self.current_layer.lines[-1].start_point, start, pen, self.current_layer_index)
            self.current_layer.lines[-1] = previous

        end = event.pos() - QPoint(self.pos_x + 1, self.pos_y)
        line_data = LineData(start, end, pen, self.current_layer_index)
        self.current_layer.lines.append(line_data)
        self.update()

    def get_line_extremities(self, lines):
        for line in lines:
            start_x = line.start_point.x()
            start_y = line.start_point.y()
            end_x = line.end_point.x()
            end_y = line.end_point.y()

            brush_size = int(self.settings_manager.settings.mask_brush_size.get() / 2)
            min_x = min(start_x, end_x) - brush_size
            min_y = min(start_y, end_y) - brush_size
            max_x = max(start_x, end_x) + brush_size
            max_y = max(start_y, end_y) + brush_size
            self.min_x = min_x
            self.min_y = min_y

            if self.left_line_extremity is None or min_x < self.left_line_extremity:
                self.left_line_extremity = min_x
            if self.right_line_extremity is None or max_x > self.right_line_extremity:
                self.right_line_extremity = max_x
            if self.top_line_extremity is None or min_y < self.top_line_extremity:
                self.top_line_extremity = min_y
            if self.bottom_line_extremity is None or max_y > self.bottom_line_extremity:
                self.bottom_line_extremity = max_y
        return self.top_line_extremity, self.left_line_extremity, self.bottom_line_extremity, self.right_line_extremity

    def rasterize_lines(self, final=False):
        max_lines = len(self.current_layer.lines)#10
        total_lines = len(self.current_layer.lines)
        # if (not self.is_drawing and total_lines < max_lines) or final:
        #     max_lines = len(self.current_layer.lines)
        # if total_lines == 0:
        #     return

        lines = self.current_layer.lines[:max_lines]
        top, left, bottom, right = self.get_line_extremities(lines)

        # create a QImage with the size of the lines
        min_x = min(left, right)
        min_y = min(top, bottom)
        max_x = max(left, right)
        max_y = max(top, bottom)
        width = abs(max_x - min_x)
        height = abs(max_y - min_y)
        img = QImage(QSize(width, height), QImage.Format.Format_ARGB32)
        img.fill(Qt.GlobalColor.transparent)
        painter = QPainter(img)
        painter.setBrush(self.brush)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        path = self.create_image_path(painter, lines)
        painter.drawPath(path)
        painter.end()

        worker = RasterizationWorker(
            convert_pixmap_to_pil_image=self.convert_pixmap_to_pil_image,
            img=img,
            top=top,
            left=left,
            bottom=bottom,
            right=right
        )
        task = RasterizationTask(worker)
        self.thread_pool.start(task)
        # task.setAutoDelete(True)
        task.worker.finished.connect(lambda _max_lines=max_lines, _final=final: self.finalize_pixmap(_max_lines, _final))

    def finalize_pixmap(self, max_lines, final=False):
        self.current_layer.lines = self.current_layer.lines[max_lines:]
        # self.thread.quit()
        # self.thread.wait()
        # if max_lines >= len(self.current_layer.lines):
        #     self.current_layer.lines = []
        # else:
        #     self.current_layer.lines = self.current_layer.lines[max_lines:]
        # self.thread = None
        # if len(self.current_layer.lines) > 0 and final:
        #     self.rasterize_lines(final=True)

    def create_image_path(self, painter, lines):
        path = QPainterPath()
        path.setFillRule(Qt.FillRule.WindingFill)
        for line in lines:
            pen = line.pen
            pen.setColor(line.color)
            pen.setCapStyle(Qt.PenCapStyle.RoundCap)
            pen.setJoinStyle(Qt.PenJoinStyle.RoundJoin)
            painter.setPen(pen)

            start = QPointF(line.start_point.x() - self.left_line_extremity, line.start_point.y() - self.top_line_extremity)
            end = QPointF(line.end_point.x() - self.left_line_extremity, line.end_point.y() - self.top_line_extremity)

            # also apply the layer offset
            offset = QPointF(self.current_layer.offset.x(), self.current_layer.offset.y())
            start += offset
            end += offset

            # calculate control points for the Bezier curve
            dx = end.x() - start.x()
            dy = end.y() - start.y()
            ctrl1 = QPointF(start.x() + dx / 3, start.y() + dy / 3)
            ctrl2 = QPointF(end.x() - dx / 3, end.y() - dy / 3)

            # add the curve to the path
            path.moveTo(start)
            path.cubicTo(ctrl1, ctrl2, end)
        return path

    def convert_pixmap_to_pil_image(self, img: Image, top: int, left: int, bottom: int, right: int):
        img = Image.fromqpixmap(img)
        width = img.width
        height = img.height
        current_image = self.current_layer.images[0].image.copy() if len(self.current_layer.images) > 0 else None
        existing_image_width = current_image.width if current_image else 0
        existing_image_height = current_image.height if current_image else 0

        composite_width = width
        composite_height = height
        if existing_image_width > composite_width:
            composite_width = existing_image_width
        if existing_image_height > composite_height:
            composite_height = existing_image_height

        do_new_image = False
        if composite_width > existing_image_width or composite_height > existing_image_height:
            composite_image = Image.new('RGBA', (composite_width, composite_height), (0, 0, 0, 0))
            do_new_image = True
        else:
            composite_image = current_image
        composite_img_dest = QPoint(left, top)

        pos_x = 0
        pos_y = 0

        if self.last_left != left:
            last_left = self.last_left
            self.last_left = left
            pos_x = -self.last_left + last_left
        if self.last_top != top:
            last_top = self.last_top
            self.last_top = top
            pos_y = -self.last_top + last_top

        new_img_dest_pos_x = 0
        new_img_dest_pos_y = 0

        # self.parent.window.debug_label.setText(
        #     f"W/H: {width}x{height} | imgdest: {new_img_dest_pos_x}, {new_img_dest_pos_y} | ext: {self.left_line_extremity}, {self.top_line_extremity}, {self.right_line_extremity}, {self.bottom_line_extremity} | max: {self.max_left}, {self.max_top} {self.max_right} {self.max_bottom} | last: {self.last_left}, {self.last_top}"
        # )

        # add current image to the composite image
        if current_image and do_new_image:
            existing_img_dest = (pos_x, pos_y)
            existing_img_source = (0, 0)
            composite_image.alpha_composite(current_image, existing_img_dest, existing_img_source)
        new_img_dest = (new_img_dest_pos_x, new_img_dest_pos_y)
        composite_image.alpha_composite(img, new_img_dest)
        self.add_image_to_canvas_new(composite_image, composite_img_dest, self.image_root_point)
