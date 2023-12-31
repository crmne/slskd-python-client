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

from pydantic import BaseModel, Field, StrictBool, conint, constr


class ProxyOptions(BaseModel):
    """
    Connection proxy options.
    """

    enabled: Optional[StrictBool] = Field(
        None, description="Gets a value indicating whether the proxy is enabled."
    )
    address: Optional[constr(strict=True, max_length=255, min_length=1)] = Field(
        None, description="Gets the proxy address."
    )
    port: Optional[conint(strict=True, le=65535, ge=1)] = Field(
        None, description="Gets the proxy port."
    )
    username: Optional[constr(strict=True, max_length=255, min_length=1)] = Field(
        None, description="Gets the proxy username, if applicable."
    )
    password: Optional[constr(strict=True, max_length=255, min_length=1)] = Field(
        None, description="Gets the proxy password, if applicable."
    )
    __properties = ["enabled", "address", "port", "username", "password"]

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
    def from_json(cls, json_str: str) -> ProxyOptions:
        """Create an instance of ProxyOptions from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # set to None if address (nullable) is None
        # and __fields_set__ contains the field
        if self.address is None and "address" in self.__fields_set__:
            _dict["address"] = None

        # set to None if port (nullable) is None
        # and __fields_set__ contains the field
        if self.port is None and "port" in self.__fields_set__:
            _dict["port"] = None

        # set to None if username (nullable) is None
        # and __fields_set__ contains the field
        if self.username is None and "username" in self.__fields_set__:
            _dict["username"] = None

        # set to None if password (nullable) is None
        # and __fields_set__ contains the field
        if self.password is None and "password" in self.__fields_set__:
            _dict["password"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ProxyOptions:
        """Create an instance of ProxyOptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ProxyOptions.parse_obj(obj)

        _obj = ProxyOptions.parse_obj(
            {
                "enabled": obj.get("enabled"),
                "address": obj.get("address"),
                "port": obj.get("port"),
                "username": obj.get("username"),
                "password": obj.get("password"),
            }
        )
        return _obj
