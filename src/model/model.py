from typing import List


class Source:
    """
    数据源
    """
    url: str

class Api:
    pass


class Case:
    pass


class ApiCase:
    api: Api
    cases: List[Case]
