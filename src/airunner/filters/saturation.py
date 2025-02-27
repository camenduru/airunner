from PIL import ImageEnhance

from airunner.filters.base_filter import BaseFilter


class SaturationFilter(BaseFilter):
    def apply_filter(self, image, do_reset):
        # limit self.factor to 2 decimal places
        self.factor = round(self.factor, 2)
        return ImageEnhance.Color(image).enhance(self.factor)
