# -*- coding: utf-8 -*-

from constructs import Construct

from ... import api as cdkit


GitHubOidcProviderStackParams = cdkit.StackParams
GitHubOidcProviderParams = cdkit.iam.GitHubOidcProviderParams


class GitHubOidcProviderStack(cdkit.BaseStack):
    def __init__(
        self,
        scope: Construct,
        params: GitHubOidcProviderStackParams,
        github_oidc_provider_params: GitHubOidcProviderParams,
    ):
        super().__init__(scope=scope, params=params)
        self.params = params
        self.github_oidc_provider = cdkit.iam.GitHubOidcProvider(
            scope=self,
            params=github_oidc_provider_params,
        )
