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


from typing import Any, Dict, List
from pydantic import BaseModel, Field, conlist
from lusid.models.placement_request import PlacementRequest

class PlaceBlocksRequest(BaseModel):
    """
    PlaceBlocksRequest
    """
    requests: conlist(PlacementRequest, max_items=100, min_items=1) = Field(..., description="A collection of PlacementRequest.")
    __properties = ["requests"]

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
    def from_json(cls, json_str: str) -> PlaceBlocksRequest:
        """Create an instance of PlaceBlocksRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in requests (list)
        _items = []
        if self.requests:
            for _item in self.requests:
                if _item:
                    _items.append(_item.to_dict())
            _dict['requests'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PlaceBlocksRequest:
        """Create an instance of PlaceBlocksRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PlaceBlocksRequest.parse_obj(obj)

        _obj = PlaceBlocksRequest.parse_obj({
            "requests": [PlacementRequest.from_dict(_item) for _item in obj.get("requests")] if obj.get("requests") is not None else None
        })
        return _obj