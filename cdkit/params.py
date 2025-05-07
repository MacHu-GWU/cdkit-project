# -*- coding: utf-8 -*-

"""
Parameter Management System for AWS CDK

This module provides a type-safe, extendable parameter system for AWS CDK constructs
and stacks using Python dataclasses. The motivation for this system is to address
limitations when subclassing CDK constructs like cdk.Stack:

1. Because cdk Python uses ``def __init__(self, ...):``, subclassing requires
    repeating parameter definitions to maintain type hints
2. Using ``**kwargs`` loses type information and IDE completion support
3. Validation of required parameters is handled manually and inconsistently
"""

import typing as T
import dataclasses

from func_args.api import REQ, OPT, remove_optional, T_KWARGS, BaseModel


if T.TYPE_CHECKING:  # pragma: no cover
    import aws_cdk as cdk


@dataclasses.dataclass
class ConstructParams(BaseModel):
    """
    Parameter dataclass for CDK Construct initialization.

    How to extend::

        import dataclasses
        from func_args.api import REQ

        @dataclasses.dataclass
        class MyConstructParams(ConstructParams):
            your_custom_param_1: int = dataclasses.field(default=REQ)
            your_custom_param_2: str = dataclasses.field(default="my_default_value")
    """

    id: str = dataclasses.field(default=REQ)

    def to_construct_kwargs(self) -> T_KWARGS:
        """
        Generate keyword arguments for CDK construct initialization.

        .. note::

            To generate keyword arguments for all declared attributes,
            use the ``.to_kwargs()`` method.
        """
        return remove_optional(id=self.id)


@dataclasses.dataclass
class StackParams(ConstructParams):
    """
    Parameter dataclass for CDK Stack initialization.

    How to extend::

        import dataclasses
        from func_args.api import REQ

        @dataclasses.dataclass
        class MyStackParams(StackParams):
            your_custom_param_1: int = dataclasses.field(default=REQ)
            your_custom_param_2: str = dataclasses.field(default="my_default_value")
    """

    analytics_reporting: bool = dataclasses.field(default=OPT)
    cross_region_references: bool = dataclasses.field(default=OPT)
    description: str = dataclasses.field(default=OPT)
    env: T.Union["cdk.Environment", dict[str, T.Any]] = dataclasses.field(default=OPT)
    notification_arns: T.Sequence[str] = dataclasses.field(default=OPT)
    permissions_boundary: "cdk.PermissionsBoundary" = dataclasses.field(default=OPT)
    stack_name: str = dataclasses.field(default=OPT)
    suppress_template_indentation: bool = dataclasses.field(default=OPT)
    synthesizer: "cdk.IStackSynthesizer" = dataclasses.field(default=OPT)
    tags: T.Mapping[str, str] = dataclasses.field(default=OPT)
    termination_protection: bool = dataclasses.field(default=OPT)

    def to_stack_kwargs(self) -> T_KWARGS:
        """
        Generate keyword arguments for CDK Stack initialization.

        .. note::

            To generate keyword arguments for all declared attributes,
            use the ``.to_kwargs()`` method.
        """
        return remove_optional(
            id=self.id,
            analytics_reporting=self.analytics_reporting,
            cross_region_references=self.cross_region_references,
            description=self.description,
            env=self.env,
            notification_arns=self.notification_arns,
            permissions_boundary=self.permissions_boundary,
            stack_name=self.stack_name,
            suppress_template_indentation=self.suppress_template_indentation,
            synthesizer=self.synthesizer,
            tags=self.tags,
            termination_protection=self.termination_protection,
        )
