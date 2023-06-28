import os
from PIL import Image
from PyQt6 import uic
from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtWidgets import QFileDialog, QSpacerItem, QSizePolicy, QLabel

from airunner.utils import image_to_pixmap
from airunner.windows.base_window import BaseWindow
from functools import partial


class DeterministicGenerationWindow(BaseWindow):
    template_name = "deterministic_generation_window"
    window_title = "Deterministic Generation"
    is_modal = True
    images = []
    data = {}

    def __init__(self, *args, **kwargs):
        self.images = kwargs.get("images", self.images)
        self.data = kwargs.get("data")
        super().__init__(*args, **kwargs)

    def close_event(self, _event):
        self.app.close_deterministic_generation_window()
        # remove self.app.generate_signal.connect(self.handle_generate_signal)
        self.app.generate_signal.disconnect(self.handle_generate_signal)
        self.template.close()

    def initialize_window(self):
        self.app.generate_signal.connect(self.handle_generate_signal)
        self.add_image_widgets_to_canvas()
        self.template.closeEvent = self.close_event
        # self.app.add_image_to_canvas_signal.connect(self.handle_add_image_to_canvas_signal)

    def add_image_widgets_to_canvas(self):
        if not self.images:
            return
        for index, image in enumerate(self.images):
            self.add_image_to_canvas(index, image)

    def add_image_to_canvas(self, index, image):
        widget = uic.loadUi("pyqt/deterministic_widget.ui")
        # insert image into template.thumbnail
        pixmap = image_to_pixmap(image.copy(), 200)
        widget.thumbnail.setPixmap(pixmap)
        widget.new_batch_button.clicked.connect(partial(self.new_batch, index))
        widget.to_canvas_button.clicked.connect(partial(self.to_canvas, index))
        # replace self.template.widget_1 which is a QWidget with widget
        row = 0 if index < 2 else 1
        col = index % 2
        self.template.gridLayout.addWidget(widget, row, col, 1, 1)

    def new_batch(self, index):
        self.app.new_batch(index, self.images[index], data=self.data)
        self.template.close()

    def to_canvas(self, index):
        image = self.images[index]
        image = image.convert("RGBA")
        self.app.canvas.add_image_to_canvas(image, QPoint(0, 0), QPoint(0, 0), use_outpaint=True)

    def handle_generate_signal(self, options):
        options["deterministic_generation"] = True
        #options["interpolation_data"] = self.get_interpolation_data()

    def handle_add_image_to_canvas_signal(self, data):
        data["add_image_to_canvas"] = False
