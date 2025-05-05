# -*- coding: utf-8 -*-

import dataclasses

from func_args.api import REQ, OPT

from cdkit.params import ConstructParams, StackParams


@dataclasses.dataclass
class MyConstructParams(ConstructParams):
    name: str = dataclasses.field(default=REQ)
    age: int = dataclasses.field(default=OPT)


class TestConstructParams:
    def test(self):
        construct_params = MyConstructParams(
            id="MyConstruct",
            name="Alice",
        )
        assert construct_params.to_construct_kwargs() == {"id": "MyConstruct"}
        assert construct_params.to_kwargs() == {"id": "MyConstruct", "name": "Alice"}


@dataclasses.dataclass
class MyStackParams(StackParams):
    name: str = dataclasses.field(default=REQ)
    age: int = dataclasses.field(default=OPT)


class TestStackParams:
    def test(self):
        stack_params = StackParams(
            id="MyStack",
            stack_name="MyStackName",
        )
        kwargs = stack_params.to_stack_kwargs()
        assert kwargs == {
            "id": "MyStack",
            "stack_name": "MyStackName",
        }
        assert stack_params.to_kwargs() == {
            "id": "MyStack",
            "stack_name": "MyStackName",
        }


if __name__ == "__main__":
    from cdk_mate.tests import run_cov_test

    run_cov_test(
        __file__,
        "cdkit.params",
        preview=False,
    )
