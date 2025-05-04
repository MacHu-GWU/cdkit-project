# -*- coding: utf-8 -*-

import aws_cdk as cdk
from constructs import Construct

import cdkit.api as cdkit


class GitHubOidcSingleAccountStack(cdkit.cstr.GitHubOidcSingleAccountStack):
    def create_github_repo_main_iam_role_inline_policy_document(self):
        return cdkit.srv.iam.create_get_caller_identity_document()
