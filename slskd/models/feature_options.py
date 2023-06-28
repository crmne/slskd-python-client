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

from pydantic import BaseModel, Field, StrictBool


class FeatureOptions(BaseModel):
    """
    Feature options.
    """

    swagger: Optional[StrictBool] = Field(
        None,
        description="Gets a value indicating whether swagger documentation and UI should be enabled.",
    )
    __properties = ["swagger"]

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
    def from_json(cls, json_str: str) -> FeatureOptions:
        """Create an instance of FeatureOptions from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> FeatureOptions:
        """Create an instance of FeatureOptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FeatureOptions.parse_obj(obj)

        _obj = FeatureOptions.parse_obj({"swagger": obj.get("swagger")})
        return _obj
