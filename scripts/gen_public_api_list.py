# -*- coding: utf-8 -*-

import inspect
import dataclasses
from pathlib import Path

import jinja2
import cdkit.api as cdkit
from cdkit.paths import dir_project_root

non_service_modules = [
    "ConstructParams",
    "StackParams",
    "BaseConstruct",
    "BaseStack",
    "stacks",
]

service_public_api_list = []
for module_name, module in cdkit.__dict__.items():
    if module_name.startswith("_") is False:
        if module_name not in non_service_modules:
            for var_name, var in module.__dict__.items():
                if var_name.startswith("_") is False:
                    path = f"cdkit.api.{module_name}.{var_name}"
                    if inspect.isclass(var):
                        type = "class"
                        ref = f"{var.__module__}.{var_name}"
                        api = f":{type}:`{path} <{ref}>`"
                    elif inspect.isfunction(var):
                        type = "func"
                        ref = f"{var.__module__}.{var_name}"
                        api = f":{type}:`{path} <{ref}>`"
                    else:
                        search_url = f"https://cdkit.readthedocs.io/en/latest/search.html?q={module_name}.{var_name}&check_keywords=yes&area=default"
                        api = f"`{path} <{search_url}>`_"
                    service_public_api_list.append(api)


stack_public_api_list = []
for module_name, module in cdkit.stacks.__dict__.items():
    if module_name.startswith("_") is False:
        for var_name, var in module.__dict__.items():
            if var_name.startswith("_") is False:
                path = f"cdkit.api.stacks.{module_name}.{var_name}"
                if inspect.isclass(var):
                    ref = f":class:`{path} <{var.__module__}.{var.__qualname__}>`"
                else:
                    raise NotImplementedError
                stack_public_api_list.append(ref)

dir_here = Path(__file__).absolute().parent
path_tpl = dir_here / "public_api_list.jinja"
path_out_1 = dir_here / "public_api_list.rst"
path_out_2 = dir_project_root / "docs" / "source" / "01-Public-APIs" / "index.rst"
tpl = jinja2.Template(path_tpl.read_text())
content = tpl.render(
    service_public_api_list=service_public_api_list,
    stack_public_api_list=stack_public_api_list,
)
path_out_1.write_text(content)
path_out_2.write_text(content)
