# coding: utf-8

"""
    slskd

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest

import slskd
from slskd.api.session_api import SessionApi  # noqa: E501


class TestSessionApi(unittest.TestCase):
    """SessionApi unit test stubs"""

    def setUp(self):
        self.api = slskd.api.session_api.SessionApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_v0_session_enabled_get(self):
        """Test case for api_v0_session_enabled_get

        Checks whether security is enabled.  # noqa: E501
        """

    def test_api_v0_session_get(self):
        """Test case for api_v0_session_get

        Checks whether the provided authentication is valid.  # noqa: E501
        """

    def test_api_v0_session_post(self):
        """Test case for api_v0_session_post

        Logs in.  # noqa: E501
        """


if __name__ == "__main__":
    unittest.main()
