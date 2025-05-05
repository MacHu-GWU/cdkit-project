# -*- coding: utf-8 -*-

from functools import cached_property

from boto_session_manager import BotoSesManager


class BsmEnum:  # pragma: no cover
    @cached_property
    def devops(self):
        return BotoSesManager(profile_name="esc_app_devops_us_east_1")

    @cached_property
    def dev(self):
        return BotoSesManager(profile_name="esc_app_dev_us_east_1")


bsm_enum = BsmEnum()
