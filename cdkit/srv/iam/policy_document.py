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


def create_power_ops_document(
    policy_name: str,
    prefix: str,
) -> iam.PolicyDocument:
    """
    Create an IAM policy document that grants broad AWS access with strict identity management controls.

    :param policy_name: The name of the IAM policy to be used as a permissions boundary for role creation.
    :param prefix: The required prefix for IAM roles and policies that users are allowed to manage.

    🎯 Scope of Permissions

    - Grants broad operational capabilities, excluding identity management.
      Users can perform actions across most AWS services—similar to having "Administrator" access—
      but are explicitly restricted from managing the following identity-related services:
        - AWS IAM
        - AWS Organizations
        - AWS Account

    🛡️ Identity Management Restrictions and Exceptions

    - Read-only access to IAM, Organizations, and Account services.
      Users can view configuration details of these resources but cannot create or modify them.

    - Fine-grained IAM access control:
        - Users are allowed to manage only IAM roles and policies that start with a designated company-specific prefix (e.g., "ESC").
            - For example, users can create, update, or delete roles like `ESC-MyServiceRole`.
            - Roles that do not start with the prefix are protected and cannot be modified, ensuring critical permissions are not compromised.
        - All IAM resources (regardless of prefix) are readable, allowing users to inspect existing role configurations.

    🧱 Enforced Permissions Boundary for Role Creation

    - When creating a new IAM role, users must attach the current IAM policy as a permissions boundary.
    - This prevents privilege escalation scenarios (e.g., creating a new role with full admin access and assuming it).
    - All new roles inherit the boundary, ensuring their permissions remain within the limits defined by this policy.

    ✅ Summary

    This policy establishes a model of **“controlled high-level access”**:

    - Users can perform most day-to-day operational tasks, including deployment, maintenance, and AWS service management.
    - Identity management is tightly restricted to specific prefixed IAM roles.
    - The enforced permissions boundary mechanism ensures no user can exceed the defined privilege scope, maintaining system security and control.
    """
    return iam.PolicyDocument(
        statements=[
            policy_statement.create_allow_all_services_except_identity_management_statement(),
            policy_statement.create_account_and_org_and_iam_read_only_statement(),
            policy_statement.create_prefixed_iam_management_statement(prefix=prefix),
            policy_statement.create_require_permission_boundary_for_role_creation_statement(
                policy_name=policy_name,
            ),
        ]
    )


def create_restricted_read_only_document(
    policy_name: str,
) -> iam.PolicyDocument:
    """
    Create an IAM policy document that grant read-only access across a wide range
    of AWS services, excluding any write or management actions.

    :param policy_name: The name of the IAM policy to be used as a
        permissions boundary for role creation.
    """
    return iam.PolicyDocument(
        statements=[
            policy_statement.create_restricted_read_only_statement(),
            policy_statement.create_require_permission_boundary_for_role_creation_statement(
                policy_name=policy_name,
            ),
        ]
    )
