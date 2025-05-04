# -*- coding: utf-8 -*-

if __name__ == "__main__":
    from cdkit.tests import run_cov_test

    run_cov_test(
        __file__,
        "cdkit",
        is_folder=True,
        preview=False,
    )
