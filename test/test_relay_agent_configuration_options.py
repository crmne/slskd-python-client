# coding: utf-8

"""
    slskd

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest

from slskd.models.relay_agent_configuration_options import (  # noqa: E501
    RelayAgentConfigurationOptions,
)


class TestRelayAgentConfigurationOptions(unittest.TestCase):
    """RelayAgentConfigurationOptions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RelayAgentConfigurationOptions
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `RelayAgentConfigurationOptions`
        """
        model = slskd.models.relay_agent_configuration_options.RelayAgentConfigurationOptions()  # noqa: E501
        if include_optional :
            return RelayAgentConfigurationOptions(
                instance_name = '0',
                secret = '0123456789101112131415',
                cidr = ''
            )
        else :
            return RelayAgentConfigurationOptions(
        )
        """

    def testRelayAgentConfigurationOptions(self):
        """Test RelayAgentConfigurationOptions"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
