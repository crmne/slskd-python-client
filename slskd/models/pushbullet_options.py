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

from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conint


class PushbulletOptions(BaseModel):
    """
    Pushbullet options.
    """

    enabled: Optional[StrictBool] = Field(
        None,
        description="Gets a value indicating whether the Pushbullet integration is enabled.",
    )
    access_token: Optional[StrictStr] = Field(
        None, alias="accessToken", description="Gets the Pushbullet API access token."
    )
    notification_prefix: Optional[StrictStr] = Field(
        None,
        alias="notificationPrefix",
        description="Gets the prefix for Pushbullet notification titles.",
    )
    notify_on_private_message: Optional[StrictBool] = Field(
        None,
        alias="notifyOnPrivateMessage",
        description="Gets a value indicating whether a Pushbullet notification should be sent when a private message is received.",
    )
    notify_on_room_mention: Optional[StrictBool] = Field(
        None,
        alias="notifyOnRoomMention",
        description="Gets a value indicating whether a Pushbullet notification should be sent when the currently logged  in user's username is mentioned in a room.",
    )
    retry_attempts: Optional[conint(strict=True, le=5, ge=0)] = Field(
        None,
        alias="retryAttempts",
        description="Gets the number of times failing Pushbullet notifications will be retried.",
    )
    cooldown_time: Optional[StrictInt] = Field(
        None,
        alias="cooldownTime",
        description="Gets the cooldown time for Pushbullet notifications, in milliseconds.",
    )
    __properties = [
        "enabled",
        "accessToken",
        "notificationPrefix",
        "notifyOnPrivateMessage",
        "notifyOnRoomMention",
        "retryAttempts",
        "cooldownTime",
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
    def from_json(cls, json_str: str) -> PushbulletOptions:
        """Create an instance of PushbulletOptions from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # set to None if access_token (nullable) is None
        # and __fields_set__ contains the field
        if self.access_token is None and "access_token" in self.__fields_set__:
            _dict["accessToken"] = None

        # set to None if notification_prefix (nullable) is None
        # and __fields_set__ contains the field
        if (
            self.notification_prefix is None
            and "notification_prefix" in self.__fields_set__
        ):
            _dict["notificationPrefix"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PushbulletOptions:
        """Create an instance of PushbulletOptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PushbulletOptions.parse_obj(obj)

        _obj = PushbulletOptions.parse_obj(
            {
                "enabled": obj.get("enabled"),
                "access_token": obj.get("accessToken"),
                "notification_prefix": obj.get("notificationPrefix"),
                "notify_on_private_message": obj.get("notifyOnPrivateMessage"),
                "notify_on_room_mention": obj.get("notifyOnRoomMention"),
                "retry_attempts": obj.get("retryAttempts"),
                "cooldown_time": obj.get("cooldownTime"),
            }
        )
        return _obj
