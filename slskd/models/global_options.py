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

from pydantic import BaseModel

from slskd.models.global_download_options import GlobalDownloadOptions
from slskd.models.global_upload_options import GlobalUploadOptions


class GlobalOptions(BaseModel):
    """
    Global options.
    """

    upload: Optional[GlobalUploadOptions] = None
    download: Optional[GlobalDownloadOptions] = None
    __properties = ["upload", "download"]

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
    def from_json(cls, json_str: str) -> GlobalOptions:
        """Create an instance of GlobalOptions from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of upload
        if self.upload:
            _dict["upload"] = self.upload.to_dict()
        # override the default output from pydantic by calling `to_dict()` of download
        if self.download:
            _dict["download"] = self.download.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GlobalOptions:
        """Create an instance of GlobalOptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GlobalOptions.parse_obj(obj)

        _obj = GlobalOptions.parse_obj(
            {
                "upload": GlobalUploadOptions.from_dict(obj.get("upload"))
                if obj.get("upload") is not None
                else None,
                "download": GlobalDownloadOptions.from_dict(obj.get("download"))
                if obj.get("download") is not None
                else None,
            }
        )
        return _obj
