# -*- coding: utf-8 -*-

from cdkit.tests.mock_aws import BaseMockAwsTest


class TestStackEnum(BaseMockAwsTest):

    def test_synth(self):
        from cdkit.tests.stack_enum import stack_enum

        _ = stack_enum.github_oidc_provider
        _ = stack_enum.github_oidc_single_account_devops
        _ = stack_enum.github_oidc_multi_account_devops
        _ = stack_enum.github_oidc_multi_account_dev

        stack_enum.app.synth()


if __name__ == "__main__":
    from cdkit.tests import run_cov_test

    run_cov_test(
        __file__,
        "cdkit",
        preview=False,
    )
