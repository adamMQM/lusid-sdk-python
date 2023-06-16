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
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist
from lusid.models.link import Link
from lusid.models.resource_id import ResourceId

class SequenceDefinition(BaseModel):
    """
    SequenceDefinition
    """
    id: ResourceId = Field(...)
    increment: StrictInt = Field(..., description="The Resource Id of the sequence definition")
    min_value: StrictInt = Field(..., alias="minValue", description="The minimum value of the sequence")
    max_value: StrictInt = Field(..., alias="maxValue", description="The maximum value of the sequence")
    start: StrictInt = Field(..., description="The start value of the sequence")
    value: Optional[StrictInt] = Field(None, description="The last used value of the sequence")
    cycle: StrictBool = Field(..., description="Indicates if the sequence would start from minimun value once it reaches maximum value. If set to false, a failure would return if the sequence reaches maximum value.")
    pattern: Optional[StrictStr] = Field(None, description="The pattern to be used to generate next values in the sequence.")
    links: Optional[conlist(Link)] = None
    __properties = ["id", "increment", "minValue", "maxValue", "start", "value", "cycle", "pattern", "links"]

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
    def from_json(cls, json_str: str) -> SequenceDefinition:
        """Create an instance of SequenceDefinition from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item in self.links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['links'] = _items
        # set to None if value (nullable) is None
        # and __fields_set__ contains the field
        if self.value is None and "value" in self.__fields_set__:
            _dict['value'] = None

        # set to None if pattern (nullable) is None
        # and __fields_set__ contains the field
        if self.pattern is None and "pattern" in self.__fields_set__:
            _dict['pattern'] = None

        # set to None if links (nullable) is None
        # and __fields_set__ contains the field
        if self.links is None and "links" in self.__fields_set__:
            _dict['links'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SequenceDefinition:
        """Create an instance of SequenceDefinition from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SequenceDefinition.parse_obj(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in SequenceDefinition) in the input: " + obj)

        _obj = SequenceDefinition.parse_obj({
            "id": ResourceId.from_dict(obj.get("id")) if obj.get("id") is not None else None,
            "increment": obj.get("increment"),
            "min_value": obj.get("minValue"),
            "max_value": obj.get("maxValue"),
            "start": obj.get("start"),
            "value": obj.get("value"),
            "cycle": obj.get("cycle"),
            "pattern": obj.get("pattern"),
            "links": [Link.from_dict(_item) for _item in obj.get("links")] if obj.get("links") is not None else None
        })
        return _obj

