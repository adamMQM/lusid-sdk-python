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
from lusid.models.flow_conventions import FlowConventions

class TermDepositAllOf(BaseModel):
    """
    TermDepositAllOf
    """
    start_date: datetime = Field(..., alias="startDate", description="The start date of the instrument. This is normally synonymous with the trade-date.")
    maturity_date: datetime = Field(..., alias="maturityDate", description="The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.  For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as  Constant Maturity Swaps (CMS) often have sensitivities to rates that may well be observed or set prior to the maturity date, but refer to a termination date beyond it.")
    contract_size: Union[StrictFloat, StrictInt] = Field(..., alias="contractSize", description="With an OTC we have the problem of multiple ways of booking a quantity.              e.g.              If buying a swap do you have a holding of size 1 of 100,000,000 notional swap or a holding of 100,000,000 size of 1 notional swap, or any combination that multiplies to 10^8.              When you get for a price for a 'unit swap' what do you mean? The definition must be consistent across all quotes. This includes bonds which have a face value and              fx-forwards which often trade in standard contract sizes. When we look up a price, and there are no units, we are assuming it is a price for a contract size of 1.              The logical effect of this is that              instrument clean price = contract size * quoted unit price              holding clean price    = holding quantity * instrument clean price = holding quantity * contract size * quoted unit price              In calculating accrued interest the same should hold.              NB: The real problem is that people store \"prices\" without complete units. Everything should really be \"x ccy for n units\". Where the n is implicit the above has to hold.")
    flow_convention: FlowConventions = Field(..., alias="flowConvention")
    rate: Union[StrictFloat, StrictInt] = Field(..., description="The fixed rate for the term deposit. Specified as a decimal, e.g 0.03 is meant to be 3% interest")
    dom_ccy: Optional[StrictStr] = Field(None, alias="domCcy", description="DomCcy of the TermDeposit. If provided, must match the currency of FlowConvention.")
    instrument_type: StrictStr = Field(..., alias="instrumentType", description="The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan")
    additional_properties: Dict[str, Any] = {}
    __properties = ["startDate", "maturityDate", "contractSize", "flowConvention", "rate", "domCcy", "instrumentType"]

    @validator('instrument_type')
    def instrument_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('QuotedSecurity', 'InterestRateSwap', 'FxForward', 'Future', 'ExoticInstrument', 'FxOption', 'CreditDefaultSwap', 'InterestRateSwaption', 'Bond', 'EquityOption', 'FixedLeg', 'FloatingLeg', 'BespokeCashFlowsLeg', 'Unknown', 'TermDeposit', 'ContractForDifference', 'EquitySwap', 'CashPerpetual', 'CapFloor', 'CashSettled', 'CdsIndex', 'Basket', 'FundingLeg', 'FxSwap', 'ForwardRateAgreement', 'SimpleInstrument', 'Repo', 'Equity', 'ExchangeTradedOption', 'ReferenceInstrument', 'ComplexBond', 'InflationLinkedBond', 'InflationSwap', 'SimpleCashFlowLoan'):
            raise ValueError("must be one of enum values ('QuotedSecurity', 'InterestRateSwap', 'FxForward', 'Future', 'ExoticInstrument', 'FxOption', 'CreditDefaultSwap', 'InterestRateSwaption', 'Bond', 'EquityOption', 'FixedLeg', 'FloatingLeg', 'BespokeCashFlowsLeg', 'Unknown', 'TermDeposit', 'ContractForDifference', 'EquitySwap', 'CashPerpetual', 'CapFloor', 'CashSettled', 'CdsIndex', 'Basket', 'FundingLeg', 'FxSwap', 'ForwardRateAgreement', 'SimpleInstrument', 'Repo', 'Equity', 'ExchangeTradedOption', 'ReferenceInstrument', 'ComplexBond', 'InflationLinkedBond', 'InflationSwap', 'SimpleCashFlowLoan')")
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
    def from_json(cls, json_str: str) -> TermDepositAllOf:
        """Create an instance of TermDepositAllOf from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of flow_convention
        if self.flow_convention:
            _dict['flowConvention'] = self.flow_convention.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if dom_ccy (nullable) is None
        # and __fields_set__ contains the field
        if self.dom_ccy is None and "dom_ccy" in self.__fields_set__:
            _dict['domCcy'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TermDepositAllOf:
        """Create an instance of TermDepositAllOf from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TermDepositAllOf.parse_obj(obj)

        _obj = TermDepositAllOf.parse_obj({
            "start_date": obj.get("startDate"),
            "maturity_date": obj.get("maturityDate"),
            "contract_size": obj.get("contractSize"),
            "flow_convention": FlowConventions.from_dict(obj.get("flowConvention")) if obj.get("flowConvention") is not None else None,
            "rate": obj.get("rate"),
            "dom_ccy": obj.get("domCcy"),
            "instrument_type": obj.get("instrumentType")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

