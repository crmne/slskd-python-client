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


class BufferOptions(BaseModel):
    """
    Connection buffer options.
    """

    read: Optional[conint(strict=True, le=2147483647, ge=1024)] = Field(
        None, description="Gets the connection read buffer size, in bytes."
    )
    write: Optional[conint(strict=True, le=2147483647, ge=1024)] = Field(
        None, description="Gets the connection write buffer size, in bytes."
    )
    transfer: Optional[conint(strict=True, le=2147483647, ge=81920)] = Field(
        None, description="Gets the read/write buffer size for transfers, in bytes."
    )
    write_queue: Optional[conint(strict=True, le=5000, ge=5)] = Field(
        None,
        alias="writeQueue",
        description="Gets the size of the queue for double buffered writes.",
    )
    __properties = ["read", "write", "transfer", "writeQueue"]

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
    def from_json(cls, json_str: str) -> BufferOptions:
        """Create an instance of BufferOptions from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BufferOptions:
        """Create an instance of BufferOptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BufferOptions.parse_obj(obj)

        _obj = BufferOptions.parse_obj(
            {
                "read": obj.get("read"),
                "write": obj.get("write"),
                "transfer": obj.get("transfer"),
                "write_queue": obj.get("writeQueue"),
            }
        )
        return _obj
