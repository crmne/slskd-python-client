# coding: utf-8

"""
    slskd

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest

from slskd.models.distributed_network_options import (  # noqa: E501
    DistributedNetworkOptions,
)


class TestDistributedNetworkOptions(unittest.TestCase):
    """DistributedNetworkOptions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DistributedNetworkOptions
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `DistributedNetworkOptions`
        """
        model = slskd.models.distributed_network_options.DistributedNetworkOptions()  # noqa: E501
        if include_optional :
            return DistributedNetworkOptions(
                disabled = True,
                disable_children = True,
                child_limit = 1,
                logging = True
            )
        else :
            return DistributedNetworkOptions(
        )
        """

    def testDistributedNetworkOptions(self):
        """Test DistributedNetworkOptions"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
