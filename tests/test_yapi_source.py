import pytest
import yaml

from data_source import YAPISourceAdapter




class TestYapiSource:
    def setup_class(self):
        self.yapi = YAPISourceAdapter()



    def test_adapt(self, yapi_data):
        pass



    def test_convert_to_api(self, yapi_data):
        origin_data = yapi_data[0].get("list")[0]
        yapi_obj = self.yapi.convert_to_api(origin_data)
        assert yapi_obj.api_id == 1072078
        assert yapi_obj.api_name == "httpbinGET接口"
        assert yapi_obj.req.method == "GET"


