# coding: utf-8

"""
    slskd

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest

from slskd.models.login_request import LoginRequest  # noqa: E501


class TestLoginRequest(unittest.TestCase):
    """LoginRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test LoginRequest
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `LoginRequest`
        """
        model = slskd.models.login_request.LoginRequest()  # noqa: E501
        if include_optional :
            return LoginRequest(
                username = '',
                password = ''
            )
        else :
            return LoginRequest(
        )
        """

    def testLoginRequest(self):
        """Test LoginRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
