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
from slskd.api.server_api import ServerApi  # noqa: E501


class TestServerApi(unittest.TestCase):
    """ServerApi unit test stubs"""

    def setUp(self):
        self.api = slskd.api.server_api.ServerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_v0_server_delete(self):
        """Test case for api_v0_server_delete

        Disconnects the client.  # noqa: E501
        """

    def test_api_v0_server_get(self):
        """Test case for api_v0_server_get

        Retrieves the current state of the server.  # noqa: E501
        """

    def test_api_v0_server_put(self):
        """Test case for api_v0_server_put

        Connects the client.  # noqa: E501
        """


if __name__ == "__main__":
    unittest.main()