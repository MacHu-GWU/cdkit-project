# -*- coding: utf-8 -*-

import dataclasses

import aws_cdk as cdk
from constructs import Construct

import cdkit.api as cdkit
from func_args.api import REQ


@dataclasses.dataclass
class MyStackParams(cdkit.StackParams):
    your_custom_param_1: int = dataclasses.field(default=REQ)
    your_custom_param_2: str = dataclasses.field(default="my_default_value")


class MyStack(cdkit.BaseStack):
    def __init__(
        self,
        scope: Construct,
        params: MyStackParams,
    ):
        super().__init__(scope=scope, params=params)
        self.params = params


app = cdk.App()
stack = MyStack(
    scope=app,
    params=MyStackParams(
        id="...",
        stack_name="my_stack_name",
        env=cdk.Environment(
            account="...",
            region="...",
        ),
        your_custom_param_1=42,
        your_custom_param_2="my_custom_value",
    ),
)
