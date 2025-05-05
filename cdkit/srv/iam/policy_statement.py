# -*- coding: utf-8 -*-

"""
IAM policy statement constructors.

Provides factory functions and helper classes to create AWS IAM policy statements
with correct structure and syntax. Simplifies the creation of common permission
patterns while ensuring policy best practices.
"""

import typing as T

import aws_cdk as cdk
import aws_cdk.aws_iam as iam

from func_args.api import T_OPT_KWARGS


def create_get_caller_identity_statement(
    policy_statement_kwargs: T_OPT_KWARGS = None,
) -> iam.PolicyStatement:
    """
    Allows the caller to get their identity.
    """
    if policy_statement_kwargs is None:  # pragma: no cover
        policy_statement_kwargs = {}
    return iam.PolicyStatement(
        actions=["sts:GetCallerIdentity"],
        resources=["*"],
        **policy_statement_kwargs,
    )


def create_assume_role_statement(
    role_to_assume_arn_list: list[str],
    policy_statement_kwargs: T_OPT_KWARGS = None,
) -> iam.PolicyStatement:
    """
    Allows assuming specific roles.

    :param role_to_assume_arn_list: List of ARNs of roles to assume.
    """
    if policy_statement_kwargs is None:  # pragma: no cover
        policy_statement_kwargs = {}
    return iam.PolicyStatement(
        actions=["sts:AssumeRole"],
        resources=role_to_assume_arn_list,
        **policy_statement_kwargs,
    )
