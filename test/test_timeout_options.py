# coding: utf-8

"""
    slskd

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest

from slskd.models.timeout_options import TimeoutOptions  # noqa: E501


class TestTimeoutOptions(unittest.TestCase):
    """TimeoutOptions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TimeoutOptions
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `TimeoutOptions`
        """
        model = slskd.models.timeout_options.TimeoutOptions()  # noqa: E501
        if include_optional :
            return TimeoutOptions(
                connect = 1000,
                inactivity = 1000
            )
        else :
            return TimeoutOptions(
        )
        """

    def testTimeoutOptions(self):
        """Test TimeoutOptions"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()