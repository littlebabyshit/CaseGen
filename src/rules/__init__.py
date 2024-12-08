import pkgutil
import importlib
import inspect

from rules.base import FieldRule

# 全局规则注册表
RULES_REGISTRY = {}


def to_camel_case(name: str) -> str:
    """将类名转换为小驼峰格式"""
    return name[0].lower() + name[1:]


def auto_register_rules(package_name: str):
    """自动扫描并注册规则类"""
    # 遍历指定包下的所有模块
    package = importlib.import_module(package_name)
    for _, module_name, _ in pkgutil.walk_packages(package.__path__, package_name + "."):
        module = importlib.import_module(module_name)

        # 遍历模块中的所有类
        for name, obj in inspect.getmembers(module, inspect.isclass):
            # 判断类是否是 FieldRule 的子类，并且不等于 FieldRule 本身
            if issubclass(obj, FieldRule) and obj is not FieldRule:
                RULES_REGISTRY[to_camel_case(name)] = obj


# 自动注册规则
auto_register_rules(__name__)
