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
from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, validator
from lusid.models.cash_flow_lineage import CashFlowLineage
from lusid.models.result_value_dictionary import ResultValueDictionary

class CashFlowValueAllOf(BaseModel):
    """
    CashFlowValueAllOf
    """
    payment_date: datetime = Field(..., alias="paymentDate", description="The payment date of the cash flow")
    diagnostics: Optional[ResultValueDictionary] = None
    cash_flow_lineage: Optional[CashFlowLineage] = Field(None, alias="cashFlowLineage")
    payment_amount: Union[StrictFloat, StrictInt] = Field(..., alias="paymentAmount", description="The amount paid or received")
    payment_ccy: StrictStr = Field(..., alias="paymentCcy", description="The currency of the transaction")
    result_value_type: StrictStr = Field(..., alias="resultValueType", description="The available values are: ResultValue, ResultValueDictionary, ResultValue0D, ResultValueDecimal, ResultValueInt, ResultValueString, ResultValueBool, ResultValueCurrency, CashFlowValue, CashFlowValueSet, ResultValueLifeCycleEventValue, ResultValueDateTimeOffset")
    additional_properties: Dict[str, Any] = {}
    __properties = ["paymentDate", "diagnostics", "cashFlowLineage", "paymentAmount", "paymentCcy", "resultValueType"]

    @validator('result_value_type')
    def result_value_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('ResultValue', 'ResultValueDictionary', 'ResultValue0D', 'ResultValueDecimal', 'ResultValueInt', 'ResultValueString', 'ResultValueBool', 'ResultValueCurrency', 'CashFlowValue', 'CashFlowValueSet', 'ResultValueLifeCycleEventValue', 'ResultValueDateTimeOffset'):
            raise ValueError("must be one of enum values ('ResultValue', 'ResultValueDictionary', 'ResultValue0D', 'ResultValueDecimal', 'ResultValueInt', 'ResultValueString', 'ResultValueBool', 'ResultValueCurrency', 'CashFlowValue', 'CashFlowValueSet', 'ResultValueLifeCycleEventValue', 'ResultValueDateTimeOffset')")
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
    def from_json(cls, json_str: str) -> CashFlowValueAllOf:
        """Create an instance of CashFlowValueAllOf from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of diagnostics
        if self.diagnostics:
            _dict['diagnostics'] = self.diagnostics.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cash_flow_lineage
        if self.cash_flow_lineage:
            _dict['cashFlowLineage'] = self.cash_flow_lineage.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CashFlowValueAllOf:
        """Create an instance of CashFlowValueAllOf from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CashFlowValueAllOf.parse_obj(obj)

        _obj = CashFlowValueAllOf.parse_obj({
            "payment_date": obj.get("paymentDate"),
            "diagnostics": ResultValueDictionary.from_dict(obj.get("diagnostics")) if obj.get("diagnostics") is not None else None,
            "cash_flow_lineage": CashFlowLineage.from_dict(obj.get("cashFlowLineage")) if obj.get("cashFlowLineage") is not None else None,
            "payment_amount": obj.get("paymentAmount"),
            "payment_ccy": obj.get("paymentCcy"),
            "result_value_type": obj.get("resultValueType")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

