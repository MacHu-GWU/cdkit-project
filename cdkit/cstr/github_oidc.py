# -*- coding: utf-8 -*-

import typing as T

import aws_cdk as cdk
import aws_cdk.aws_iam as iam
from constructs import Construct

from ..srv.iam.utils import role_name_to_inline_policy_name
from ..srv.iam.policy_document import create_assume_role_document
from ..srv.iam.github_oidc import (
    create_github_oidc_provider,
    GITHUB_OIDC_PROVIDER_ARN,
    create_github_repo_main_iam_role_assumed_by,
)


class GitHubOidcProviderStack(cdk.Stack):
    """ """

    def __init__(
        self,
        scope: Construct,
        id: str,
        stack_name: str,
        env: cdk.Environment,
        # --- stack parameters ---
        url: str = "https://token.actions.githubusercontent.com",
        client_id_list: T.Optional[list[str]] = None,
        thumbprint_list: T.Optional[list[str]] = None,
    ):
        super().__init__(
            scope=scope,
            id=id,
            stack_name=stack_name,
            env=env,
        )
        self.url = url
        self.client_id_list = client_id_list
        self.thumbprint_list = thumbprint_list

        self.create_github_oidc_provider()

    def create_github_oidc_provider(self):
        self.github_oidc_provider = create_github_oidc_provider(
            scope=self,
            id="GitHubOIDCProvider",
            url=self.url,
            client_id_list=self.client_id_list,
            thumbprint_list=self.thumbprint_list,
        )


class GitHubOidcSingleAccountStack(cdk.Stack):
    """
    Stack for creating a GitHub OIDC provider and IAM role for GitHub Actions.

     i.e. the iam role can be assumed by github
    action principal will do the AWS work directly.
    """

    def __init__(
        self,
        scope: Construct,
        id: str,
        stack_name: str,
        env: cdk.Environment,
        # --- GitHub OIDC provider parameters ---
        role_name: str,
        repo_patterns: T.Union[str, T.List[str]],
        federated: str = GITHUB_OIDC_PROVIDER_ARN,
    ):
        super().__init__(
            scope=scope,
            id=id,
            stack_name=stack_name,
            env=env,
        )
        self.role_name = role_name
        self.repo_patterns = repo_patterns
        self.federated = federated

        self.create_github_repo_main_iam_role()

    def create_github_repo_main_iam_role_inline_policy_document(
        self,
    ) -> iam.PolicyDocument:
        raise NotImplementedError
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
        inline_policy_name = role_name_to_inline_policy_name(self.role_name)
        inline_policy_document = (
            self.create_github_repo_main_iam_role_inline_policy_document()
        )
        self.github_repo_main_iam_role = iam.Role(
            scope=self,
            id="GitHubRepoMainIamRole",
            role_name=self.role_name,
            assumed_by=create_github_repo_main_iam_role_assumed_by(
                repo_patterns=self.repo_patterns,
                federated=self.federated,
            ),
            inline_policies={
                inline_policy_name: inline_policy_document,
            },
        )


class GitHubOidcMultiAccountDevopsStack(cdk.Stack):
    """
    The devops iam role will be assumed by the github action, and devops iam role
    has to assume to the workload iam role to do the AWS work.
    """

    def __init__(
        self,
        scope: Construct,
        id: str,
        stack_name: str,
        env: cdk.Environment,
        # --- GitHub OIDC provider parameters ---
        role_name: str,
        repo_patterns: T.Union[str, T.List[str]],
        workload_iam_role_arn_list: T.List[str],
        federated: str = GITHUB_OIDC_PROVIDER_ARN,
    ):
        super().__init__(
            scope=scope,
            id=id,
            stack_name=stack_name,
            env=env,
        )
        self.role_name = role_name
        self.repo_patterns = repo_patterns
        self.workload_iam_role_arn_list = workload_iam_role_arn_list
        self.federated = federated

        self.create_github_repo_main_iam_role()

    def create_github_repo_main_iam_role_inline_policy_document(
        self,
    ) -> iam.PolicyDocument:
        return iam.PolicyDocument(
            statements=[
                iam.PolicyStatement(
                    actions=["sts:AssumeRole"],
                    resources=self.workload_iam_role_arn_list,
                )
            ]
        )

    def create_github_repo_main_iam_role(self):
        inline_policy_name = role_name_to_inline_policy_name(self.role_name)
        inline_policy_document = (
            self.create_github_repo_main_iam_role_inline_policy_document()
        )
        self.github_repo_main_iam_role = iam.Role(
            scope=self,
            id="GitHubRepoMainIamRole",
            role_name=self.role_name,
            assumed_by=create_github_repo_main_iam_role_assumed_by(
                repo_patterns=self.repo_patterns,
                federated=self.federated,
            ),
            inline_policies={
                inline_policy_name: inline_policy_document,
            },
        )
