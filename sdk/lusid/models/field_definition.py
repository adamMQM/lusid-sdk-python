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



from pydantic import BaseModel, Field, StrictBool, constr, validator

class FieldDefinition(BaseModel):
    """
    FieldDefinition
    """
    key: constr(strict=True, max_length=512, min_length=1) = Field(...)
    is_required: StrictBool = Field(..., alias="isRequired")
    is_unique: StrictBool = Field(..., alias="isUnique")
    __properties = ["key", "isRequired", "isUnique"]

    @validator('key')
    def key_validate_regular_expression(cls, value):
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
    def from_json(cls, json_str: str) -> FieldDefinition:
        """Create an instance of FieldDefinition from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> FieldDefinition:
        """Create an instance of FieldDefinition from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FieldDefinition.parse_obj(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in FieldDefinition) in the input: " + obj)

        _obj = FieldDefinition.parse_obj({
            "key": obj.get("key"),
            "is_required": obj.get("isRequired"),
            "is_unique": obj.get("isUnique")
        })
        return _obj

