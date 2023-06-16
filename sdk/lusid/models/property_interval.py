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



from pydantic import BaseModel, Field, constr
from lusid.models.date_range import DateRange
from lusid.models.property_value import PropertyValue

class PropertyInterval(BaseModel):
    """
    PropertyInterval
    """
    value: PropertyValue = Field(...)
    effective_range: DateRange = Field(..., alias="effectiveRange")
    as_at_range: DateRange = Field(..., alias="asAtRange")
    status: constr(strict=True, min_length=1) = Field(..., description="Indicates whether the value is part of the prevailing effective date timeline for the requested asAt date, or whether it has been superseded by correctional activity")
    __properties = ["value", "effectiveRange", "asAtRange", "status"]

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
    def from_json(cls, json_str: str) -> PropertyInterval:
        """Create an instance of PropertyInterval from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of value
        if self.value:
            _dict['value'] = self.value.to_dict()
        # override the default output from pydantic by calling `to_dict()` of effective_range
        if self.effective_range:
            _dict['effectiveRange'] = self.effective_range.to_dict()
        # override the default output from pydantic by calling `to_dict()` of as_at_range
        if self.as_at_range:
            _dict['asAtRange'] = self.as_at_range.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PropertyInterval:
        """Create an instance of PropertyInterval from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PropertyInterval.parse_obj(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in PropertyInterval) in the input: " + obj)

        _obj = PropertyInterval.parse_obj({
            "value": PropertyValue.from_dict(obj.get("value")) if obj.get("value") is not None else None,
            "effective_range": DateRange.from_dict(obj.get("effectiveRange")) if obj.get("effectiveRange") is not None else None,
            "as_at_range": DateRange.from_dict(obj.get("asAtRange")) if obj.get("asAtRange") is not None else None,
            "status": obj.get("status")
        })
        return _obj

