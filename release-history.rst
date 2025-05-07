.. _release_history:

Release and Version History
==============================================================================


x.y.z (Backlog)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

**Minor Improvements**

**Bugfixes**

**Miscellaneous**


0.1.3 (2025-05-06)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- Add the following public APIs:
    - Utilities and construct:
        - ``cdkit.api.iam.create_allow_all_services_except_identity_management_statement``
        - ``cdkit.api.iam.create_account_and_org_and_iam_read_only_statement``
        - ``cdkit.api.iam.create_prefixed_iam_management_statement``
        - ``cdkit.api.iam.create_require_permission_boundary_for_role_creation_statement``
        - ``cdkit.api.iam.create_restricted_read_only_statement``
        - ``cdkit.api.iam.create_power_ops_document``
        - ``cdkit.api.iam.create_restricted_read_only_document``

**Minor Improvements**

- Minor improvements to the following construct to make them easier to extend:
    - ``cdkit.api.iam.GitHubOidcSingleAccountParams``
    - ``cdkit.api.iam.GitHubOidcSingleAccount``
    - ``cdkit.api.iam.GitHubOidcMultiAccountDevopsParams``
    - ``cdkit.api.iam.GitHubOidcMultiAccountDevops``
    - ``cdkit.api.iam.GitHubOidcMultiAccountWorkloadParams``
    - ``cdkit.api.iam.GitHubOidcMultiAccountWorkload``


0.1.2 (2025-05-05)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- First release
- Add the following public APIs:
    - Core API:
        - ``cdkit.api.ConstructParams``
        - ``cdkit.api.StackParams``
        - ``cdkit.api.BaseConstruct``
        - ``cdkit.api.BaseStack``
    - Utilities and construct:
        - ``cdkit.api.iam.role_name_to_inline_policy_name``
        - ``cdkit.api.iam.ServicePrincipalEnum``
        - ``cdkit.api.iam.create_get_caller_identity_statement``
        - ``cdkit.api.iam.create_assume_role_statement``
        - ``cdkit.api.iam.create_get_caller_identity_document``
        - ``cdkit.api.iam.create_assume_role_document``
        - ``cdkit.api.iam.create_github_oidc_provider``
        - ``cdkit.api.iam.GITHUB_OIDC_PROVIDER_ARN``
        - ``cdkit.api.iam.create_github_repo_main_iam_role_assumed_by``
        - ``cdkit.api.iam.GitHubOidcProviderParams``
        - ``cdkit.api.iam.GitHubOidcProvider``
        - ``cdkit.api.iam.GitHubOidcSingleAccountParams``
        - ``cdkit.api.iam.GitHubOidcSingleAccount``
        - ``cdkit.api.iam.GitHubOidcMultiAccountDevopsParams``
        - ``cdkit.api.iam.GitHubOidcMultiAccountDevops``
        - ``cdkit.api.iam.GitHubOidcMultiAccountWorkloadParams``
        - ``cdkit.api.iam.GitHubOidcMultiAccountWorkload``
    - Stacks:
        - ``cdkit.api.stacks.github_oidc_provider.GitHubOidcProviderParams``
        - ``cdkit.api.stacks.github_oidc_provider.GitHubOidcProviderStackParams``
        - ``cdkit.api.stacks.github_oidc_provider.GitHubOidcProviderStack``
        - ``cdkit.api.stacks.github_oidc_multi_account_devops.GitHubOidcMultiAccountDevopsParams``
        - ``cdkit.api.stacks.github_oidc_multi_account_devops.GitHubOidcMultiAccountDevopsStackParams``
        - ``cdkit.api.stacks.github_oidc_multi_account_devops.GitHubOidcMultiAccountDevopsStack``
