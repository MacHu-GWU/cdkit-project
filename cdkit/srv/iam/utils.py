# -*- coding: utf-8 -*-


def role_name_to_inline_policy_name(role_name: str) -> str:
    """
    Convert a role name to an inline policy name.
    """
    return f"{role_name}-inlpol"
