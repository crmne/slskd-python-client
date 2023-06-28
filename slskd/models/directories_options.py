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

from pydantic import BaseModel, Field, StrictStr


class DirectoriesOptions(BaseModel):
    """
    Directory options.
    """

    incomplete: Optional[StrictStr] = Field(
        None, description="Gets the path where incomplete downloads are saved."
    )
    downloads: Optional[StrictStr] = Field(
        None, description="Gets the path where downloaded files are saved."
    )
    __properties = ["incomplete", "downloads"]

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
    def from_json(cls, json_str: str) -> DirectoriesOptions:
        """Create an instance of DirectoriesOptions from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # set to None if incomplete (nullable) is None
        # and __fields_set__ contains the field
        if self.incomplete is None and "incomplete" in self.__fields_set__:
            _dict["incomplete"] = None

        # set to None if downloads (nullable) is None
        # and __fields_set__ contains the field
        if self.downloads is None and "downloads" in self.__fields_set__:
            _dict["downloads"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DirectoriesOptions:
        """Create an instance of DirectoriesOptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DirectoriesOptions.parse_obj(obj)

        _obj = DirectoriesOptions.parse_obj(
            {"incomplete": obj.get("incomplete"), "downloads": obj.get("downloads")}
        )
        return _obj
