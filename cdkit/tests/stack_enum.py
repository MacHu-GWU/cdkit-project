# -*- coding: utf-8 -*-

import dataclasses
from functools import cached_property

import aws_cdk as cdk

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
            **stack_ctx_enum.github_oidc_provider.to_stack_kwargs(),
        )

    @cached_property
    def github_oidc_single_account_devops(self):  # pragma: no cover
        return GitHubOidcSingleAccountStack(
            scope=self.app,
            **stack_ctx_enum.github_oidc_single_account_devops.to_stack_kwargs(),
            role_name=f"{stack_ctx_enum.github_oidc_single_account_devops.stack_name}-role-{cdk.Aws.REGION}",
            repo_patterns="MacHu-GWU/cdkit-project",
        )

    @cached_property
    def github_oidc_multi_account_devops(self):  # pragma: no cover
        return GitHubOidcMultiAccountDevopsStack(
            scope=self.app,
            **stack_ctx_enum.github_oidc_multi_account_devops.to_stack_kwargs(),
            role_name=f"{stack_ctx_enum.github_oidc_multi_account_devops.stack_name}-role-{cdk.Aws.REGION}",
            repo_patterns="MacHu-GWU/cdkit-project",
            workload_iam_role_arn_list=[
                f"arn:aws:iam::{bsm_enum.dev.aws_account_id}:role/{stack_ctx_enum.github_oidc_multi_account_dev.stack_name}-role-{cdk.Aws.REGION}"
            ],
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
            **stack_ctx_enum.github_oidc_multi_account_dev.to_stack_kwargs(),
            role_name=f"{stack_ctx_enum.github_oidc_multi_account_dev.stack_name}-role-{cdk.Aws.REGION}",
            devops_iam_role_arn=devops_iam_role_arn,
        )


stack_enum = StackEnum(app=cdk.App())
