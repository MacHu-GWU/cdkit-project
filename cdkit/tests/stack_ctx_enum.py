# -*- coding: utf-8 -*-

import dataclasses
from functools import cached_property

import cdk_mate.api as cdk_mate
import cdkit.api as cdkit

from .bsm_enum import bsm_enum


@dataclasses.dataclass
class StackCtx(cdk_mate.StackCtx):
    def to_stack_params(self) -> cdkit.StackParams:
        return cdkit.StackParams(**self.to_stack_kwargs())


class StackCtxEnum:  # pragma: no cover
    @cached_property
    def github_oidc_provider(self):
        return StackCtx.new(
            stack_name="github_oidc_provider",
            bsm=bsm_enum.devops,
        )

    @cached_property
    def github_oidc_single_account_devops(self):
        return StackCtx.new(
            stack_name="github_oidc_single_account_devops",
            bsm=bsm_enum.devops,
        )

    @cached_property
    def github_oidc_multi_account_devops(self):
        return StackCtx.new(
            stack_name="github_oidc_multi_account_devops",
            bsm=bsm_enum.devops,
        )

    @cached_property
    def github_oidc_multi_account_dev(self):
        return StackCtx.new(
            stack_name="github_oidc_multi_account_dev",
            bsm=bsm_enum.dev,
        )


stack_ctx_enum = StackCtxEnum()
