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
from pydantic import BaseModel, conlist
from lusid.models.error_detail import ErrorDetail
from lusid.models.resource_id import ResourceId

class AllocationServiceRunResult(BaseModel):
    """
    AllocationServiceRunResult
    """
    values: Optional[conlist(ResourceId)] = None
    failed: Optional[Dict[str, ErrorDetail]] = None
    __properties = ["values", "failed"]

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
    def from_json(cls, json_str: str) -> AllocationServiceRunResult:
        """Create an instance of AllocationServiceRunResult from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in values (list)
        _items = []
        if self.values:
            for _item in self.values:
                if _item:
                    _items.append(_item.to_dict())
            _dict['values'] = _items
        # override the default output from pydantic by calling `to_dict()` of each value in failed (dict)
        _field_dict = {}
        if self.failed:
            for _key in self.failed:
                if self.failed[_key]:
                    _field_dict[_key] = self.failed[_key].to_dict()
            _dict['failed'] = _field_dict
        # set to None if values (nullable) is None
        # and __fields_set__ contains the field
        if self.values is None and "values" in self.__fields_set__:
            _dict['values'] = None

        # set to None if failed (nullable) is None
        # and __fields_set__ contains the field
        if self.failed is None and "failed" in self.__fields_set__:
            _dict['failed'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AllocationServiceRunResult:
        """Create an instance of AllocationServiceRunResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AllocationServiceRunResult.parse_obj(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in AllocationServiceRunResult) in the input: " + obj)

        _obj = AllocationServiceRunResult.parse_obj({
            "values": [ResourceId.from_dict(_item) for _item in obj.get("values")] if obj.get("values") is not None else None,
            "failed": {k: (None if v is None else ErrorDetail.from_dict(v)) for k, v in obj.get("failed").items()} if obj.get("failed") is not None else None,
        })
        return _obj

