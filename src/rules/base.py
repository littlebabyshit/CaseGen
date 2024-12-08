from abc import ABC, abstractmethod

class FieldRule(ABC):
    """规则基类"""

    @abstractmethod
    def get_data(self):
        pass
