# -*- coding: utf-8 -*-

"""
Provides functionality to create
`GitHub OpenID Connect <https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services>`_
providers and IAM roles that can be assumed by GitHub Actions workflows.
"""

import typing as T
import dataclasses

import aws_cdk as cdk
import aws_cdk.aws_iam as iam
from constructs import Construct
from func_args.api import REQ, OPT, remove_optional

from ...base import BaseConstruct
from ...params import ConstructParams

from .utils import role_name_to_inline_policy_name


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
"""
GitHub OIDC Provider ARN in AWS is always in this format.
"""


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


@dataclasses.dataclass
class GitHubOidcProviderParams(ConstructParams):
    """
    Parameters for creating a GitHub OIDC provider.

    See :class:`GitHubOidcProvider`
    """

    # fmt: off
    id: str = dataclasses.field(default="GitHubOidcProviderConstruct")
    github_oidc_provider_res_id: str = dataclasses.field(default="GitHubOidcProviderResource")
    url: str = dataclasses.field(default="https://token.actions.githubusercontent.com")
    client_id_list: list[str] = dataclasses.field(default=OPT)
    thumbprint_list: list[str] = dataclasses.field(default=OPT)
    # fmt: on


class GitHubOidcProvider(BaseConstruct):
    """
    Construct for creating a GitHub OIDC provider in AWS IAM.

    :param params: :class:`GitHubOidcProviderParams`
    """

    def __init__(
        self,
        scope: Construct,
        params: GitHubOidcProviderParams,
    ):
        super().__init__(scope=scope, params=params)
        self.params = params

        self.create_github_oidc_provider()

    def create_github_oidc_provider(self):
        self.github_oidc_provider = create_github_oidc_provider(
            scope=self,
            **remove_optional(
                id=self.params.github_oidc_provider_res_id,
                url=self.params.url,
                client_id_list=self.params.client_id_list,
                thumbprint_list=self.params.thumbprint_list,
            ),
        )


@dataclasses.dataclass
class SingleRoleWithInlinePolicyConstructParams(ConstructParams):
    role_name: str = dataclasses.field(default=REQ)

    @property
    def inline_policy_name(self) -> str:
        return role_name_to_inline_policy_name(self.role_name)


@dataclasses.dataclass
class GitHubOidcSingleAccountParams(SingleRoleWithInlinePolicyConstructParams):
    """
    Parameters for creating a GitHub OIDC role in a single AWS account setup.

    See :class:`GitHubOidcSingleAccount`
    """

    # fmt: off
    id: str = dataclasses.field(default="GitHubOidcSingleAccountConstruct")
    github_repo_main_iam_role_res_id: str = dataclasses.field(default="GitHubRepoMainIamRole")
    repo_patterns: T.Union[str, T.List[str]] = dataclasses.field(default=REQ)
    federated: str = dataclasses.field(default=GITHUB_OIDC_PROVIDER_ARN)
    # fmt: on


class GitHubOidcSingleAccount(BaseConstruct):
    """
    Construct for creating an IAM role assumable by GitHub Actions.

    The role can be assumed directly by GitHub Actions and has the permission
    to perform deployment related AWS actions directly.

    :param params: :class:`GitHubOidcSingleAccountParams`
    """

    def __init__(
        self,
        scope: Construct,
        params: GitHubOidcSingleAccountParams,
    ):
        super().__init__(scope=scope, params=params)
        self.params = params

        self.create_github_repo_main_iam_role()

    def create_github_repo_main_iam_role_inline_policy_document(
        self,
    ) -> iam.PolicyDocument:
        """
        Implement this method to return the inline policy document for the IAM role.

        Example:

        .. code-block:: python

            def ...(...) -> ...:
                return iam.PolicyDocument(
                    statements=[
                        iam.PolicyStatement(
                            actions=...,
                            resources=...,
                        ),
                    ],
                )
        """
        raise NotImplementedError(
            "You need to implement the "
            f"`{self.create_github_repo_main_iam_role_inline_policy_document}` method!"
            f"This method should return an instance of `iam.PolicyDocument` for ..."
        )
        # Example:
        # return iam.PolicyDocument(
        #     statements=[
        #         iam.PolicyStatement(
        #             actions=...,
        #             resources=...,
        #         ),
        #     ],
        # )

    def create_github_repo_main_iam_role(self):
        """
        Create the main IAM role that will be assumed by GitHub Actions.

        .. note::

            User can override this method to customize the IAM role creation.
        """
        self.github_repo_main_iam_role = iam.Role(
            scope=self,
            id=self.params.github_repo_main_iam_role_res_id,
            description="GitHub OIDC DevOps main IAM role that will be assumed by GitHub Actions",
            role_name=self.params.role_name,
            assumed_by=create_github_repo_main_iam_role_assumed_by(
                repo_patterns=self.params.repo_patterns,
                federated=self.params.federated,
            ),
            inline_policies={
                self.params.inline_policy_name: self.create_github_repo_main_iam_role_inline_policy_document(),
            },
        )


@dataclasses.dataclass
class GitHubOidcMultiAccountDevopsParams(SingleRoleWithInlinePolicyConstructParams):
    """
    Parameters for creating a GitHub OIDC devops role in a multi AWS account setup.

    See :class:`GitHubOidcMultiAccountDevops`
    """

    # fmt: off
    id: str = dataclasses.field(default="GitHubOidcMultiAccountDevopsConstruct")
    github_repo_main_iam_role_res_id: str = dataclasses.field(default="GitHubRepoMainIamRole")
    repo_patterns: T.Union[str, T.List[str]] = dataclasses.field(default=REQ)
    workload_iam_role_arn_list: T.List[str] = dataclasses.field(default=REQ)
    federated: str = dataclasses.field(default=GITHUB_OIDC_PROVIDER_ARN)
    # fmt: on


class GitHubOidcMultiAccountDevops(BaseConstruct):
    """
    Construct for creating a GitHub OIDC devops role in a multi AWS account setup.

    This role can be assumed by GitHub Actions and has the permission to assume
    other roles in different AWS accounts.

    :param params: :class:`GitHubOidcMultiAccountDevopsParams`
    """

    def __init__(
        self,
        scope: Construct,
        params: GitHubOidcMultiAccountDevopsParams,
    ):
        super().__init__(scope=scope, params=params)
        self.params = params

        self.create_github_repo_main_iam_role()

    def create_github_repo_main_iam_role_inline_policy_document(
        self,
    ) -> iam.PolicyDocument:
        return iam.PolicyDocument(
            statements=[
                iam.PolicyStatement(
                    actions=["sts:AssumeRole"],
                    resources=self.params.workload_iam_role_arn_list,
                )
            ]
        )

    def create_github_repo_main_iam_role(self):
        """
        Create the main IAM role that will be assumed by GitHub Actions.

        .. note::

            User can override this method to customize the IAM role creation.
        """
        self.github_repo_main_iam_role = iam.Role(
            scope=self,
            id=self.params.github_repo_main_iam_role_res_id,
            description="GitHub OIDC DevOps main IAM role that will be assumed by GitHub Actions",
            role_name=self.params.role_name,
            assumed_by=create_github_repo_main_iam_role_assumed_by(
                repo_patterns=self.params.repo_patterns,
                federated=self.params.federated,
            ),
            inline_policies={
                self.params.inline_policy_name: self.create_github_repo_main_iam_role_inline_policy_document(),
            },
        )


@dataclasses.dataclass
class GitHubOidcMultiAccountWorkloadParams(SingleRoleWithInlinePolicyConstructParams):
    """
    Parameters for creating a GitHub OIDC workload role.

    See :class:`GitHubOidcMultiAccountWorkload`
    """

    # fmt: off
    id: str = dataclasses.field(default="GitHubOidcMultiAccountWorkloadConstruct")
    github_repo_workload_iam_role_res_id: str = dataclasses.field(default="GitHubRepoWorkloadIamRole")
    devops_iam_role_arn: str = dataclasses.field(default=REQ)
    # fmt: on


class GitHubOidcMultiAccountWorkload(BaseConstruct):
    """
    Construct for creating a workload IAM role in a multi-account setup.

    This role can be assumed by a devops IAM role, and it has the permission to
    perform deployment related AWS actions.

    :param params: :class:`GitHubOidcMultiAccountWorkloadParams`
    """

    def __init__(
        self,
        scope: Construct,
        params: GitHubOidcMultiAccountWorkloadParams,
    ):
        super().__init__(scope=scope, params=params)
        self.params = params

        self.create_github_repo_workload_iam_role()

    def create_github_repo_workload_iam_role_inline_policy_document(
        self,
    ) -> iam.PolicyDocument:
        """
        Implement this method to return the inline policy document for the IAM role.

        Example:

        .. code-block:: python

            def ...(...) -> ...:
                return iam.PolicyDocument(
                    statements=[
                        iam.PolicyStatement(
                            actions=...,
                            resources=...,
                        ),
                    ],
                )
        """
        raise NotImplementedError(
            "You need to implement the "
            f"`{self.create_github_repo_workload_iam_role_inline_policy_document}` method!"
            f"This method should return an instance of `iam.PolicyDocument` for ..."
        )
        # Example:
        # return iam.PolicyDocument(
        #     statements=[
        #         iam.PolicyStatement(
        #             actions=...,
        #             resources=...,
        #         ),
        #     ],
        # )

    def create_github_repo_workload_iam_role(self):
        """
        Create the main IAM role that will be assumed by GitHub Actions.

        .. note::

            User can override this method to customize the IAM role creation.
        """
        self.github_repo_workload_iam_role = iam.Role(
            scope=self,
            id=self.params.github_repo_workload_iam_role_res_id,
            description="GitHub OIDC workload IAM role that will be assumed by the DevOps role",
            role_name=self.params.role_name,
            assumed_by=iam.ArnPrincipal(
                arn=self.params.devops_iam_role_arn,
            ),
            inline_policies={
                self.params.inline_policy_name: self.create_github_repo_workload_iam_role_inline_policy_document(),
            },
        )
