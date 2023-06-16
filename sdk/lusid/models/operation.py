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


from typing import Any, Optional
from pydantic import BaseModel, Field, constr

class Operation(BaseModel):
    """
    Operation
    """
    value: Optional[Any] = None
    path: constr(strict=True, max_length=6000, min_length=0) = Field(...)
    op: constr(strict=True, min_length=1) = Field(...)
    var_from: Optional[constr(strict=True, max_length=6000, min_length=0)] = Field(None, alias="from")
    __properties = ["value", "path", "op", "from"]

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
    def from_json(cls, json_str: str) -> Operation:
        """Create an instance of Operation from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if value (nullable) is None
        # and __fields_set__ contains the field
        if self.value is None and "value" in self.__fields_set__:
            _dict['value'] = None

        # set to None if var_from (nullable) is None
        # and __fields_set__ contains the field
        if self.var_from is None and "var_from" in self.__fields_set__:
            _dict['from'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Operation:
        """Create an instance of Operation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Operation.parse_obj(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in Operation) in the input: " + obj)

        _obj = Operation.parse_obj({
            "value": obj.get("value"),
            "path": obj.get("path"),
            "op": obj.get("op"),
            "var_from": obj.get("from")
        })
        return _obj

