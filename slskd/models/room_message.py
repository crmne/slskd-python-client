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
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, StrictStr

from slskd.models.message_direction import MessageDirection


class RoomMessage(BaseModel):
    """
    A message sent to a room.
    """

    timestamp: Optional[datetime] = Field(
        None, description="The timestamp of the message."
    )
    username: Optional[StrictStr] = Field(
        None, description="The username of the user who sent the message."
    )
    message: Optional[StrictStr] = Field(None, description="The message.")
    room_name: Optional[StrictStr] = Field(
        None, alias="roomName", description="The room to which the message pertains."
    )
    direction: Optional[MessageDirection] = None
    __properties = ["timestamp", "username", "message", "roomName", "direction"]

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
    def from_json(cls, json_str: str) -> RoomMessage:
        """Create an instance of RoomMessage from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # set to None if username (nullable) is None
        # and __fields_set__ contains the field
        if self.username is None and "username" in self.__fields_set__:
            _dict["username"] = None

        # set to None if message (nullable) is None
        # and __fields_set__ contains the field
        if self.message is None and "message" in self.__fields_set__:
            _dict["message"] = None

        # set to None if room_name (nullable) is None
        # and __fields_set__ contains the field
        if self.room_name is None and "room_name" in self.__fields_set__:
            _dict["roomName"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RoomMessage:
        """Create an instance of RoomMessage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RoomMessage.parse_obj(obj)

        _obj = RoomMessage.parse_obj(
            {
                "timestamp": obj.get("timestamp"),
                "username": obj.get("username"),
                "message": obj.get("message"),
                "room_name": obj.get("roomName"),
                "direction": obj.get("direction"),
            }
        )
        return _obj