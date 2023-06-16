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
from typing import Dict, List, Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, conlist, constr
from lusid.models.link import Link
from lusid.models.resource_id import ResourceId

class InstrumentCashFlow(BaseModel):
    """
    The details for the cashflow associated with an instrument from a given portfolio.
    """
    payment_date: datetime = Field(..., alias="paymentDate", description="The date at which the given cash flow is due to be paid (SettlementDate is used somewhat interchangeably with PaymentDate.)")
    amount: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="The quantity (amount) that will be paid. Note that this can be empty if the payment is in the future and a model is used that cannot estimate it.")
    currency: StrictStr = Field(..., description="The payment currency of the cash flow.")
    source_portfolio_id: ResourceId = Field(..., alias="sourcePortfolioId")
    source_transaction_id: constr(strict=True, min_length=1) = Field(..., alias="sourceTransactionId", description="The identifier for the parent transaction on the instrument that will pay/receive this cash flow.")
    source_instrument_scope: constr(strict=True, min_length=1) = Field(..., alias="sourceInstrumentScope", description="The unqiue Lusid Instrument Id (LUID) of the instrument that the holding is in.")
    source_instrument_id: constr(strict=True, min_length=1) = Field(..., alias="sourceInstrumentId", description="The unqiue Lusid Instrument Id (LUID) of the instrument that the holding is in.")
    diagnostics: Dict[str, StrictStr] = Field(..., description="Whilst a cash flow is defined by an (amount,ccy) pair and the date it is paid on there is additional information required for diagnostics. This includes a range of information and can be empty in the case of a simple cash quantity or where further information is not available. Typical information includes items such as reset dates, RIC, accrual start/end, number of days and curve data.")
    links: Optional[conlist(Link)] = None
    __properties = ["paymentDate", "amount", "currency", "sourcePortfolioId", "sourceTransactionId", "sourceInstrumentScope", "sourceInstrumentId", "diagnostics", "links"]

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
    def from_json(cls, json_str: str) -> InstrumentCashFlow:
        """Create an instance of InstrumentCashFlow from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of source_portfolio_id
        if self.source_portfolio_id:
            _dict['sourcePortfolioId'] = self.source_portfolio_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item in self.links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['links'] = _items
        # set to None if amount (nullable) is None
        # and __fields_set__ contains the field
        if self.amount is None and "amount" in self.__fields_set__:
            _dict['amount'] = None

        # set to None if links (nullable) is None
        # and __fields_set__ contains the field
        if self.links is None and "links" in self.__fields_set__:
            _dict['links'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> InstrumentCashFlow:
        """Create an instance of InstrumentCashFlow from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return InstrumentCashFlow.parse_obj(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in InstrumentCashFlow) in the input: " + obj)

        _obj = InstrumentCashFlow.parse_obj({
            "payment_date": obj.get("paymentDate"),
            "amount": obj.get("amount"),
            "currency": obj.get("currency"),
            "source_portfolio_id": ResourceId.from_dict(obj.get("sourcePortfolioId")) if obj.get("sourcePortfolioId") is not None else None,
            "source_transaction_id": obj.get("sourceTransactionId"),
            "source_instrument_scope": obj.get("sourceInstrumentScope"),
            "source_instrument_id": obj.get("sourceInstrumentId"),
            "diagnostics": obj.get("diagnostics"),
            "links": [Link.from_dict(_item) for _item in obj.get("links")] if obj.get("links") is not None else None
        })
        return _obj

