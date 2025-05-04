# -*- coding: utf-8 -*-

from cdkit import api


def test():
    _ = api


if __name__ == "__main__":
    from cdkit.tests import run_cov_test

    run_cov_test(
        __file__,
        "cdkit.api",
        preview=False,
    )
