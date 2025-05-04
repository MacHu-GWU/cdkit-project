# -*- coding: utf-8 -*-

"""

"""

import typing as T

import aws_cdk as cdk
import aws_cdk.aws_iam as iam
from constructs import Construct


def create_github_oidc_provider(
    scope: Construct,
    id: str,
    url: str = "https://token.actions.githubusercontent.com",
    client_id_list: T.Optional[list[str]] = None,
    thumbprint_list: T.Optional[list[str]] = None,
) -> iam.CfnOIDCProvider:
    """
    Create a GitHub OIDC Provider in AWS IAM.

    This function creates an OIDC provider configuration that allows GitHub Actions
    to authenticate with AWS using short-lived tokens instead of long-term credentials.
    The provider is configured with standard GitHub token URL and thumbprint.

    Ref: https://github.com/aws-actions/configure-aws-credentials
    """
    if client_id_list is None:
        client_id_list = ["sts.amazonaws.com"]
    if thumbprint_list is None:
        thumbprint_list = ["6938fd4d98bab03faadb97b34396831e3780aea1"]
    return cdk.aws_iam.CfnOIDCProvider(
        scope=scope,
        id=id,
        url=url,
        client_id_list=client_id_list,
        thumbprint_list=thumbprint_list,
    )


GITHUB_OIDC_PROVIDER_ARN = (
    f"arn:aws:iam::{cdk.Aws.ACCOUNT_ID}:oidc-provider/"
    "token.actions.githubusercontent.com"
)


def create_github_repo_main_iam_role_assumed_by(
    repo_patterns: T.Union[str, T.List[str]],
    federated: str = GITHUB_OIDC_PROVIDER_ARN,
) -> iam.FederatedPrincipal:
    """
    Create a FederatedPrincipal for GitHub OIDC authentication.

    Creates an IAM FederatedPrincipal that allows GitHub Actions to assume
    the role via OIDC authentication.

    Usage Example::

        iam.Role(
            scope=...,
            id=...,
            role_name=...,
            assumed_by=create_github_repo_main_iam_role_assumed_by(
                repo_patterns=...,
                federated=...,
            ),
            inline_policies=inline_policies,
        )

    :param repo_patterns: GitHub repository pattern(s) allowed to assume the role.
        Can be a single pattern string or a list of patterns.
        Example: "repo:organization/repo-name:*" or
        ["repo:org/repo1:*", "repo:org/repo2:*"].
    :param federated: ARN of the OIDC provider. Defaults to GitHub's OIDC provider.
    """
    return iam.FederatedPrincipal(
        federated=federated,
        assume_role_action="sts:AssumeRoleWithWebIdentity",
        conditions={
            "StringEquals": {
                "token.actions.githubusercontent.com:aud": "sts.amazonaws.com",
            },
            "StringLike": {
                "token.actions.githubusercontent.com:sub": repo_patterns,
            },
        },
    )
