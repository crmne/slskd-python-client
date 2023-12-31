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
from datetime import datetime
from typing import Optional, Union

from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr

from slskd.models.ip_end_point import IPEndPoint
from slskd.models.transfer_direction import TransferDirection
from slskd.models.transfer_states import TransferStates


class Transfer(BaseModel):
    """
    A single file transfer.
    """

    average_speed: Optional[Union[StrictFloat, StrictInt]] = Field(
        None,
        alias="averageSpeed",
        description="Gets the current average transfer speed.",
    )
    bytes_remaining: Optional[StrictInt] = Field(
        None,
        alias="bytesRemaining",
        description="Gets the number of remaining bytes to be transferred.",
    )
    bytes_transferred: Optional[StrictInt] = Field(
        None,
        alias="bytesTransferred",
        description="Gets the total number of bytes transferred.",
    )
    direction: Optional[TransferDirection] = None
    elapsed_time: Optional[Union[StrictFloat, StrictInt]] = Field(
        None,
        alias="elapsedTime",
        description="Gets the current duration of the transfer, if it has been started.",
    )
    end_time: Optional[datetime] = Field(
        None,
        alias="endTime",
        description="Gets the UTC time at which the transfer transitioned into the Soulseek.TransferStates.Completed state.",
    )
    filename: Optional[StrictStr] = Field(
        None, description="Gets the filename of the file to be transferred."
    )
    id: Optional[StrictStr] = Field(None, description="Gets the transfer id.")
    ip_end_point: Optional[IPEndPoint] = Field(None, alias="ipEndPoint")
    percent_complete: Optional[Union[StrictFloat, StrictInt]] = Field(
        None,
        alias="percentComplete",
        description="Gets the current progress in percent.",
    )
    place_in_queue: Optional[StrictInt] = Field(
        None,
        alias="placeInQueue",
        description="Gets the current place in queue, if it has been fetched.",
    )
    remaining_time: Optional[Union[StrictFloat, StrictInt]] = Field(
        None,
        alias="remainingTime",
        description="Gets the projected remaining duration of the transfer.",
    )
    remote_token: Optional[StrictInt] = Field(
        None,
        alias="remoteToken",
        description="Gets the remote unique token for the transfer.",
    )
    size: Optional[StrictInt] = Field(
        None, description="Gets the size of the file to be transferred, in bytes."
    )
    start_offset: Optional[StrictInt] = Field(
        None,
        alias="startOffset",
        description="Gets the starting offset of the transfer, in bytes.",
    )
    start_time: Optional[datetime] = Field(
        None,
        alias="startTime",
        description="Gets the UTC time at which the transfer transitioned into the Soulseek.TransferStates.InProgress state.",
    )
    state: Optional[TransferStates] = None
    token: Optional[StrictInt] = Field(
        None, description="Gets the unique token for the transfer."
    )
    username: Optional[StrictStr] = Field(
        None,
        description="Gets the username of the peer to or from which the file is to be transferred.",
    )
    exception: Optional[StrictStr] = Field(
        None,
        description="Gets the Exception that caused the failure of the transfer, if applicable.",
    )
    __properties = [
        "averageSpeed",
        "bytesRemaining",
        "bytesTransferred",
        "direction",
        "elapsedTime",
        "endTime",
        "filename",
        "id",
        "ipEndPoint",
        "percentComplete",
        "placeInQueue",
        "remainingTime",
        "remoteToken",
        "size",
        "startOffset",
        "startTime",
        "state",
        "token",
        "username",
        "exception",
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
    def from_json(cls, json_str: str) -> Transfer:
        """Create an instance of Transfer from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(
            by_alias=True,
            exclude={
                "id",
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of ip_end_point
        if self.ip_end_point:
            _dict["ipEndPoint"] = self.ip_end_point.to_dict()
        # set to None if elapsed_time (nullable) is None
        # and __fields_set__ contains the field
        if self.elapsed_time is None and "elapsed_time" in self.__fields_set__:
            _dict["elapsedTime"] = None

        # set to None if end_time (nullable) is None
        # and __fields_set__ contains the field
        if self.end_time is None and "end_time" in self.__fields_set__:
            _dict["endTime"] = None

        # set to None if filename (nullable) is None
        # and __fields_set__ contains the field
        if self.filename is None and "filename" in self.__fields_set__:
            _dict["filename"] = None

        # set to None if id (nullable) is None
        # and __fields_set__ contains the field
        if self.id is None and "id" in self.__fields_set__:
            _dict["id"] = None

        # set to None if place_in_queue (nullable) is None
        # and __fields_set__ contains the field
        if self.place_in_queue is None and "place_in_queue" in self.__fields_set__:
            _dict["placeInQueue"] = None

        # set to None if remaining_time (nullable) is None
        # and __fields_set__ contains the field
        if self.remaining_time is None and "remaining_time" in self.__fields_set__:
            _dict["remainingTime"] = None

        # set to None if remote_token (nullable) is None
        # and __fields_set__ contains the field
        if self.remote_token is None and "remote_token" in self.__fields_set__:
            _dict["remoteToken"] = None

        # set to None if start_time (nullable) is None
        # and __fields_set__ contains the field
        if self.start_time is None and "start_time" in self.__fields_set__:
            _dict["startTime"] = None

        # set to None if username (nullable) is None
        # and __fields_set__ contains the field
        if self.username is None and "username" in self.__fields_set__:
            _dict["username"] = None

        # set to None if exception (nullable) is None
        # and __fields_set__ contains the field
        if self.exception is None and "exception" in self.__fields_set__:
            _dict["exception"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Transfer:
        """Create an instance of Transfer from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Transfer.parse_obj(obj)

        _obj = Transfer.parse_obj(
            {
                "average_speed": obj.get("averageSpeed"),
                "bytes_remaining": obj.get("bytesRemaining"),
                "bytes_transferred": obj.get("bytesTransferred"),
                "direction": obj.get("direction"),
                "elapsed_time": obj.get("elapsedTime"),
                "end_time": obj.get("endTime"),
                "filename": obj.get("filename"),
                "id": obj.get("id"),
                "ip_end_point": IPEndPoint.from_dict(obj.get("ipEndPoint"))
                if obj.get("ipEndPoint") is not None
                else None,
                "percent_complete": obj.get("percentComplete"),
                "place_in_queue": obj.get("placeInQueue"),
                "remaining_time": obj.get("remainingTime"),
                "remote_token": obj.get("remoteToken"),
                "size": obj.get("size"),
                "start_offset": obj.get("startOffset"),
                "start_time": obj.get("startTime"),
                "state": obj.get("state"),
                "token": obj.get("token"),
                "username": obj.get("username"),
                "exception": obj.get("exception"),
            }
        )
        return _obj
