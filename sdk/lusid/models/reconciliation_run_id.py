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
from lusid.models.reconciliation_id import ReconciliationId

class ReconciliationRunId(BaseModel):
    """
    ReconciliationRunId
    """
    reconciliation: Optional[ReconciliationId] = None
    var_date: Optional[datetime] = Field(None, alias="date")
    version: Optional[StrictInt] = None
    as_string: Optional[StrictStr] = Field(None, alias="asString")
    __properties = ["reconciliation", "date", "version", "asString"]

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
    def from_json(cls, json_str: str) -> ReconciliationRunId:
        """Create an instance of ReconciliationRunId from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "as_string",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of reconciliation
        if self.reconciliation:
            _dict['reconciliation'] = self.reconciliation.to_dict()
        # set to None if as_string (nullable) is None
        # and __fields_set__ contains the field
        if self.as_string is None and "as_string" in self.__fields_set__:
            _dict['asString'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ReconciliationRunId:
        """Create an instance of ReconciliationRunId from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ReconciliationRunId.parse_obj(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in ReconciliationRunId) in the input: " + obj)

        _obj = ReconciliationRunId.parse_obj({
            "reconciliation": ReconciliationId.from_dict(obj.get("reconciliation")) if obj.get("reconciliation") is not None else None,
            "var_date": obj.get("date"),
            "version": obj.get("version"),
            "as_string": obj.get("asString")
        })
        return _obj

