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

from slskd.models.connection_options import ConnectionOptions
from slskd.models.diagnostic_level import DiagnosticLevel
from slskd.models.distributed_network_options import DistributedNetworkOptions


class SoulseekOptions(BaseModel):
    """
    Soulseek client options.
    """

    username: Optional[StrictStr] = Field(
        None, description="Gets the username for the Soulseek network."
    )
    password: Optional[StrictStr] = Field(
        None, description="Gets the password for the Soulseek network."
    )
    description: Optional[StrictStr] = Field(
        None, description="Gets the description of the Soulseek user."
    )
    listen_port: Optional[conint(strict=True, le=65535, ge=1024)] = Field(
        None,
        alias="listenPort",
        description="Gets the port on which to listen for incoming connections.",
    )
    diagnostic_level: Optional[DiagnosticLevel] = Field(None, alias="diagnosticLevel")
    distributed_network: Optional[DistributedNetworkOptions] = Field(
        None, alias="distributedNetwork"
    )
    connection: Optional[ConnectionOptions] = None
    __properties = [
        "username",
        "password",
        "description",
        "listenPort",
        "diagnosticLevel",
        "distributedNetwork",
        "connection",
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
    def from_json(cls, json_str: str) -> SoulseekOptions:
        """Create an instance of SoulseekOptions from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of distributed_network
        if self.distributed_network:
            _dict["distributedNetwork"] = self.distributed_network.to_dict()
        # override the default output from pydantic by calling `to_dict()` of connection
        if self.connection:
            _dict["connection"] = self.connection.to_dict()
        # set to None if username (nullable) is None
        # and __fields_set__ contains the field
        if self.username is None and "username" in self.__fields_set__:
            _dict["username"] = None

        # set to None if password (nullable) is None
        # and __fields_set__ contains the field
        if self.password is None and "password" in self.__fields_set__:
            _dict["password"] = None

        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict["description"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SoulseekOptions:
        """Create an instance of SoulseekOptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SoulseekOptions.parse_obj(obj)

        _obj = SoulseekOptions.parse_obj(
            {
                "username": obj.get("username"),
                "password": obj.get("password"),
                "description": obj.get("description"),
                "listen_port": obj.get("listenPort"),
                "diagnostic_level": obj.get("diagnosticLevel"),
                "distributed_network": DistributedNetworkOptions.from_dict(
                    obj.get("distributedNetwork")
                )
                if obj.get("distributedNetwork") is not None
                else None,
                "connection": ConnectionOptions.from_dict(obj.get("connection"))
                if obj.get("connection") is not None
                else None,
            }
        )
        return _obj
