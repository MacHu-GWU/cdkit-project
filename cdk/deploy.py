# -*- coding: utf-8 -*-

import cdk_mate.api as cdk_mate
from cdkit.tests.stack_ctx_enum import stack_ctx_enum

# --- Group stack by aws account
# --- Creation order
create_devops_stack_ctx_list = [
    stack_ctx_enum.github_oidc_provider,
    stack_ctx_enum.github_oidc_single_account_devops,
    stack_ctx_enum.github_oidc_multi_account_devops,
]

create_dev_stack_ctx_list = [
    stack_ctx_enum.github_oidc_multi_account_dev,
]

# --- Deletion order
delete_devops_stack_ctx_list = [
    stack_ctx_enum.github_oidc_multi_account_devops,
    stack_ctx_enum.github_oidc_single_account_devops,
    stack_ctx_enum.github_oidc_provider,
]

delete_dev_stack_ctx_list = [
    stack_ctx_enum.github_oidc_multi_account_dev,
]

# --- 📦 cdk synth
# cdk_mate.cli.Synth().run(dir_cdk=__file__)

# --- 🔍 cdk diff
# cdk_mate.cdk_diff_many(create_devops_stack_ctx_list, dir_cdk=__file__)
# cdk_mate.cdk_diff_many(create_dev_stack_ctx_list, dir_cdk=__file__)

# --- 🚀 cdk deploy
# cdk_mate.cdk_deploy_many(create_devops_stack_ctx_list, dir_cdk=__file__)
# cdk_mate.cdk_deploy_many(create_dev_stack_ctx_list, dir_cdk=__file__)

# --- 💥 cdk destroy
# cdk_mate.cdk_destroy_many(delete_dev_stack_ctx_list, dir_cdk=__file__)
# cdk_mate.cdk_destroy_many(delete_devops_stack_ctx_list, dir_cdk=__file__)
