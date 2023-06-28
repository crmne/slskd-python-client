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

from pydantic import BaseModel, Field, StrictBool, StrictStr

from slskd.models.ip_end_point import IPEndPoint
from slskd.models.soulseek_client_states import SoulseekClientStates


class ServerState(BaseModel):
    """
    ServerState
    """

    address: Optional[StrictStr] = None
    ip_end_point: Optional[IPEndPoint] = Field(None, alias="ipEndPoint")
    state: Optional[SoulseekClientStates] = None
    username: Optional[StrictStr] = None
    is_connected: Optional[StrictBool] = Field(None, alias="isConnected")
    is_logged_in: Optional[StrictBool] = Field(None, alias="isLoggedIn")
    is_transitioning: Optional[StrictBool] = Field(None, alias="isTransitioning")
    __properties = [
        "address",
        "ipEndPoint",
        "state",
        "username",
        "isConnected",
        "isLoggedIn",
        "isTransitioning",
    ]

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
    def from_json(cls, json_str: str) -> ServerState:
        """Create an instance of ServerState from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(
            by_alias=True,
            exclude={
                "is_connected",
                "is_logged_in",
                "is_transitioning",
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of ip_end_point
        if self.ip_end_point:
            _dict["ipEndPoint"] = self.ip_end_point.to_dict()
        # set to None if address (nullable) is None
        # and __fields_set__ contains the field
        if self.address is None and "address" in self.__fields_set__:
            _dict["address"] = None

        # set to None if username (nullable) is None
        # and __fields_set__ contains the field
        if self.username is None and "username" in self.__fields_set__:
            _dict["username"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ServerState:
        """Create an instance of ServerState from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ServerState.parse_obj(obj)

        _obj = ServerState.parse_obj(
            {
                "address": obj.get("address"),
                "ip_end_point": IPEndPoint.from_dict(obj.get("ipEndPoint"))
                if obj.get("ipEndPoint") is not None
                else None,
                "state": obj.get("state"),
                "username": obj.get("username"),
                "is_connected": obj.get("isConnected"),
                "is_logged_in": obj.get("isLoggedIn"),
                "is_transitioning": obj.get("isTransitioning"),
            }
        )
        return _obj