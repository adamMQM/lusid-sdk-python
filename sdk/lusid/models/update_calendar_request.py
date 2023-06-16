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
from pydantic import BaseModel, Field, conlist, constr, validator
from lusid.models.model_property import ModelProperty
from lusid.models.weekend_mask import WeekendMask

class UpdateCalendarRequest(BaseModel):
    """
    UpdateCalendarRequest
    """
    weekend_mask: WeekendMask = Field(..., alias="weekendMask")
    source_provider: constr(strict=True, max_length=256, min_length=1) = Field(..., alias="sourceProvider")
    properties: conlist(ModelProperty) = Field(...)
    __properties = ["weekendMask", "sourceProvider", "properties"]

    @validator('source_provider')
    def source_provider_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-zA-Z0-9\-_]+$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9\-_]+$/")
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
    def from_json(cls, json_str: str) -> UpdateCalendarRequest:
        """Create an instance of UpdateCalendarRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of weekend_mask
        if self.weekend_mask:
            _dict['weekendMask'] = self.weekend_mask.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in properties (list)
        _items = []
        if self.properties:
            for _item in self.properties:
                if _item:
                    _items.append(_item.to_dict())
            _dict['properties'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UpdateCalendarRequest:
        """Create an instance of UpdateCalendarRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UpdateCalendarRequest.parse_obj(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in UpdateCalendarRequest) in the input: " + obj)

        _obj = UpdateCalendarRequest.parse_obj({
            "weekend_mask": WeekendMask.from_dict(obj.get("weekendMask")) if obj.get("weekendMask") is not None else None,
            "source_provider": obj.get("sourceProvider"),
            "properties": [ModelProperty.from_dict(_item) for _item in obj.get("properties")] if obj.get("properties") is not None else None
        })
        return _obj

