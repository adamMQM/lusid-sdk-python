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


from typing import Optional
from pydantic import BaseModel, Field, StrictStr
from lusid.models.property_value import PropertyValue

class PerpetualProperty(BaseModel):
    """
    PerpetualProperty
    """
    key: StrictStr = Field(..., description="The key of the property. This takes the format {domain}/{scope}/{code} e.g. 'Instrument/system/Name' or 'Transaction/strategy/quantsignal'.")
    value: Optional[PropertyValue] = None
    __properties = ["key", "value"]

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
    def from_json(cls, json_str: str) -> PerpetualProperty:
        """Create an instance of PerpetualProperty from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PerpetualProperty:
        """Create an instance of PerpetualProperty from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PerpetualProperty.parse_obj(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in PerpetualProperty) in the input: " + obj)

        _obj = PerpetualProperty.parse_obj({
            "key": obj.get("key"),
            "value": PropertyValue.from_dict(obj.get("value")) if obj.get("value") is not None else None
        })
        return _obj

