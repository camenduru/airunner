from airunner.filters.filter_base import FilterBase


class BlurFilter(FilterBase):
    ui_name = ""
    window_title = ""
    default_value = 0.0

    def __init__(self, parent):
        super().__init__(parent)
        self.blur_radius = parent.settings_manager.settings.blur_radius


    def show(self):
        super().show()
        self.blur_radius.set(self.default_value)

        self.parent.current_filter = self.filter

        blur_radius = self.blur_radius.get()

        # set the gaussian_blur_window settings values to the current settings
        self.filter_window.blur_slider.setValue(int(blur_radius))
        self.filter_window.blur_slider.valueChanged.connect(
            lambda val: self.handle_blur_radius_slider_change(val))
        self.filter_window.blur_spinbox.setValue(blur_radius)
        self.filter_window.blur_spinbox.valueChanged.connect(
            lambda val: self.handle_blur_radius_spinbox_change(val))

        # on ok button click, apply the filter
        self.filter_window.buttonBox.rejected.connect(self.cancel_filter)
        self.filter_window.buttonBox.accepted.connect(self.apply_filter)

        self.filter_window.exec()

    def handle_blur_radius_slider_change(self, val):
        self.blur_radius.set(float(val))
        self.filter_window.blur_spinbox.setValue(float(val))
        self.parent.current_filter = self.filter
        self.canvas.update()

    def handle_blur_radius_spinbox_change(self, val):
        self.blur_radius.set(val)
        self.filter_window.blur_slider.setValue(int(val))
        self.parent.current_filter = self.filter
        self.update_canvas()
