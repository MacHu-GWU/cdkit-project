# -*- coding: utf-8 -*-

"""
IAM policy document builders.

Provides utilities for creating and managing complete AWS IAM policy documents.
Includes builders for common policy types and helpers to combine policy statements
into properly formatted policy documents.
"""

import typing as T

import aws_cdk as cdk
import aws_cdk.aws_iam as iam

from func_args.api import T_OPT_KWARGS

from . import policy_statement


def create_get_caller_identity_document(
    policy_statement_kwargs: T_OPT_KWARGS = None,
    policy_document_kwargs: T_OPT_KWARGS = None,
) -> iam.PolicyDocument:
    """
    Allows the caller to get their identity.
    """
    if policy_document_kwargs is None:  # pragma: no cover
        policy_document_kwargs = {}
    return iam.PolicyDocument(
        statements=[
            policy_statement.create_get_caller_identity_statement(
                policy_statement_kwargs=policy_statement_kwargs,
            )
        ],
        **policy_document_kwargs,
    )


def create_assume_role_document(
    role_to_assume_arn_list: list[str],
    policy_statement_kwargs: T_OPT_KWARGS = None,
    policy_document_kwargs: T_OPT_KWARGS = None,
) -> iam.PolicyDocument:
    """
    Allow assuming specific roles.

    :param role_to_assume_arn_list: List of ARNs of roles to assume.
    """
    if policy_document_kwargs is None:  # pragma: no cover
        policy_document_kwargs = {}
    return iam.PolicyDocument(
        statements=[
            policy_statement.create_assume_role_statement(
                role_to_assume_arn_list=role_to_assume_arn_list,
                policy_statement_kwargs=policy_statement_kwargs,
            )
        ],
        **policy_document_kwargs,
    )
