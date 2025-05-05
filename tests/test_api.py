# -*- coding: utf-8 -*-

from cdkit import api


def test():
    # fmt: off
    _ = api
    _ = api.T_KWARGS
    _ = api.T_OPT_KWARGS
    _ = api.ParamError
    _ = api.REQ
    _ = api.OPT
    _ = api.check_required
    _ = api.remove_optional
    _ = api.prepare_kwargs
    _ = api.BaseModel
    _ = api.BaseFrozenModel
    _ = api.ConstructParams
    _ = api.StackParams
    _ = api.BaseConstruct
    _ = api.BaseStack

    # ===== AWS Services =====
    _ = api.iam
    _ = api.iam.role_name_to_inline_policy_name
    _ = api.iam.ServicePrincipalEnum
    _ = api.iam.create_get_caller_identity_statement
    _ = api.iam.create_assume_role_statement
    _ = api.iam.create_get_caller_identity_document
    _ = api.iam.create_assume_role_document
    _ = api.iam.create_github_oidc_provider
    _ = api.iam.GITHUB_OIDC_PROVIDER_ARN
    _ = api.iam.create_github_repo_main_iam_role_assumed_by
    _ = api.iam.GitHubOidcProviderParams
    _ = api.iam.GitHubOidcProvider
    _ = api.iam.GitHubOidcSingleAccountParams
    _ = api.iam.GitHubOidcSingleAccount
    _ = api.iam.GitHubOidcMultiAccountDevopsParams
    _ = api.iam.GitHubOidcMultiAccountDevops
    _ = api.iam.GitHubOidcMultiAccountWorkloadParams
    _ = api.iam.GitHubOidcMultiAccountWorkload

    # ===== Stack =====
    _ = api.stacks

    _ = api.stacks.github_oidc_provider.GitHubOidcProviderParams
    _ = api.stacks.github_oidc_provider.GitHubOidcProviderStackParams
    _ = api.stacks.github_oidc_provider.GitHubOidcProviderStack

    _ = api.stacks.github_oidc_multi_account_devops.GitHubOidcMultiAccountDevopsParams
    _ = api.stacks.github_oidc_multi_account_devops.GitHubOidcMultiAccountDevopsStackParams
    _ = api.stacks.github_oidc_multi_account_devops.GitHubOidcMultiAccountDevopsStack
    # fmt: on


if __name__ == "__main__":
    from cdkit.tests import run_cov_test

    run_cov_test(
        __file__,
        "cdkit.api",
        preview=False,
    )
