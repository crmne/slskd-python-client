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
from slskd.api.public_chat_api import PublicChatApi  # noqa: E501


class TestPublicChatApi(unittest.TestCase):
    """PublicChatApi unit test stubs"""

    def setUp(self):
        self.api = slskd.api.public_chat_api.PublicChatApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_v0_publicchat_delete(self):
        """Test case for api_v0_publicchat_delete

        Stops public chat.  # noqa: E501
        """

    def test_api_v0_publicchat_post(self):
        """Test case for api_v0_publicchat_post

        Starts public chat.  # noqa: E501
        """


if __name__ == "__main__":
    unittest.main()
