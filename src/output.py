from abc import ABC, abstractmethod
from model.api import Api
import yaml


class OutputGenerator(ABC):
    def __init__(self, api: Api):
        self.api = api

    @abstractmethod
    def generate(self, output_path: str) -> None:
        pass


class YamlOutputGenerator(OutputGenerator):
    def generate(self, output_path: str) -> None:
        # 将 Api 对象转换为字典，便于序列化
        api_dict = self.api.dict()
        with open(output_path, 'w') as file:
            yaml.dump(api_dict, file, default_flow_style=False)
