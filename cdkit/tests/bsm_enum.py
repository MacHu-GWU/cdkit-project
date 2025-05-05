# -*- coding: utf-8 -*-

from functools import cached_property

from boto_session_manager import BotoSesManager

from .runtime import IS_CI


class BsmEnum:  # pragma: no cover
    def _get_bsm(self, profile: str) -> BotoSesManager:
        if IS_CI:
            return BotoSesManager(region_name="us-east-1")
        else:
            return BotoSesManager(profile_name=profile)

    @cached_property
    def devops(self):
        return self._get_bsm("esc_app_devops_us_east_1")

    @cached_property
    def dev(self):
        return self._get_bsm("esc_app_dev_us_east_1")


bsm_enum = BsmEnum()
