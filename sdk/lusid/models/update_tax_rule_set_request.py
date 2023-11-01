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
from pydantic import BaseModel, Field, conlist, constr, validator
from lusid.models.tax_rule import TaxRule

class UpdateTaxRuleSetRequest(BaseModel):
    """
    UpdateTaxRuleSetRequest
    """
    display_name: constr(strict=True, max_length=1024, min_length=0) = Field(..., alias="displayName")
    description: constr(strict=True, max_length=1024, min_length=0) = Field(...)
    rules: conlist(TaxRule, max_items=100) = Field(...)
    __properties = ["displayName", "description", "rules"]

    @validator('display_name')
    def display_name_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[\s\S]*$", value):
            raise ValueError(r"must validate the regular expression /^[\s\S]*$/")
        return value

    @validator('description')
    def description_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[\s\S]*$", value):
            raise ValueError(r"must validate the regular expression /^[\s\S]*$/")
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
    def from_json(cls, json_str: str) -> UpdateTaxRuleSetRequest:
        """Create an instance of UpdateTaxRuleSetRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in rules (list)
        _items = []
        if self.rules:
            for _item in self.rules:
                if _item:
                    _items.append(_item.to_dict())
            _dict['rules'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UpdateTaxRuleSetRequest:
        """Create an instance of UpdateTaxRuleSetRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UpdateTaxRuleSetRequest.parse_obj(obj)

        _obj = UpdateTaxRuleSetRequest.parse_obj({
            "display_name": obj.get("displayName"),
            "description": obj.get("description"),
            "rules": [TaxRule.from_dict(_item) for _item in obj.get("rules")] if obj.get("rules") is not None else None
        })
        return _obj