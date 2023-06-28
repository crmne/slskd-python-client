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
from typing import Dict, Optional

from pydantic import BaseModel, Field, StrictBool, StrictStr

from slskd.models.relay_agent_configuration_options import (
    RelayAgentConfigurationOptions,
)
from slskd.models.relay_controller_configuration_options import (
    RelayControllerConfigurationOptions,
)


class RelayOptions(BaseModel):
    """
    Relay options.
    """

    enabled: Optional[StrictBool] = Field(
        None, description="Gets a value indicating whether the relay is enabled."
    )
    mode: Optional[StrictStr] = Field(None, description="Gets the relay mode.")
    controller: Optional[RelayControllerConfigurationOptions] = None
    agents: Optional[Dict[str, RelayAgentConfigurationOptions]] = Field(
        None, description="Gets the agent configuration."
    )
    __properties = ["enabled", "mode", "controller", "agents"]

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
    def from_json(cls, json_str: str) -> RelayOptions:
        """Create an instance of RelayOptions from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of controller
        if self.controller:
            _dict["controller"] = self.controller.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each value in agents (dict)
        _field_dict = {}
        if self.agents:
            for _key in self.agents:
                if self.agents[_key]:
                    _field_dict[_key] = self.agents[_key].to_dict()
            _dict["agents"] = _field_dict
        # set to None if mode (nullable) is None
        # and __fields_set__ contains the field
        if self.mode is None and "mode" in self.__fields_set__:
            _dict["mode"] = None

        # set to None if agents (nullable) is None
        # and __fields_set__ contains the field
        if self.agents is None and "agents" in self.__fields_set__:
            _dict["agents"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RelayOptions:
        """Create an instance of RelayOptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RelayOptions.parse_obj(obj)

        _obj = RelayOptions.parse_obj(
            {
                "enabled": obj.get("enabled"),
                "mode": obj.get("mode"),
                "controller": RelayControllerConfigurationOptions.from_dict(
                    obj.get("controller")
                )
                if obj.get("controller") is not None
                else None,
                "agents": dict(
                    (_k, RelayAgentConfigurationOptions.from_dict(_v))
                    for _k, _v in obj.get("agents").items()
                )
                if obj.get("agents") is not None
                else None,
            }
        )
        return _obj