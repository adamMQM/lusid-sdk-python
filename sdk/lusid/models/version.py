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
from pydantic import BaseModel, Field, StrictInt, StrictStr

class Version(BaseModel):
    """
    The version metadata.
    """
    effective_from: datetime = Field(..., alias="effectiveFrom", description="The effective datetime at which this version became valid. Only applies when a single entity is being interacted with.")
    as_at_date: datetime = Field(..., alias="asAtDate", description="The asAt datetime at which the data was committed to LUSID.")
    as_at_created: Optional[datetime] = Field(None, alias="asAtCreated", description="The asAt datetime at which the entity was first created in LUSID.")
    user_id_created: Optional[StrictStr] = Field(None, alias="userIdCreated", description="The unique id of the user who created the entity.")
    as_at_modified: Optional[datetime] = Field(None, alias="asAtModified", description="The asAt datetime at which the entity (including its properties) was last updated in LUSID.")
    user_id_modified: Optional[StrictStr] = Field(None, alias="userIdModified", description="The unique id of the user who last updated the entity (including its properties) in LUSID.")
    as_at_version_number: Optional[StrictInt] = Field(None, alias="asAtVersionNumber", description="The integer version number for the entity (the entity was created at version 1)")
    __properties = ["effectiveFrom", "asAtDate", "asAtCreated", "userIdCreated", "asAtModified", "userIdModified", "asAtVersionNumber"]

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
    def from_json(cls, json_str: str) -> Version:
        """Create an instance of Version from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "as_at_created",
                            "user_id_created",
                            "as_at_modified",
                            "user_id_modified",
                            "as_at_version_number",
                          },
                          exclude_none=True)
        # set to None if as_at_created (nullable) is None
        # and __fields_set__ contains the field
        if self.as_at_created is None and "as_at_created" in self.__fields_set__:
            _dict['asAtCreated'] = None

        # set to None if user_id_created (nullable) is None
        # and __fields_set__ contains the field
        if self.user_id_created is None and "user_id_created" in self.__fields_set__:
            _dict['userIdCreated'] = None

        # set to None if as_at_modified (nullable) is None
        # and __fields_set__ contains the field
        if self.as_at_modified is None and "as_at_modified" in self.__fields_set__:
            _dict['asAtModified'] = None

        # set to None if user_id_modified (nullable) is None
        # and __fields_set__ contains the field
        if self.user_id_modified is None and "user_id_modified" in self.__fields_set__:
            _dict['userIdModified'] = None

        # set to None if as_at_version_number (nullable) is None
        # and __fields_set__ contains the field
        if self.as_at_version_number is None and "as_at_version_number" in self.__fields_set__:
            _dict['asAtVersionNumber'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Version:
        """Create an instance of Version from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Version.parse_obj(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in Version) in the input: " + obj)

        _obj = Version.parse_obj({
            "effective_from": obj.get("effectiveFrom"),
            "as_at_date": obj.get("asAtDate"),
            "as_at_created": obj.get("asAtCreated"),
            "user_id_created": obj.get("userIdCreated"),
            "as_at_modified": obj.get("asAtModified"),
            "user_id_modified": obj.get("userIdModified"),
            "as_at_version_number": obj.get("asAtVersionNumber")
        })
        return _obj

