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

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist
from lusid.models.link import Link
from lusid.models.resource_id import ResourceId

class Change(BaseModel):
    """
    The time an entity was modified (amendment and/or historical correction).
    """
    href: Optional[StrictStr] = None
    entity_id: ResourceId = Field(..., alias="entityId")
    corrected: StrictBool = Field(...)
    correction_effective_at: Optional[datetime] = Field(None, alias="correctionEffectiveAt")
    correction_as_at: Optional[datetime] = Field(None, alias="correctionAsAt")
    amended: StrictBool = Field(...)
    amendment_effective_at: Optional[datetime] = Field(None, alias="amendmentEffectiveAt")
    amendment_as_at: Optional[datetime] = Field(None, alias="amendmentAsAt")
    links: Optional[conlist(Link)] = None
    __properties = ["href", "entityId", "corrected", "correctionEffectiveAt", "correctionAsAt", "amended", "amendmentEffectiveAt", "amendmentAsAt", "links"]

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
    def from_json(cls, json_str: str) -> Change:
        """Create an instance of Change from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of entity_id
        if self.entity_id:
            _dict['entityId'] = self.entity_id.to_dict()
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

        # set to None if correction_effective_at (nullable) is None
        # and __fields_set__ contains the field
        if self.correction_effective_at is None and "correction_effective_at" in self.__fields_set__:
            _dict['correctionEffectiveAt'] = None

        # set to None if correction_as_at (nullable) is None
        # and __fields_set__ contains the field
        if self.correction_as_at is None and "correction_as_at" in self.__fields_set__:
            _dict['correctionAsAt'] = None

        # set to None if amendment_effective_at (nullable) is None
        # and __fields_set__ contains the field
        if self.amendment_effective_at is None and "amendment_effective_at" in self.__fields_set__:
            _dict['amendmentEffectiveAt'] = None

        # set to None if amendment_as_at (nullable) is None
        # and __fields_set__ contains the field
        if self.amendment_as_at is None and "amendment_as_at" in self.__fields_set__:
            _dict['amendmentAsAt'] = None

        # set to None if links (nullable) is None
        # and __fields_set__ contains the field
        if self.links is None and "links" in self.__fields_set__:
            _dict['links'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Change:
        """Create an instance of Change from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Change.parse_obj(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in Change) in the input: " + obj)

        _obj = Change.parse_obj({
            "href": obj.get("href"),
            "entity_id": ResourceId.from_dict(obj.get("entityId")) if obj.get("entityId") is not None else None,
            "corrected": obj.get("corrected"),
            "correction_effective_at": obj.get("correctionEffectiveAt"),
            "correction_as_at": obj.get("correctionAsAt"),
            "amended": obj.get("amended"),
            "amendment_effective_at": obj.get("amendmentEffectiveAt"),
            "amendment_as_at": obj.get("amendmentAsAt"),
            "links": [Link.from_dict(_item) for _item in obj.get("links")] if obj.get("links") is not None else None
        })
        return _obj

