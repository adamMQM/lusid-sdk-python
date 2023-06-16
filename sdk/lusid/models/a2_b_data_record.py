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


from typing import Dict, List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from lusid.models.a2_b_category import A2BCategory
from lusid.models.model_property import ModelProperty
from lusid.models.perpetual_property import PerpetualProperty
from lusid.models.resource_id import ResourceId
from lusid.models.response_meta_data import ResponseMetaData

class A2BDataRecord(BaseModel):
    """
    A2B Record - shows values on, and changes between two dates: A and B
    """
    portfolio_id: Optional[ResourceId] = Field(None, alias="portfolioId")
    holding_type: Optional[StrictStr] = Field(None, alias="holdingType", description="The code for the type of the holding e.g. P, B, C, R, F etc.")
    instrument_scope: Optional[StrictStr] = Field(None, alias="instrumentScope", description="The unique Lusid Instrument Id (LUID) of the instrument that the holding is in.")
    instrument_uid: Optional[StrictStr] = Field(None, alias="instrumentUid", description="The unique Lusid Instrument Id (LUID) of the instrument that the holding is in.")
    sub_holding_keys: Optional[Dict[str, PerpetualProperty]] = Field(None, alias="subHoldingKeys", description="The sub-holding properties which identify the holding. Each property will be from the 'Transaction' domain. These are configured on a transaction portfolio.")
    currency: Optional[StrictStr] = Field(None, description="The holding currency.")
    transaction_id: Optional[StrictStr] = Field(None, alias="transactionId", description="The unique identifier for the transaction.")
    start: Optional[A2BCategory] = None
    flows: Optional[A2BCategory] = None
    gains: Optional[A2BCategory] = None
    carry: Optional[A2BCategory] = None
    end: Optional[A2BCategory] = None
    properties: Optional[Dict[str, ModelProperty]] = Field(None, description="The properties which have been requested to be decorated onto the holding. These will be from the 'Instrument' domain.")
    group_id: Optional[StrictStr] = Field(None, alias="groupId", description="Arbitrary string that can be used to cross reference an entry in the A2B report with activity in the A2B-Movements. This should be used purely as a token. The content should not be relied upon.")
    errors: Optional[conlist(ResponseMetaData)] = Field(None, description="Any errors with the record are reported here.")
    __properties = ["portfolioId", "holdingType", "instrumentScope", "instrumentUid", "subHoldingKeys", "currency", "transactionId", "start", "flows", "gains", "carry", "end", "properties", "groupId", "errors"]

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
    def from_json(cls, json_str: str) -> A2BDataRecord:
        """Create an instance of A2BDataRecord from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of portfolio_id
        if self.portfolio_id:
            _dict['portfolioId'] = self.portfolio_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each value in sub_holding_keys (dict)
        _field_dict = {}
        if self.sub_holding_keys:
            for _key in self.sub_holding_keys:
                if self.sub_holding_keys[_key]:
                    _field_dict[_key] = self.sub_holding_keys[_key].to_dict()
            _dict['subHoldingKeys'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of start
        if self.start:
            _dict['start'] = self.start.to_dict()
        # override the default output from pydantic by calling `to_dict()` of flows
        if self.flows:
            _dict['flows'] = self.flows.to_dict()
        # override the default output from pydantic by calling `to_dict()` of gains
        if self.gains:
            _dict['gains'] = self.gains.to_dict()
        # override the default output from pydantic by calling `to_dict()` of carry
        if self.carry:
            _dict['carry'] = self.carry.to_dict()
        # override the default output from pydantic by calling `to_dict()` of end
        if self.end:
            _dict['end'] = self.end.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each value in properties (dict)
        _field_dict = {}
        if self.properties:
            for _key in self.properties:
                if self.properties[_key]:
                    _field_dict[_key] = self.properties[_key].to_dict()
            _dict['properties'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each item in errors (list)
        _items = []
        if self.errors:
            for _item in self.errors:
                if _item:
                    _items.append(_item.to_dict())
            _dict['errors'] = _items
        # set to None if holding_type (nullable) is None
        # and __fields_set__ contains the field
        if self.holding_type is None and "holding_type" in self.__fields_set__:
            _dict['holdingType'] = None

        # set to None if instrument_scope (nullable) is None
        # and __fields_set__ contains the field
        if self.instrument_scope is None and "instrument_scope" in self.__fields_set__:
            _dict['instrumentScope'] = None

        # set to None if instrument_uid (nullable) is None
        # and __fields_set__ contains the field
        if self.instrument_uid is None and "instrument_uid" in self.__fields_set__:
            _dict['instrumentUid'] = None

        # set to None if sub_holding_keys (nullable) is None
        # and __fields_set__ contains the field
        if self.sub_holding_keys is None and "sub_holding_keys" in self.__fields_set__:
            _dict['subHoldingKeys'] = None

        # set to None if currency (nullable) is None
        # and __fields_set__ contains the field
        if self.currency is None and "currency" in self.__fields_set__:
            _dict['currency'] = None

        # set to None if transaction_id (nullable) is None
        # and __fields_set__ contains the field
        if self.transaction_id is None and "transaction_id" in self.__fields_set__:
            _dict['transactionId'] = None

        # set to None if properties (nullable) is None
        # and __fields_set__ contains the field
        if self.properties is None and "properties" in self.__fields_set__:
            _dict['properties'] = None

        # set to None if group_id (nullable) is None
        # and __fields_set__ contains the field
        if self.group_id is None and "group_id" in self.__fields_set__:
            _dict['groupId'] = None

        # set to None if errors (nullable) is None
        # and __fields_set__ contains the field
        if self.errors is None and "errors" in self.__fields_set__:
            _dict['errors'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> A2BDataRecord:
        """Create an instance of A2BDataRecord from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return A2BDataRecord.parse_obj(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in A2BDataRecord) in the input: " + obj)

        _obj = A2BDataRecord.parse_obj({
            "portfolio_id": ResourceId.from_dict(obj.get("portfolioId")) if obj.get("portfolioId") is not None else None,
            "holding_type": obj.get("holdingType"),
            "instrument_scope": obj.get("instrumentScope"),
            "instrument_uid": obj.get("instrumentUid"),
            "sub_holding_keys": {k: (None if v is None else PerpetualProperty.from_dict(v)) for k, v in obj.get("subHoldingKeys").items()} if obj.get("subHoldingKeys") is not None else None,
            "currency": obj.get("currency"),
            "transaction_id": obj.get("transactionId"),
            "start": A2BCategory.from_dict(obj.get("start")) if obj.get("start") is not None else None,
            "flows": A2BCategory.from_dict(obj.get("flows")) if obj.get("flows") is not None else None,
            "gains": A2BCategory.from_dict(obj.get("gains")) if obj.get("gains") is not None else None,
            "carry": A2BCategory.from_dict(obj.get("carry")) if obj.get("carry") is not None else None,
            "end": A2BCategory.from_dict(obj.get("end")) if obj.get("end") is not None else None,
            "properties": {k: (None if v is None else ModelProperty.from_dict(v)) for k, v in obj.get("properties").items()} if obj.get("properties") is not None else None,
            "group_id": obj.get("groupId"),
            "errors": [ResponseMetaData.from_dict(_item) for _item in obj.get("errors")] if obj.get("errors") is not None else None
        })
        return _obj

