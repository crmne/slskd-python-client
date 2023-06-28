# coding: utf-8

"""
    slskd

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import re  # noqa: F401

from aenum import Enum


class UserPresence(str, Enum):
    """
    UserPresence
    """

    """
    allowed enum values
    """
    OFFLINE = "Offline"
    AWAY = "Away"
    ONLINE = "Online"

    @classmethod
    def from_json(cls, json_str: str) -> UserPresence:
        """Create an instance of UserPresence from a JSON string"""
        return UserPresence(json.loads(json_str))