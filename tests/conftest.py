import pytest
import yaml


@pytest.fixture
def yapi_data():
    with open("data/yapi.json") as f:
        data = yaml.safe_load(f)
    yield data
