# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    Contact: info@finbourne.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Dict, List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from lusid.models.link import Link
from lusid.models.response_meta_data import ResponseMetaData
from lusid.models.version import Version

class AdjustHolding(BaseModel):
    """
    AdjustHolding
    """
    href: Optional[StrictStr] = Field(None, description="The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.")
    version: Version = Field(...)
    metadata: Optional[Dict[str, conlist(ResponseMetaData)]] = Field(None, description="Contains warnings related to unresolved instruments")
    links: Optional[conlist(Link)] = None
    __properties = ["href", "version", "metadata", "links"]

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
    def from_json(cls, json_str: str) -> AdjustHolding:
        """Create an instance of AdjustHolding from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of version
        if self.version:
            _dict['version'] = self.version.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each value in metadata (dict)
        _field_dict = {}
        if self.metadata:
            for _key in self.metadata:
                if self.metadata[_key]:
                    _field_dict[_key] = self.metadata[_key].to_dict()
            _dict['metadata'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item in self.links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['links'] = _items
        # set to None if href (nullable) is None
        # and __fields_set__ contains the field
        if self.href is None and "href" in self.__fields_set__:
            _dict['href'] = None

        # set to None if metadata (nullable) is None
        # and __fields_set__ contains the field
        if self.metadata is None and "metadata" in self.__fields_set__:
            _dict['metadata'] = None

        # set to None if links (nullable) is None
        # and __fields_set__ contains the field
        if self.links is None and "links" in self.__fields_set__:
            _dict['links'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AdjustHolding:
        """Create an instance of AdjustHolding from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AdjustHolding.parse_obj(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in AdjustHolding) in the input: " + obj)

        _obj = AdjustHolding.parse_obj({
            "href": obj.get("href"),
            "version": Version.from_dict(obj.get("version")) if obj.get("version") is not None else None,
            "metadata": {k: (None if v is None else [ResponseMetaData.from_dict(iv) for iv in v]) for k, v in obj.get("metadata").items()} if obj.get("metadata") is not None else None,
            "links": [Link.from_dict(_item) for _item in obj.get("links")] if obj.get("links") is not None else None
        })
        return _obj

