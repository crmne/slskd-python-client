# coding: utf-8

"""
    slskd

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest

from slskd.models.file_attribute import FileAttribute  # noqa: E501


class TestFileAttribute(unittest.TestCase):
    """FileAttribute unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test FileAttribute
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `FileAttribute`
        """
        model = slskd.models.file_attribute.FileAttribute()  # noqa: E501
        if include_optional :
            return FileAttribute(
                type = 'BitRate',
                value = 56
            )
        else :
            return FileAttribute(
        )
        """

    def testFileAttribute(self):
        """Test FileAttribute"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
