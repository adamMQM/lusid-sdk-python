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

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, constr, validator

class CustomEntityId(BaseModel):
    """
    CustomEntityId
    """
    identifier_scope: constr(strict=True, max_length=64, min_length=1) = Field(..., alias="identifierScope", description="The scope the identifier resides in (the scope of the identifier property definition).")
    identifier_type: constr(strict=True, max_length=64, min_length=1) = Field(..., alias="identifierType", description="What the identifier represents (the code of the identifier property definition).")
    identifier_value: constr(strict=True, max_length=1024, min_length=1) = Field(..., alias="identifierValue", description="The value of the identifier for this entity.")
    effective_from: Optional[datetime] = Field(None, alias="effectiveFrom", description="The effective datetime from which the identifier is valid.")
    effective_until: Optional[datetime] = Field(None, alias="effectiveUntil", description="The effective datetime until which the identifier is valid. If not supplied this will be valid indefinitely, or until the next 'effectiveFrom' datetime of the identifier.")
    __properties = ["identifierScope", "identifierType", "identifierValue", "effectiveFrom", "effectiveUntil"]

    @validator('identifier_scope')
    def identifier_scope_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-zA-Z0-9\-_]+$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9\-_]+$/")
        return value

    @validator('identifier_type')
    def identifier_type_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-zA-Z0-9\-_]+$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9\-_]+$/")
        return value

    @validator('identifier_value')
    def identifier_value_validate_regular_expression(cls, value):
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
    def from_json(cls, json_str: str) -> CustomEntityId:
        """Create an instance of CustomEntityId from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if effective_from (nullable) is None
        # and __fields_set__ contains the field
        if self.effective_from is None and "effective_from" in self.__fields_set__:
            _dict['effectiveFrom'] = None

        # set to None if effective_until (nullable) is None
        # and __fields_set__ contains the field
        if self.effective_until is None and "effective_until" in self.__fields_set__:
            _dict['effectiveUntil'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CustomEntityId:
        """Create an instance of CustomEntityId from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CustomEntityId.parse_obj(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in CustomEntityId) in the input: " + obj)

        _obj = CustomEntityId.parse_obj({
            "identifier_scope": obj.get("identifierScope"),
            "identifier_type": obj.get("identifierType"),
            "identifier_value": obj.get("identifierValue"),
            "effective_from": obj.get("effectiveFrom"),
            "effective_until": obj.get("effectiveUntil")
        })
        return _obj

