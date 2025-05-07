# -*- coding: utf-8 -*-

import json
import dataclasses
from pathlib import Path

import jinja2
import requests


@dataclasses.dataclass
class ServicePrincipal:
    var_name: str
    principal: str


def get_service_principal_list() -> list[ServicePrincipal]:
    """
    从 AWS 提供的策略生成器中提取 Service Principal 列表. 这个列表是 AWS 官方工具
    `AWS Policy Generator <https://awspolicygen.s3.amazonaws.com/policygen.html>`_
    的底层组件.
    """
    url = "https://awspolicygen.s3.amazonaws.com/js/policies.js"
    res = requests.get(url)
    content = res.text
    content = content.replace("app.PolicyEditorConfig=", "")
    data = json.loads(content)
    mapping = dict()
    name_mapping = {
        "lambda": "lambda_",
    }
    for _, dct in data["serviceMap"].items():
        string_prefix = dct["StringPrefix"]
        var_name = string_prefix.replace("-", "_")
        var_name = name_mapping.get(var_name, var_name)
        principal = f"{string_prefix}.amazonaws.com"
        mapping[var_name] = principal
    sp_list = [
        ServicePrincipal(var_name=var_name, principal=principal)
        for var_name, principal in sorted(mapping.items(), key=lambda x: x[0])
    ]
    return sp_list


def gen_code(sp_list: list[ServicePrincipal]):
    """
    生成代码.
    """
    dir_here = Path(__file__).absolute().parent
    path_tpl = dir_here / "service_principal_enum.jinja"
    path_out = dir_here / "service_principal_enum.py"
    template = jinja2.Template(path_tpl.read_text())
    content = template.render(sp_list=sp_list)
    path_out.write_text(content)


if __name__ == "__main__":
    sp_list = get_service_principal_list()
    gen_code(sp_list)
