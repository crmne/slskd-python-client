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
from typing import Optional, Union

from pydantic import BaseModel, Field, StrictBool, StrictBytes, StrictInt, StrictStr


class Info(BaseModel):
    """
    Info
    """

    description: Optional[StrictStr] = None
    has_free_upload_slot: Optional[StrictBool] = Field(None, alias="hasFreeUploadSlot")
    has_picture: Optional[StrictBool] = Field(None, alias="hasPicture")
    picture: Optional[Union[StrictBytes, StrictStr]] = None
    queue_length: Optional[StrictInt] = Field(None, alias="queueLength")
    upload_slots: Optional[StrictInt] = Field(None, alias="uploadSlots")
    __properties = [
        "description",
        "hasFreeUploadSlot",
        "hasPicture",
        "picture",
        "queueLength",
        "uploadSlots",
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
    def from_json(cls, json_str: str) -> Info:
        """Create an instance of Info from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict["description"] = None

        # set to None if picture (nullable) is None
        # and __fields_set__ contains the field
        if self.picture is None and "picture" in self.__fields_set__:
            _dict["picture"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Info:
        """Create an instance of Info from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Info.parse_obj(obj)

        _obj = Info.parse_obj(
            {
                "description": obj.get("description"),
                "has_free_upload_slot": obj.get("hasFreeUploadSlot"),
                "has_picture": obj.get("hasPicture"),
                "picture": obj.get("picture"),
                "queue_length": obj.get("queueLength"),
                "upload_slots": obj.get("uploadSlots"),
            }
        )
        return _obj
