#!/usr/bin/env python3

from cdkit.tests.stack_enum import stack_enum

_ = stack_enum.github_oidc_provider
_ = stack_enum.github_oidc_single_account_devops
_ = stack_enum.github_oidc_multi_account_devops
_ = stack_enum.github_oidc_multi_account_dev

stack_enum.app.synth()
