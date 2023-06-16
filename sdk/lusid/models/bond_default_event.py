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
from typing import Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, constr, validator
from lusid.models.instrument_event import InstrumentEvent

class BondDefaultEvent(InstrumentEvent):
    """
    Indicates when an issuer has defaulted on an obligation due to technical default, missed payments, or bankruptcy filing.
    """
    amount: Union[StrictFloat, StrictInt] = Field(..., description="Percentage or amount of each share held to be given to shareholders.")
    coupon_paid_date: datetime = Field(..., alias="couponPaidDate", description="Date that the missed coupon is paid if payment is made within grace period.")
    default_status: constr(strict=True, min_length=1) = Field(..., alias="defaultStatus", description="The status of the bond default (i.e., technical or default)    Supported string (enumeration) values are: [Technical, Default].")
    default_type: constr(strict=True, min_length=1) = Field(..., alias="defaultType", description="The type of the default. (coupon payment, principal payment, covenant ...)    Supported string (enumeration) values are: [CouponPayment, CouponAndPrincipalPayment, PrincipalPayment, Covenant, Bankruptcy, BuyBackOption].")
    grace_end_date: datetime = Field(..., alias="graceEndDate", description="Date the grace period for making coupon payment ends.")
    payment_date: datetime = Field(..., alias="paymentDate", description="The date the coupon payment was missed.")
    instrument_event_type: StrictStr = Field(..., alias="instrumentEventType", description="The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent")
    additional_properties: Dict[str, Any] = {}
    __properties = ["instrumentEventType", "amount", "couponPaidDate", "defaultStatus", "defaultType", "graceEndDate", "paymentDate"]

    @validator('instrument_event_type')
    def instrument_event_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('TransitionEvent', 'InformationalEvent', 'OpenEvent', 'CloseEvent', 'StockSplitEvent', 'BondDefaultEvent', 'CashDividendEvent', 'AmortisationEvent', 'CashFlowEvent', 'ExerciseEvent', 'ResetEvent', 'TriggerEvent', 'RawVendorEvent', 'InformationalErrorEvent'):
            raise ValueError("must be one of enum values ('TransitionEvent', 'InformationalEvent', 'OpenEvent', 'CloseEvent', 'StockSplitEvent', 'BondDefaultEvent', 'CashDividendEvent', 'AmortisationEvent', 'CashFlowEvent', 'ExerciseEvent', 'ResetEvent', 'TriggerEvent', 'RawVendorEvent', 'InformationalErrorEvent')")
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
    def from_json(cls, json_str: str) -> BondDefaultEvent:
        """Create an instance of BondDefaultEvent from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BondDefaultEvent:
        """Create an instance of BondDefaultEvent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BondDefaultEvent.parse_obj(obj)

        _obj = BondDefaultEvent.parse_obj({
            "instrument_event_type": obj.get("instrumentEventType"),
            "amount": obj.get("amount"),
            "coupon_paid_date": obj.get("couponPaidDate"),
            "default_status": obj.get("defaultStatus"),
            "default_type": obj.get("defaultType"),
            "grace_end_date": obj.get("graceEndDate"),
            "payment_date": obj.get("paymentDate")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

