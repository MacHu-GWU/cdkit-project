# -*- coding: utf-8 -*-

from cdkit.tests.stack_ctx_enum import stack_ctx_enum

# --- 📦 cdk synth
# stack_ctx_enum.github_oidc_provider.cdk_synth(dir_cdk=__file__)
# stack_ctx_enum.github_oidc_single_account_devops.cdk_synth(dir_cdk=__file__)
# stack_ctx_enum.github_oidc_multi_account_devops.cdk_synth(dir_cdk=__file__)
# stack_ctx_enum.github_oidc_multi_account_dev.cdk_synth(dir_cdk=__file__)

# --- 🔍 cdk diff
# stack_ctx_enum.github_oidc_provider.cdk_diff(dir_cdk=__file__)
# stack_ctx_enum.github_oidc_single_account_devops.cdk_diff(dir_cdk=__file__)
# stack_ctx_enum.github_oidc_multi_account_devops.cdk_diff(dir_cdk=__file__)
# stack_ctx_enum.github_oidc_multi_account_dev.cdk_diff(dir_cdk=__file__)

# --- 🚀 cdk deploy
# stack_ctx_enum.github_oidc_provider.cdk_deploy(dir_cdk=__file__)
# stack_ctx_enum.github_oidc_single_account_devops.cdk_deploy(dir_cdk=__file__, prompt=False)
# stack_ctx_enum.github_oidc_multi_account_devops.cdk_deploy(dir_cdk=__file__)
# stack_ctx_enum.github_oidc_multi_account_dev.cdk_deploy(dir_cdk=__file__)

# --- 💥 cdk destroy
stack_ctx_enum.github_oidc_provider.cdk_destroy(dir_cdk=__file__)
stack_ctx_enum.github_oidc_single_account_devops.cdk_destroy(dir_cdk=__file__, prompt=False)
stack_ctx_enum.github_oidc_multi_account_devops.cdk_destroy(dir_cdk=__file__)
stack_ctx_enum.github_oidc_multi_account_devops.cdk_deploy(dir_cdk=__file__)
