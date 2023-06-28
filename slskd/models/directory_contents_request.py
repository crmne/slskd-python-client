# coding: utf-8

"""
    slskd

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations

import json
import pprint
import re  # noqa: F401
from typing import Optional

from pydantic import BaseModel, StrictStr


class DirectoryContentsRequest(BaseModel):
    """
    DirectoryContentsRequest
    """

    directory: Optional[StrictStr] = None
    __properties = ["directory"]

    class Config:
        """Pydantic configuration"""

        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> DirectoryContentsRequest:
        """Create an instance of DirectoryContentsRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # set to None if directory (nullable) is None
        # and __fields_set__ contains the field
        if self.directory is None and "directory" in self.__fields_set__:
            _dict["directory"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DirectoryContentsRequest:
        """Create an instance of DirectoryContentsRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DirectoryContentsRequest.parse_obj(obj)

        _obj = DirectoryContentsRequest.parse_obj({"directory": obj.get("directory")})
        return _obj