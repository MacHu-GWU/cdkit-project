# -*- coding: utf-8 -*-

"""
Test for:

- :mod:`cdkit.srv.iam.github_oidc`.
- :mod:`cdkit.stacks.github_oidc_provider`.
- :mod:`cdkit.stacks.github_oidc_multi_account_devops`.
"""

import aws_cdk as cdk
import aws_cdk.aws_iam as iam
from constructs import Construct

import cdkit.api as cdkit

GitHubOidcProviderStack = cdkit.stacks.github_oidc_provider.GitHubOidcProviderStack


class GitHubOidcSingleAccount(cdkit.iam.GitHubOidcSingleAccount):
    def create_github_repo_main_iam_role_inline_policy_document(
        self,
    ) -> iam.PolicyDocument:
        return cdkit.iam.create_get_caller_identity_document()


class GitHubOidcSingleAccountStack(cdkit.BaseStack):
    def __init__(
        self,
        scope: Construct,
        params: cdkit.StackParams,
        github_oidc_single_account_params: cdkit.iam.GitHubOidcSingleAccountParams,
    ):
        super().__init__(scope=scope, params=params)
        self.params = params
        self.github_oidc_single_account = GitHubOidcSingleAccount(
            scope=self,
            params=github_oidc_single_account_params,
        )


GitHubOidcMultiAccountDevopsStack = (
    cdkit.stacks.github_oidc_multi_account_devops.GitHubOidcMultiAccountDevopsStack
)


class GitHubOidcMultiAccountWorkload(cdkit.iam.GitHubOidcMultiAccountWorkload):
    def create_github_repo_workload_iam_role_inline_policy_document(
        self,
    ) -> iam.PolicyDocument:
        return cdkit.iam.create_get_caller_identity_document()


class GitHubOidcMultiAccountWorkloadStack(cdkit.BaseStack):
    """ """

    def __init__(
        self,
        scope: Construct,
        params: cdkit.StackParams,
        github_oidc_multi_account_workload_params: cdkit.iam.GitHubOidcMultiAccountWorkloadParams,
    ):
        super().__init__(scope=scope, params=params)
        self.params = params
        self.github_oidc_multi_account_workload = GitHubOidcMultiAccountWorkload(
            scope=self,
            params=github_oidc_multi_account_workload_params,
        )
