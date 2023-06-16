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

class EntityIdentifier(BaseModel):
    """
    Dto to expose mapped keys to new standardised format
    """
    identifier_scope: Optional[StrictStr] = Field(None, alias="identifierScope", description="The scope of the identifier")
    identifier_type: StrictStr = Field(..., alias="identifierType", description="The type of the identifier")
    identifier_value: StrictStr = Field(..., alias="identifierValue", description="The value of the identifier")
    __properties = ["identifierScope", "identifierType", "identifierValue"]

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
    def from_json(cls, json_str: str) -> EntityIdentifier:
        """Create an instance of EntityIdentifier from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if identifier_scope (nullable) is None
        # and __fields_set__ contains the field
        if self.identifier_scope is None and "identifier_scope" in self.__fields_set__:
            _dict['identifierScope'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EntityIdentifier:
        """Create an instance of EntityIdentifier from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EntityIdentifier.parse_obj(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in EntityIdentifier) in the input: " + obj)

        _obj = EntityIdentifier.parse_obj({
            "identifier_scope": obj.get("identifierScope"),
            "identifier_type": obj.get("identifierType"),
            "identifier_value": obj.get("identifierValue")
        })
        return _obj

