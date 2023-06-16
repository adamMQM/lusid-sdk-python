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


from typing import Dict, List
from pydantic import BaseModel, Field, conlist
from lusid.models.access_metadata_value import AccessMetadataValue
from lusid.models.quote_access_metadata_rule_id import QuoteAccessMetadataRuleId

class UpsertQuoteAccessMetadataRuleRequest(BaseModel):
    """
    UpsertQuoteAccessMetadataRuleRequest
    """
    id: QuoteAccessMetadataRuleId = Field(...)
    metadata: Dict[str, conlist(AccessMetadataValue)] = Field(..., description="The access control metadata to assign to quotes that match the identifier")
    __properties = ["id", "metadata"]

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
    def from_json(cls, json_str: str) -> UpsertQuoteAccessMetadataRuleRequest:
        """Create an instance of UpsertQuoteAccessMetadataRuleRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each value in metadata (dict)
        _field_dict = {}
        if self.metadata:
            for _key in self.metadata:
                if self.metadata[_key]:
                    _field_dict[_key] = self.metadata[_key].to_dict()
            _dict['metadata'] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UpsertQuoteAccessMetadataRuleRequest:
        """Create an instance of UpsertQuoteAccessMetadataRuleRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UpsertQuoteAccessMetadataRuleRequest.parse_obj(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in UpsertQuoteAccessMetadataRuleRequest) in the input: " + obj)

        _obj = UpsertQuoteAccessMetadataRuleRequest.parse_obj({
            "id": QuoteAccessMetadataRuleId.from_dict(obj.get("id")) if obj.get("id") is not None else None,
            "metadata": {k: (None if v is None else [AccessMetadataValue.from_dict(iv) for iv in v]) for k, v in obj.get("metadata").items()} if obj.get("metadata") is not None else None,
        })
        return _obj

