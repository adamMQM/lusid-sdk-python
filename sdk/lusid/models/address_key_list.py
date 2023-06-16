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


from typing import List
from pydantic import BaseModel, Field, StrictStr, conlist, validator

class AddressKeyList(BaseModel):
    """
    AddressKeyList
    """
    values: conlist(StrictStr) = Field(...)
    reference_list_type: StrictStr = Field(..., alias="referenceListType", description="The reference list values. The available values are: PortfolioGroupIdList, PortfolioIdList, AddressKeyList, StringList, InstrumentList, DecimalList")
    __properties = ["values", "referenceListType"]

    @validator('reference_list_type')
    def reference_list_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('PortfolioGroupIdList', 'PortfolioIdList', 'AddressKeyList', 'StringList', 'InstrumentList', 'DecimalList'):
            raise ValueError("must be one of enum values ('PortfolioGroupIdList', 'PortfolioIdList', 'AddressKeyList', 'StringList', 'InstrumentList', 'DecimalList')")
        return value

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
    def from_json(cls, json_str: str) -> AddressKeyList:
        """Create an instance of AddressKeyList from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AddressKeyList:
        """Create an instance of AddressKeyList from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AddressKeyList.parse_obj(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in AddressKeyList) in the input: " + obj)

        _obj = AddressKeyList.parse_obj({
            "values": obj.get("values"),
            "reference_list_type": obj.get("referenceListType")
        })
        return _obj

