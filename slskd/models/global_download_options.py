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

from pydantic import BaseModel, Field, conint


class GlobalDownloadOptions(BaseModel):
    """
    Gets global download options.
    """

    slots: Optional[conint(strict=True, le=2147483647, ge=1)] = Field(
        None, description="Gets the limit for the total number of download slots."
    )
    speed_limit: Optional[conint(strict=True, le=2147483647, ge=1)] = Field(
        None, alias="speedLimit", description="Gets the total download speed limit."
    )
    __properties = ["slots", "speedLimit"]

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
    def from_json(cls, json_str: str) -> GlobalDownloadOptions:
        """Create an instance of GlobalDownloadOptions from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GlobalDownloadOptions:
        """Create an instance of GlobalDownloadOptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GlobalDownloadOptions.parse_obj(obj)

        _obj = GlobalDownloadOptions.parse_obj(
            {"slots": obj.get("slots"), "speed_limit": obj.get("speedLimit")}
        )
        return _obj
