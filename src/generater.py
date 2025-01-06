from model.api import Api
from req_loader import YApiLoader
from uils.file_util import FileUtil
from uils.path import project_root
from uils.template_util import TemplateUtil

yapi_loader = YApiLoader()


class Generater:
    def __init__(self, api: Api, interface_template, case_template):
        self.api = api
        self.interface_template = project_root / interface_template
        self.case_template = project_root / case_template

    def run(self):
        # 读取单个 yapi： 文件/链接读取

        # 根据 yapi 生成接口文件： 输入：
        # 1. 根据 yapi 的接口信息，接口模版生成接口信息
        # 输入 api.req， 模版内容。
        # 输出为模版文档。
        # self.data_source
        api_context = TemplateUtil.generate_by_api(self.interface_template, self.api)
        # # 2. 根据 yapi 的路径，设置api的生成路径。
        # # 输入为 api.path ，模版文档内容，
        # # 输出为 生成api文件（包含路径）
        FileUtil.generate_by_path(api_context, f"api{self.api.api_path}.py")
        # # 3. 根据 yapi 的reqschema 生成测试数据： 输入 yapi 的reqscehma ，
        # # 输出： 测试数据，
        case_data = yapi_loader._load_data_by_schema(self.api.req_schema)
        # # 4. 输入：测试用例模版，生成的接口文件路径，
        # # 输出 自动化测试用例内容
        case_context = TemplateUtil.generate_by_case(self.case_template, self.api, case_data)
        # FileUtil.generate_by_path(case_context, f"testcase{self.api.api_path}_test.py")

        return api_context
