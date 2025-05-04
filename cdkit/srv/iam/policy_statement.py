# -*- coding: utf-8 -*-

import typing as T

import aws_cdk as cdk
import aws_cdk.aws_iam as iam

from ...type_hint import T_OPT_KWARGS


def create_get_caller_identity_statement(
    policy_statement_kwargs: T_OPT_KWARGS = None,
) -> iam.PolicyStatement:
    """
    Create a policy document that allows the caller to get their identity.
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
    Create a policy statement that allows assuming roles.

    :param role_to_assume_arn_list: List of ARNs of roles to assume.
    """
    if policy_statement_kwargs is None:  # pragma: no cover
        policy_statement_kwargs = {}
    return iam.PolicyStatement(
        actions=["sts:AssumeRole"],
        resources=role_to_assume_arn_list,
        **policy_statement_kwargs,
    )
