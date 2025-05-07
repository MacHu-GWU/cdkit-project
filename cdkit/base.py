# -*- coding: utf-8 -*-

"""
Base classes for AWS CDK constructs and stacks with integrated parameter management.

This module provides base classes that integrate AWS CDK constructs and stacks with
the parameter system defined in :mod:`cdkit.params`. The integration eliminates
repetitive parameter definition code by leveraging Python dataclasses to create
strongly-typed, validated configuration objects.
"""

import aws_cdk as cdk
from constructs import Construct

from .params import ConstructParams, StackParams


class BaseConstruct(Construct):
    """
    Base class for AWS CDK constructs with integrated parameter management.

    Example, define a custom construct with typed parameters:

    .. code-block:: python

        import dataclasses
        from cdkit.api import BaseConstruct, ConstructParams, REQ

        @dataclasses.dataclass
        class BucketParams(ConstructParams):
            bucket_name: str = dataclasses.field(default=REQ)
            versioned: bool = dataclasses.field(default=False)

        class S3Bucket(BaseConstruct):
            def __init__(
                self,
                scope: Construct,
                params: BucketParams,
            ):
                super().__init__(scope=scope, params=params)
                self.params = params # this is for type hint

                # Access parameters via self.params
                bucket = s3.Bucket(
                    self, "Bucket",
                    bucket_name=self.params.bucket_name,
                    versioned=self.params.versioned,
                )
    """

    def __init__(
        self,
        scope: Construct,
        params: ConstructParams,
    ):
        super().__init__(scope=scope, **params.to_construct_kwargs())
        self.params = params


class BaseStack(cdk.Stack):
    """
    Base class for AWS CDK stacks with integrated parameter management.

    This class extends the standard cdk.Stack class with parameter management
    capabilities, enabling a more structured and type-safe approach to stack
    configuration. It serves as the foundation for all CDK stacks in the project,
    providing consistency in initialization and access to stack parameters.

    :param scope: The CDK construct scope (typically a Stack or another Construct)
    :param params: Parameter object containing all construct configuration,
        must be an instance of :class:`~cdkit.params.ConstructParams` or a subclass

    Example: create a subclass of BaseStack and pass your custom stack parameters:

    .. code-block:: python

        import dataclasses
        import aws_cdk as cdk
        from constructs import Construct
        from cdkit.api import BaseStack, StackParams, REQ

        @dataclasses.dataclass
        class MyStackParams(StackParams):
            project_name: str = dataclasses.field(default=REQ)
            env_name: str = dataclasses.field(default=REQ)

        class MyStack(BaseStack):
            def __init__(
                self,
                scope: Construct,
                params: MyStackParams,
            ):
                super().__init__(scope=scope, params=params)
                self.params = params # this is for type hint

                cdk.Tags.of(self).add("tech:project_name", self.params.project_name)
                cdk.Tags.of(self).add("tech:env_name", self.params.env_name)
    """

    def __init__(
        self,
        scope: Construct,
        params: StackParams,
    ):
        super().__init__(scope=scope, **params.to_stack_kwargs())
        self.params = params
