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


from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist, constr, validator
from lusid.models.link import Link
from lusid.models.resource_id import ResourceId
from lusid.models.tax_rule import TaxRule
from lusid.models.version import Version

class TaxRuleSet(BaseModel):
    """
    TaxRuleSet
    """
    id: ResourceId = Field(...)
    display_name: constr(strict=True, max_length=1024, min_length=0) = Field(..., alias="displayName", description="A user-friendly name")
    description: constr(strict=True, max_length=1024, min_length=0) = Field(..., description="A description of what this rule set is for")
    output_property_key: StrictStr = Field(..., alias="outputPropertyKey", description="The property key that this rule set will write to")
    rules: conlist(TaxRule, max_items=100) = Field(..., description="The rules of this rule set, which stipulate what rate to apply (i.e. write to the OutputPropertyKey) under certain conditions")
    version: Optional[Version] = None
    links: Optional[conlist(Link)] = None
    __properties = ["id", "displayName", "description", "outputPropertyKey", "rules", "version", "links"]

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
    def from_json(cls, json_str: str) -> TaxRuleSet:
        """Create an instance of TaxRuleSet from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of id
        if self.id:
            _dict['id'] = self.id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in rules (list)
        _items = []
        if self.rules:
            for _item in self.rules:
                if _item:
                    _items.append(_item.to_dict())
            _dict['rules'] = _items
        # override the default output from pydantic by calling `to_dict()` of version
        if self.version:
            _dict['version'] = self.version.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item in self.links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['links'] = _items
        # set to None if links (nullable) is None
        # and __fields_set__ contains the field
        if self.links is None and "links" in self.__fields_set__:
            _dict['links'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TaxRuleSet:
        """Create an instance of TaxRuleSet from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TaxRuleSet.parse_obj(obj)

        _obj = TaxRuleSet.parse_obj({
            "id": ResourceId.from_dict(obj.get("id")) if obj.get("id") is not None else None,
            "display_name": obj.get("displayName"),
            "description": obj.get("description"),
            "output_property_key": obj.get("outputPropertyKey"),
            "rules": [TaxRule.from_dict(_item) for _item in obj.get("rules")] if obj.get("rules") is not None else None,
            "version": Version.from_dict(obj.get("version")) if obj.get("version") is not None else None,
            "links": [Link.from_dict(_item) for _item in obj.get("links")] if obj.get("links") is not None else None
        })
        return _obj