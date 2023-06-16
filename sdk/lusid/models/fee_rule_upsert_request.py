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


from typing import Dict, Optional
from pydantic import BaseModel, Field, StrictStr, constr, validator
from lusid.models.calculation_info import CalculationInfo

class FeeRuleUpsertRequest(BaseModel):
    """
    FeeRuleUpsertRequest
    """
    code: Optional[constr(strict=True, max_length=64, min_length=1)] = None
    transaction_property_key: StrictStr = Field(..., alias="transactionPropertyKey")
    transaction_type: constr(strict=True, max_length=64, min_length=1) = Field(..., alias="transactionType")
    country: constr(strict=True, max_length=64, min_length=1) = Field(...)
    counterparty: constr(strict=True, max_length=64, min_length=1) = Field(...)
    transaction_currency: constr(strict=True, max_length=64, min_length=1) = Field(..., alias="transactionCurrency")
    settlement_currency: constr(strict=True, max_length=64, min_length=1) = Field(..., alias="settlementCurrency")
    execution_broker: constr(strict=True, max_length=64, min_length=1) = Field(..., alias="executionBroker")
    custodian: constr(strict=True, max_length=64, min_length=1) = Field(...)
    exchange: constr(strict=True, max_length=64, min_length=1) = Field(...)
    fee: CalculationInfo = Field(...)
    min_fee: Optional[CalculationInfo] = Field(None, alias="minFee")
    max_fee: Optional[CalculationInfo] = Field(None, alias="maxFee")
    additional_keys: Optional[Dict[str, StrictStr]] = Field(None, alias="additionalKeys")
    description: Optional[constr(strict=True, max_length=1024, min_length=0)] = None
    __properties = ["code", "transactionPropertyKey", "transactionType", "country", "counterparty", "transactionCurrency", "settlementCurrency", "executionBroker", "custodian", "exchange", "fee", "minFee", "maxFee", "additionalKeys", "description"]

    @validator('code')
    def code_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-zA-Z0-9\-_]+$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9\-_]+$/")
        return value

    @validator('description')
    def description_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

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
    def from_json(cls, json_str: str) -> FeeRuleUpsertRequest:
        """Create an instance of FeeRuleUpsertRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of fee
        if self.fee:
            _dict['fee'] = self.fee.to_dict()
        # override the default output from pydantic by calling `to_dict()` of min_fee
        if self.min_fee:
            _dict['minFee'] = self.min_fee.to_dict()
        # override the default output from pydantic by calling `to_dict()` of max_fee
        if self.max_fee:
            _dict['maxFee'] = self.max_fee.to_dict()
        # set to None if code (nullable) is None
        # and __fields_set__ contains the field
        if self.code is None and "code" in self.__fields_set__:
            _dict['code'] = None

        # set to None if additional_keys (nullable) is None
        # and __fields_set__ contains the field
        if self.additional_keys is None and "additional_keys" in self.__fields_set__:
            _dict['additionalKeys'] = None

        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> FeeRuleUpsertRequest:
        """Create an instance of FeeRuleUpsertRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FeeRuleUpsertRequest.parse_obj(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in FeeRuleUpsertRequest) in the input: " + obj)

        _obj = FeeRuleUpsertRequest.parse_obj({
            "code": obj.get("code"),
            "transaction_property_key": obj.get("transactionPropertyKey"),
            "transaction_type": obj.get("transactionType"),
            "country": obj.get("country"),
            "counterparty": obj.get("counterparty"),
            "transaction_currency": obj.get("transactionCurrency"),
            "settlement_currency": obj.get("settlementCurrency"),
            "execution_broker": obj.get("executionBroker"),
            "custodian": obj.get("custodian"),
            "exchange": obj.get("exchange"),
            "fee": CalculationInfo.from_dict(obj.get("fee")) if obj.get("fee") is not None else None,
            "min_fee": CalculationInfo.from_dict(obj.get("minFee")) if obj.get("minFee") is not None else None,
            "max_fee": CalculationInfo.from_dict(obj.get("maxFee")) if obj.get("maxFee") is not None else None,
            "additional_keys": obj.get("additionalKeys"),
            "description": obj.get("description")
        })
        return _obj

