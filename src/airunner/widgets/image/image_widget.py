import os

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QVBoxLayout
from PyQt6.QtWidgets import QDialog

from PIL import Image
from airunner.utils import load_metadata_from_image

from airunner.widgets.base_widget import BaseWidget
from airunner.widgets.image.templates.image_widget_ui import Ui_image_widget
from airunner.aihandler.logger import Logger


class ImageWidget(BaseWidget):
    widget_class_ = Ui_image_widget
    image_path = None
    meta_data = {}
    image_width = 0
    image_height = 0

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui.permanently_delete_2.hide()

    def set_image(self, image_path):
        size = self.ui.image_frame.width()
        self.image_path = image_path

        self.load_meta_data(image_path)

        # Create a QPixmap object
        pixmap = QPixmap(self.image_path)
        pixmap = pixmap.scaled(size, size, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)

        # set width and height
        self.image_width = pixmap.width()
        self.image_height = pixmap.height()

        # Create a QLabel object
        label = QLabel(self.ui.image_frame)

        # set width and height of label to size
        label.setFixedWidth(size)
        label.setFixedHeight(size)
        label.mousePressEvent = self.handle_label_clicked
        label.setCursor(Qt.CursorShape.PointingHandCursor)

        # Set the pixmap to the label
        label.setPixmap(pixmap)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    
    def handle_label_clicked(self, event):
        # create a popup window and show the full size image in it
        self.dialog = QDialog()
        self.dialog.setWindowTitle("Image preview")
        layout = QVBoxLayout(self.dialog)
        self.dialog.setLayout(layout)
        pixmap = QPixmap(self.image_path)
        label = QLabel()
        label.setPixmap(pixmap)
        layout.addWidget(label)
        self.dialog.show()
    
    def load_meta_data(self, image_path):
        # load the png metadata from image_path
        with open(image_path, 'rb') as image_file:
            image = Image.open(image_file)
            self.meta_data = load_metadata_from_image(image)

    def send_image_to_grid(self):
        #self.app.ui.canvas_plus_widget.load_image(self.image_path)
        self.app.ui.standard_image_widget.set_pixmap(self.image_path)

    def confirm_delete(self):
        self.ui.permanently_delete_2.show()
    
    def cancel_delete(self):
        self.ui.permanently_delete_2.hide()

    def delete_image(self):
        if not self.image_path:
            return
        try:
            os.remove(self.image_path)
        except Exception as e:
            Logger.error("Failed to delete image")
        try:
            self.deleteLater()
        except Exception as e:
            Logger.error("Failed to delete widget")

    def generate_similar(self):
        image = Image.open(self.image_path)
        meta_data = self.meta_data.copy()
        meta_data.pop("seed", None)
        meta_data.pop("latents_seed", None)
        meta_data["action"] = "txt2img"
        meta_data["width"] = image.width
        meta_data["height"] = image.height
        meta_data["enable_controlnet"] = True
        meta_data["controlnet"] = "canny"
        meta_data["controlnet_conditioning_scale"] = 150
        meta_data["image_guidance_scale"] = 100.0
        meta_data["strength"] = 1.0
        meta_data["enable_input_image"] = True
        meta_data["use_cropped_image"] = False
        self.app.generator_tab_widget.current_generator_widget.call_generate(
            image=image,
            override_data=meta_data
        )
    
    def generate_variant(self):
        image = Image.open(self.image_path)
        meta_data = self.meta_data.copy()
        meta_data.pop("seed", None)
        meta_data.pop("latents_seed", None)
        meta_data["action"] = "txt2img"
        meta_data["width"] = image.width
        meta_data["height"] = image.height
        meta_data["enable_controlnet"] = True
        meta_data["controlnet"] = "canny"
        meta_data["controlnet_conditioning_scale"] = 1000
        meta_data["image_guidance_scale"] = 100.0
        meta_data["strength"] = 1.0
        meta_data["enable_input_image"] = True
        meta_data["use_cropped_image"] = False
        self.app.generator_tab_widget.current_generator_widget.call_generate(
            image=image,
            override_data=meta_data
        )
