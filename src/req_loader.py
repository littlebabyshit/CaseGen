from abc import ABC, abstractmethod
from copy import deepcopy

import requests
import json
import random
import string


# 数据源加载策略接口
class DataSourceLoader(ABC):
    @abstractmethod
    def load_data(self):
        """加载原始数据"""
        pass


# 从 YApi 加载数据
class YApiLoader(DataSourceLoader):
    def load_data(self, endpoint=None, schema=None):
        if endpoint:
            self.raw_data = self._load_data_by_url(endpoint)
        elif schema:
            self.raw_data = self._load_data_by_schema(schema)
        else:
            raise Exception("No data load")

    def _load_data_by_url(self, endpoint):
        print(f"Loading data from YApi: {endpoint}")
        response = requests.get(endpoint)
        if response.status_code == 200:
            return response.json().get("data", {})
        else:
            raise Exception("Failed to load data from YApi.")

    def _load_data_by_schema(self, req_schema):
        """
        根据schema 拼接出来原始响应。
        :param req_schema:
        :return:
        """
        # 获取响应体数据
        body_test_data_list = []
        self.body_raw_data = self.get_body_raw_data(req_schema.get("properties"))
        # 如果有必填字段，则挨个将必填字段删除生成最终数据。
        required = req_schema.get("required")
        if required:
            body_test_data_list.extend(self.list_by_delete_required(required))

        return body_test_data_list

    def get_body_raw_data(self, schema):
        """
        根据字段类型生成数据，递归处理嵌套的对象类型字段
        :param schema: 字段定义的 schema，包含字段名、类型及其他字段信息
        :return: 生成的测试数据
        """

        def generate_by_type(field_type, field_length=None):
            """根据字段类型生成对应的值"""
            if field_type == "string":
                return ''.join(random.choices(string.ascii_letters + string.digits, k=field_length or 10))
            elif field_type == "number":
                return random.randint(10 ** (field_length - 1),
                                      10 ** field_length - 1) if field_length else random.randint(
                    1, 100)
            elif field_type == "boolean":
                return random.choice([True, False])
            elif field_type == "object":
                return {}  # 对象类型会在递归时处理
            else:
                raise ValueError(f"Unsupported field type: {field_type}")

        def recursive_generate(schema):
            """递归生成对象类型字段"""
            data = {}
            for field_name, field_info in schema.items():
                field_type = field_info.get("type")
                field_length = field_info.get("length", None)
                # todo 字段描述，通常是对业务含义的补充。可以使用人工智能去做鉴定。
                description = field_info.get("description", None)
                if field_type == "object":
                    # 递归处理 object 类型
                    properties = field_info.get("properties", {})
                    data[field_name] = recursive_generate(properties)
                else:
                    # todo : 直接生成非对象字段
                    data[field_name] = generate_by_type(field_type, field_length)
            return data

        return recursive_generate(schema)

    # todo ： 未考虑场景，有些字段为具有业务要求的字段。
    def list_by_delete_required(self, required_list):
        """
        列举出来所有删除掉必填字段的情况
        :return:
        """
        test_required_list = []

        for required in required_list:
            new_body_data = deepcopy(self.body_raw_data)
            new_body_data.pop(required)
            test_required_list.append(new_body_data)
        return test_required_list
