# coding: utf-8

"""
    slskd

    A python client for slskd  # noqa: E501

    The version of the OpenAPI document: 0.17.8.0
    Contact: carmine@paolino.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import re  # noqa: F401

from aenum import Enum


class DiagnosticLevel(str, Enum):
    """
    DiagnosticLevel
    """

    """
    allowed enum values
    """
    NONE = "None"
    WARNING = "Warning"
    INFO = "Info"
    DEBUG = "Debug"

    @classmethod
    def from_json(cls, json_str: str) -> DiagnosticLevel:
        """Create an instance of DiagnosticLevel from a JSON string"""
        return DiagnosticLevel(json.loads(json_str))
