# coding: utf-8

"""
    slskd

    A python client for slskd  # noqa: E501

    The version of the OpenAPI document: 0.17.8.0
    Contact: carmine@paolino.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations

import json
import pprint
import re  # noqa: F401
from typing import Optional

from pydantic import BaseModel, Field, StrictStr, constr


class ApiKeyOptions(BaseModel):
    """
    API key options.
    """

    key: Optional[constr(strict=True, max_length=255, min_length=16)] = Field(
        None, description="Gets the API key value."
    )
    role: Optional[StrictStr] = Field(None, description="Gets the role for the key.")
    cidr: Optional[StrictStr] = Field(
        None,
        description="Gets the comma separated list of CIDRs that are authorized to use the key.",
    )
    __properties = ["key", "role", "cidr"]

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
    def from_json(cls, json_str: str) -> ApiKeyOptions:
        """Create an instance of ApiKeyOptions from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # set to None if key (nullable) is None
        # and __fields_set__ contains the field
        if self.key is None and "key" in self.__fields_set__:
            _dict["key"] = None

        # set to None if role (nullable) is None
        # and __fields_set__ contains the field
        if self.role is None and "role" in self.__fields_set__:
            _dict["role"] = None

        # set to None if cidr (nullable) is None
        # and __fields_set__ contains the field
        if self.cidr is None and "cidr" in self.__fields_set__:
            _dict["cidr"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiKeyOptions:
        """Create an instance of ApiKeyOptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiKeyOptions.parse_obj(obj)

        _obj = ApiKeyOptions.parse_obj(
            {"key": obj.get("key"), "role": obj.get("role"), "cidr": obj.get("cidr")}
        )
        return _obj
