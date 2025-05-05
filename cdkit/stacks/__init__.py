# -*- coding: utf-8 -*-

"""
Pre-built AWS CDK stacks for vertical use cases.

This package provides reusable AWS CDK stack implementations for common cloud
infrastructure patterns and architectures. Each submodule encapsulates a
complete vertical solution that can be deployed with minimal configuration.

**Package Structure**:

Each subdirectory represents a specific vertical use case with:

- `impl.py`: Implementation details and internal logic
- `api.py`: Public API and exported classes
- Supporting modules specific to that vertical

**Available Verticals Example**:

- github_oidc_provider: GitHub OpenID Connect provider for AWS authentication
- github_oidc_multi_account_devops: Multi-account GitHub OIDC setup for DevOps workflows

Usage Examples:

    >>> import cdkit.api as cdkit
    >>> # Access vertical use case modules
    >>> cdkit.stacks.github_oidc_provider
    >>> cdkit.stacks.github_oidc_multi_account_devops
    >>> # Access components in each vertical use case module
    >>> cdkit.stacks.github_oidc_provider.GitHubOidcProviderParams
    >>> cdkit.stacks.github_oidc_provider.GitHubOidcProviderStackParams
    >>> cdkit.stacks.github_oidc_provider.GitHubOidcProviderStack
"""