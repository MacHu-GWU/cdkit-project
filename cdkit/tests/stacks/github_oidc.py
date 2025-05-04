# -*- coding: utf-8 -*-

import aws_cdk as cdk
import aws_cdk.aws_iam as iam
from constructs import Construct

import cdkit.api as cdkit

GitHubOidcProviderStack = cdkit.cstr.GitHubOidcProviderStack


class GitHubOidcSingleAccountStack(cdkit.cstr.GitHubOidcSingleAccountStack):
    def create_github_repo_main_iam_role_inline_policy_document(self):
        return cdkit.srv.iam.create_get_caller_identity_document()


GitHubOidcMultiAccountDevopsStack = cdkit.cstr.GitHubOidcMultiAccountDevopsStack


class GitHubOidcMultiAccountWorkloadStack(cdk.Stack):
    """ """

    def __init__(
        self,
        scope: Construct,
        id: str,
        stack_name: str,
        env: cdk.Environment,
        # --- GitHub OIDC provider parameters ---
        role_name: str,
        devops_iam_role_arn: str,
    ):
        super().__init__(
            scope=scope,
            id=id,
            stack_name=stack_name,
            env=env,
        )
        self.role_name = role_name
        self.devops_iam_role_arn = devops_iam_role_arn

        self.create_github_repo_workload_iam_role()

    def create_github_repo_workload_iam_role(self):
        inline_policy_name = cdkit.srv.iam.role_name_to_inline_policy_name(
            self.role_name
        )
        inline_policy_document = cdkit.srv.iam.create_get_caller_identity_document()
        self.github_repo_workload_iam_role = iam.Role(
            scope=self,
            id="GitHubRepoWorkloadIamRole",
            role_name=self.role_name,
            assumed_by=iam.ArnPrincipal(
                arn=self.devops_iam_role_arn,
            ),
            inline_policies={
                inline_policy_name: inline_policy_document,
            },
        )
