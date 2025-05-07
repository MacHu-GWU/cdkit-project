# -*- coding: utf-8 -*-

import aws_cdk as cdk
from constructs import Construct


class MyStack(cdk.Stack):
    def __init__(
        self,
        scope: Construct,
        id: str,
        stack_name: str,
        env: cdk.Environment,
        your_custom_param_1: int,
        your_custom_param_2: str = "my_default_value",
        **kwargs,  # more parameters for the default cdk.Stack.__init__
    ):
        super().__init__(
            scope=scope,
            id=id,
            stack_name=stack_name,
            env=env,
            **kwargs,
        )
        self.your_custom_param_1 = your_custom_param_1
        self.your_custom_param_2 = your_custom_param_2


app = cdk.App()
stack = MyStack(
    scope=app,
    id="...",
    stack_name="my_stack_name",
    env=cdk.Environment(
        account="...",
        region="...",
    ),
    your_custom_param_1=42,
    your_custom_param_2="my_custom_value",
)
