
import pymustache

from model.api import Api


class TemplateUtil:
    @classmethod
    def generate_by_api(self, template_file, api: Api):
        """
        :param template_file:
        :param render_file:
        :param kwargs:
        :return:
        """
        interface_data = api.dict()
        with open(template_file) as f:
            template = f.read()
        mustache_context = pymustache.render(template, interface_data)
        return mustache_context

    @classmethod
    def generate_by_case(self, template_file, testcase, api):
        """
        :param template_file:
        :param render_file:
        :param kwargs:
        :return:
        """
        mustache_context = pymustache.render(template_file, )
        return mustache_context
