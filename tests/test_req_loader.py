import json

from req_loader import YApiLoader


yapi_loader = YApiLoader()

def test_load_data_by_url():
    assert False


def test_load_data_by_schema():
    req_shcema = json.load(open("./res/req_schema.json"))
    yapi_loader.load_data(schema = req_shcema)
    res = yapi_loader._load_data_by_schema(req_shcema)
    print(res)


def test__get_body_by_schema():
    assert False


