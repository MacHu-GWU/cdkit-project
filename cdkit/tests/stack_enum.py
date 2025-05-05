# -*- coding: utf-8 -*-

import dataclasses
from functools import cached_property

import aws_cdk as cdk
import cdkit.api as cdkit

from .bsm_enum import bsm_enum
from .stack_ctx_enum import stack_ctx_enum

from .stacks.github_oidc import GitHubOidcProviderStack
from .stacks.github_oidc import GitHubOidcSingleAccountStack
from .stacks.github_oidc import GitHubOidcMultiAccountDevopsStack
from .stacks.github_oidc import GitHubOidcMultiAccountWorkloadStack


@dataclasses.dataclass
class StackEnum:
    app: cdk.App = dataclasses.field()

    @cached_property
    def github_oidc_provider(self):
        return GitHubOidcProviderStack(
            scope=self.app,
            params=stack_ctx_enum.github_oidc_provider.to_stack_params(),
            github_oidc_provider_params=cdkit.iam.GitHubOidcProviderParams(),
        )

    @cached_property
    def github_oidc_single_account_devops(self):  # pragma: no cover
        return GitHubOidcSingleAccountStack(
            scope=self.app,
            params=stack_ctx_enum.github_oidc_single_account_devops.to_stack_params(),
            github_oidc_single_account_params=cdkit.iam.GitHubOidcSingleAccountParams(
                role_name=f"{stack_ctx_enum.github_oidc_single_account_devops.stack_name}-role-{cdk.Aws.REGION}",
                repo_patterns="MacHu-GWU/cdkit-project",
            ),
        )

    @cached_property
    def github_oidc_multi_account_devops(self):  # pragma: no cover
        return GitHubOidcMultiAccountDevopsStack(
            scope=self.app,
            params=stack_ctx_enum.github_oidc_multi_account_devops.to_stack_params(),
            github_oidc_multi_account_devops_params=cdkit.iam.GitHubOidcMultiAccountDevopsParams(
                role_name=f"{stack_ctx_enum.github_oidc_multi_account_devops.stack_name}-role-{cdk.Aws.REGION}",
                repo_patterns="MacHu-GWU/cdkit-project",
                workload_iam_role_arn_list=[
                    f"arn:aws:iam::{bsm_enum.dev.aws_account_id}:role/{stack_ctx_enum.github_oidc_multi_account_dev.stack_name}-role-{cdk.Aws.REGION}"
                ],
            ),
        )

    @cached_property
    def github_oidc_multi_account_dev(self):  # pragma: no cover
        devops_role_name = f"{stack_ctx_enum.github_oidc_multi_account_devops.stack_name}-role-{cdk.Aws.REGION}"
        devops_account_id = bsm_enum.devops.aws_account_id
        devops_iam_role_arn = (
            f"arn:aws:iam::{devops_account_id}:role/{devops_role_name}"
        )
        return GitHubOidcMultiAccountWorkloadStack(
            scope=self.app,
            params=stack_ctx_enum.github_oidc_multi_account_dev.to_stack_params(),
            github_oidc_multi_account_workload_params=cdkit.iam.GitHubOidcMultiAccountWorkloadParams(
                role_name=f"{stack_ctx_enum.github_oidc_multi_account_dev.stack_name}-role-{cdk.Aws.REGION}",
                devops_iam_role_arn=devops_iam_role_arn,
            ),
        )


stack_enum = StackEnum(app=cdk.App())
