# coding: utf-8

"""
    slskd

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest

from slskd.models.flags_options import FlagsOptions  # noqa: E501


class TestFlagsOptions(unittest.TestCase):
    """FlagsOptions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test FlagsOptions
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `FlagsOptions`
        """
        model = slskd.models.flags_options.FlagsOptions()  # noqa: E501
        if include_optional :
            return FlagsOptions(
                no_logo = True,
                no_start = True,
                no_connect = True,
                no_share_scan = True,
                force_share_scan = True,
                no_version_check = True,
                log_sql = True,
                experimental = True,
                volatile = True,
                case_sensitive_reg_ex = True
            )
        else :
            return FlagsOptions(
        )
        """

    def testFlagsOptions(self):
        """Test FlagsOptions"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
