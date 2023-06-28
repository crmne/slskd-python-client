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

from pydantic import BaseModel, Field, StrictInt, StrictStr


class QueueDownloadRequest(BaseModel):
    """
    QueueDownloadRequest
    """

    filename: Optional[StrictStr] = Field(
        None, description="Gets or sets the filename to download."
    )
    size: Optional[StrictInt] = Field(
        None, description="Gets or sets the size of the file."
    )
    __properties = ["filename", "size"]

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
    def from_json(cls, json_str: str) -> QueueDownloadRequest:
        """Create an instance of QueueDownloadRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # set to None if filename (nullable) is None
        # and __fields_set__ contains the field
        if self.filename is None and "filename" in self.__fields_set__:
            _dict["filename"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> QueueDownloadRequest:
        """Create an instance of QueueDownloadRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return QueueDownloadRequest.parse_obj(obj)

        _obj = QueueDownloadRequest.parse_obj(
            {"filename": obj.get("filename"), "size": obj.get("size")}
        )
        return _obj