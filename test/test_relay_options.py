# coding: utf-8

"""
    slskd

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest

from slskd.models.relay_options import RelayOptions  # noqa: E501


class TestRelayOptions(unittest.TestCase):
    """RelayOptions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RelayOptions
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `RelayOptions`
        """
        model = slskd.models.relay_options.RelayOptions()  # noqa: E501
        if include_optional :
            return RelayOptions(
                enabled = True,
                mode = '',
                controller = slskd.models.relay_controller_configuration_options.RelayControllerConfigurationOptions(
                    address = '',
                    ignore_certificate_errors = True,
                    api_key = '0123456789101112131415',
                    secret = '0123456789101112131415',
                    downloads = True, ),
                agents = {
                    'key' : slskd.models.relay_agent_configuration_options.RelayAgentConfigurationOptions(
                        instance_name = '0',
                        secret = '0123456789101112131415',
                        cidr = '', )
                    }
            )
        else :
            return RelayOptions(
        )
        """

    def testRelayOptions(self):
        """Test RelayOptions"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()