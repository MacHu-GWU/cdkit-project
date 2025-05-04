# -*- coding: utf-8 -*-

from functools import cached_property

from boto_session_manager import BotoSesManager
import cdk_mate.api as cdk_mate

from .bsm_enum import bsm_enum


class StackCtxEnum: # pragma: no cover

    def create(
        self,
        bsm: BotoSesManager,
        stack_name: str,
    ) -> cdk_mate.StackCtx:
        return cdk_mate.StackCtx(
            construct_id=cdk_mate.to_camel(cdk_mate.to_slug(stack_name)),
            stack_name=cdk_mate.to_slug(stack_name),
            aws_account_id=bsm.aws_account_id,
            aws_region=bsm.aws_region,
            bsm=bsm,
        )

    @cached_property
    def github_oidc_single_account_devops(self):
        return self.create(
            stack_name="github_oidc_single_account_devops",
            bsm=bsm_enum.devops,
        )

stack_ctx_enum = StackCtxEnum()
