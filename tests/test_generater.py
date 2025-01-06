from data_source import YAPISourceAdapter
from generater import Generater


def test_run(yapi_data):
    origin_data = yapi_data[0].get("list")[0]
    api_obj = YAPISourceAdapter().convert_to_api(origin_data)
    generater = Generater(api_obj, "template/interface.template", "template/pytest.template")
    print(generater.run())

