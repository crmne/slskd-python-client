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

from pydantic import BaseModel, Field, StrictStr, conint


class ShareCacheOptions(BaseModel):
    """
    Share caching options.
    """

    storage_mode: Optional[StrictStr] = Field(
        None,
        alias="storageMode",
        description="Gets the type of storage to use for the share cache.",
    )
    workers: Optional[conint(strict=True, le=128, ge=1)] = Field(
        None, description="Gets the number of workers to use while scanning shares."
    )
    __properties = ["storageMode", "workers"]

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
    def from_json(cls, json_str: str) -> ShareCacheOptions:
        """Create an instance of ShareCacheOptions from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # set to None if storage_mode (nullable) is None
        # and __fields_set__ contains the field
        if self.storage_mode is None and "storage_mode" in self.__fields_set__:
            _dict["storageMode"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ShareCacheOptions:
        """Create an instance of ShareCacheOptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ShareCacheOptions.parse_obj(obj)

        _obj = ShareCacheOptions.parse_obj(
            {"storage_mode": obj.get("storageMode"), "workers": obj.get("workers")}
        )
        return _obj
