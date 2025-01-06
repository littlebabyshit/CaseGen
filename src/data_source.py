# 抽象适配器
from abc import abstractmethod, ABC
from typing import List

from model.api import Api, Req, Res


# yapi -> api 的抽象对象 -> 具体的数据

# YapiSource -> dict -> api 抽象对象


class AbstractSourceAdapter(ABC):
    @abstractmethod
    def adapt(self, raw_data) -> List[Api]:
        pass


class YAPISourceAdapter(AbstractSourceAdapter):
    """
    # YAPI 适配器
    yapi 的数据包含所属项目，接口名称，接口id，接口信息
    """

    def adapt(self, raw_data) -> List[Api]:
        project_name = raw_data.get("name")
        api_list = raw_data.get("list")
        return [self.convert_to_api(api) for api in api_list]

    def convert_to_api(self, api_dict) -> Api:
        req = Req(method=api_dict.get("method"),
                  path=(api_dict.get("path")),
                  headers=(api_dict.get("headers"))
                  )
        res = Res(body=(api_dict.get("res_body")))
        return Api(
            api_id=api_dict.get("_id"),
            api_name=api_dict.get("title"),
            api_path=api_dict.get("path", ""),
            req=req,
            res=res,
        )


# Swagger 适配器
class SwaggerAdapter(AbstractSourceAdapter):
    def adapt(self, raw_data) -> List[Api]:
        name = raw_data["info"]["title"]
        endpoints = raw_data["paths"]
        return []

# 工厂类
class DataSourceFactory:
    @staticmethod
    def get_source(data_source_type: str) -> AbstractSourceAdapter:
        if data_source_type == "yapi":
            return YAPISourceAdapter()
        elif data_source_type == "swagger":
            return SwaggerAdapter()
        else:
            raise ValueError(f"Unknown data source type: {data_source_type}")
