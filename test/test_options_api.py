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
from slskd.api.options_api import OptionsApi  # noqa: E501


class TestOptionsApi(unittest.TestCase):
    """OptionsApi unit test stubs"""

    def setUp(self):
        self.api = slskd.api.options_api.OptionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_v0_options_debug_get(self):
        """Test case for api_v0_options_debug_get

        Gets the debug view of the current application options.  # noqa: E501
        """

    def test_api_v0_options_get(self):
        """Test case for api_v0_options_get

        Gets the current application options.  # noqa: E501
        """

    def test_api_v0_options_startup_get(self):
        """Test case for api_v0_options_startup_get

        Gets the application options provided at startup.  # noqa: E501
        """

    def test_api_v0_options_yaml_get(self):
        """Test case for api_v0_options_yaml_get"""

    def test_api_v0_options_yaml_location_get(self):
        """Test case for api_v0_options_yaml_location_get"""

    def test_api_v0_options_yaml_post(self):
        """Test case for api_v0_options_yaml_post"""

    def test_api_v0_options_yaml_validate_post(self):
        """Test case for api_v0_options_yaml_validate_post"""


if __name__ == "__main__":
    unittest.main()
