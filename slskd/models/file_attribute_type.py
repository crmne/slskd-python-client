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


class FileAttributeType(str, Enum):
    """
    FileAttributeType
    """

    """
    allowed enum values
    """
    BITRATE = "BitRate"
    LENGTH = "Length"
    VARIABLEBITRATE = "VariableBitRate"
    SAMPLERATE = "SampleRate"
    BITDEPTH = "BitDepth"

    @classmethod
    def from_json(cls, json_str: str) -> FileAttributeType:
        """Create an instance of FileAttributeType from a JSON string"""
        return FileAttributeType(json.loads(json_str))
