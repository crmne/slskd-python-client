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
from slskd.api.searches_api import SearchesApi  # noqa: E501


class TestSearchesApi(unittest.TestCase):
    """SearchesApi unit test stubs"""

    def setUp(self):
        self.api = slskd.api.searches_api.SearchesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_v0_searches_get(self):
        """Test case for api_v0_searches_get

        Gets the list of active and completed searches.  # noqa: E501
        """

    def test_api_v0_searches_id_delete(self):
        """Test case for api_v0_searches_id_delete

        Deletes the search corresponding to the specified id.  # noqa: E501
        """

    def test_api_v0_searches_id_get(self):
        """Test case for api_v0_searches_id_get

        Gets the state of the search corresponding to the specified id.  # noqa: E501
        """

    def test_api_v0_searches_id_put(self):
        """Test case for api_v0_searches_id_put

        Stops the search corresponding to the specified id.  # noqa: E501
        """

    def test_api_v0_searches_id_responses_get(self):
        """Test case for api_v0_searches_id_responses_get

        Gets the state of the search corresponding to the specified id.  # noqa: E501
        """

    def test_api_v0_searches_post(self):
        """Test case for api_v0_searches_post

        Performs a search for the specified request.  # noqa: E501
        """


if __name__ == "__main__":
    unittest.main()
