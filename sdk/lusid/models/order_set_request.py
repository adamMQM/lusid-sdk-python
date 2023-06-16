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


from typing import List, Optional
from pydantic import BaseModel, Field, conlist
from lusid.models.order_request import OrderRequest

class OrderSetRequest(BaseModel):
    """
    A request to create or update multiple Orders.
    """
    order_requests: Optional[conlist(OrderRequest)] = Field(None, alias="orderRequests", description="A collection of OrderRequests.")
    __properties = ["orderRequests"]

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
    def from_json(cls, json_str: str) -> OrderSetRequest:
        """Create an instance of OrderSetRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in order_requests (list)
        _items = []
        if self.order_requests:
            for _item in self.order_requests:
                if _item:
                    _items.append(_item.to_dict())
            _dict['orderRequests'] = _items
        # set to None if order_requests (nullable) is None
        # and __fields_set__ contains the field
        if self.order_requests is None and "order_requests" in self.__fields_set__:
            _dict['orderRequests'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OrderSetRequest:
        """Create an instance of OrderSetRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OrderSetRequest.parse_obj(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in OrderSetRequest) in the input: " + obj)

        _obj = OrderSetRequest.parse_obj({
            "order_requests": [OrderRequest.from_dict(_item) for _item in obj.get("orderRequests")] if obj.get("orderRequests") is not None else None
        })
        return _obj

