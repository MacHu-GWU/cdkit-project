# -*- coding: utf-8 -*-

from .utils import role_name_to_inline_policy_name
from .service_principal_enum import ServicePrincipalEnum
from .policy_statement import create_get_caller_identity_statement
from .policy_statement import create_assume_role_statement
from .policy_document import create_get_caller_identity_document
from .policy_document import create_assume_role_document
from .github_oidc import create_github_oidc_provider
from .github_oidc import GITHUB_OIDC_PROVIDER_ARN
from .github_oidc import create_github_repo_main_iam_role_assumed_by
from .github_oidc import GitHubOidcProviderParams
from .github_oidc import GitHubOidcProvider
from .github_oidc import GitHubOidcSingleAccountParams
from .github_oidc import GitHubOidcSingleAccount
from .github_oidc import GitHubOidcMultiAccountDevopsParams
from .github_oidc import GitHubOidcMultiAccountDevops
from .github_oidc import GitHubOidcMultiAccountWorkloadParams
from .github_oidc import GitHubOidcMultiAccountWorkload
