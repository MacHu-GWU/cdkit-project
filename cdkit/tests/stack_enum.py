# -*- coding: utf-8 -*-

import dataclasses
from functools import cached_property

import aws_cdk as cdk

from .stack_ctx_enum import stack_ctx_enum

from .stacks.github_oidc import GitHubOidcSingleAccountStack


@dataclasses.dataclass
class StackEnum:
    app: cdk.App = dataclasses.field()

    @cached_property
    def github_oidc_single_account_devops(self):  # pragma: no cover
        return GitHubOidcSingleAccountStack(
            scope=self.app,
            **stack_ctx_enum.github_oidc_single_account_devops.to_stack_kwargs(),
            role_name=f"{stack_ctx_enum.github_oidc_single_account_devops.stack_name}-devops-role-{cdk.Aws.REGION}",
            repo_patterns="MacHu-GWU/cdkit-project",
        )


stack_enum = StackEnum(app=cdk.App())
