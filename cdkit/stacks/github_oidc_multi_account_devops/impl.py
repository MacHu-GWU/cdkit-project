# -*- coding: utf-8 -*-

from constructs import Construct

from ... import api as cdkit


GitHubOidcMultiAccountDevopsStackParams = cdkit.StackParams
GitHubOidcMultiAccountDevopsParams = cdkit.iam.GitHubOidcMultiAccountDevopsParams


class GitHubOidcMultiAccountDevopsStack(cdkit.BaseStack):
    def __init__(
        self,
        scope: Construct,
        params: GitHubOidcMultiAccountDevopsStackParams,
        github_oidc_multi_account_devops_params: GitHubOidcMultiAccountDevopsParams,
    ):
        super().__init__(scope=scope, params=params)
        self.params = params
        self.github_oidc_multi_account_devops = cdkit.iam.GitHubOidcMultiAccountDevops(
            scope=self,
            params=github_oidc_multi_account_devops_params,
        )
