from .base import FieldRule

class DemoId(FieldRule):
    def get_data(self):
        return "DemoID Data"
