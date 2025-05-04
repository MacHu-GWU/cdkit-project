# -*- coding: utf-8 -*-

from cdkit import api
from cdkit.tests.stack_enum import stack_enum


class TestStackEnum:
    @classmethod
    def setup_class(cls):
        cls.stack_enum = stack_enum

    def test_synth(self):
        _ = stack_enum.github_oidc_single_account_devops

        stack_enum.app.synth()


if __name__ == "__main__":
    from cdkit.tests import run_cov_test

    run_cov_test(
        __file__,
        "cdkit",
        preview=False,
    )
