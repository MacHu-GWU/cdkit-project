# -*- coding: utf-8 -*-

import moto

from .runtime import IS_CI


class BaseMockAwsTest:
    mock_aws: "moto.mock_aws" = None

    @classmethod
    def setup_class(cls):
        if IS_CI:
            cls.mock_aws = moto.mock_aws()
            cls.mock_aws.start()

        cls.setup_class_post_hook()

    @classmethod
    def setup_class_post_hook(cls):
        pass

    @classmethod
    def teardown_class(cls):
        if IS_CI:
            cls.mock_aws.stop()
