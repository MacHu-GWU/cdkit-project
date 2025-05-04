# -*- coding: utf-8 -*-

import typing as T

import aws_cdk as cdk
import aws_cdk.aws_iam as iam

from ...type_hint import T_OPT_KWARGS

from . import policy_statement


def create_get_caller_identity_document(
    policy_statement_kwargs: T_OPT_KWARGS = None,
    policy_document_kwargs: T_OPT_KWARGS = None,
) -> iam.PolicyDocument:
    """
    Create a policy document that allows the caller to get their identity.
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
    Create a policy document that only has one permission, which is
    to allow assuming roles.

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
