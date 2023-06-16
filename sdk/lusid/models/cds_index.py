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
from typing import Dict, Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, validator
from lusid.models.basket import Basket
from lusid.models.cds_flow_conventions import CdsFlowConventions
from lusid.models.flow_convention_name import FlowConventionName
from lusid.models.lusid_instrument import LusidInstrument

class CdsIndex(LusidInstrument):
    """
    LUSID representation of a Credit Default Swap Index (CDX).
    """
    start_date: datetime = Field(..., alias="startDate", description="The start date of the instrument. This is normally synonymous with the trade-date.")
    maturity_date: datetime = Field(..., alias="maturityDate", description="The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.  For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as  Constant Maturity Swaps (CMS) often have sensitivities to rates that may well be observed or set prior to the maturity date, but refer to a termination date beyond it.")
    flow_conventions: Optional[CdsFlowConventions] = Field(None, alias="flowConventions")
    coupon_rate: Union[StrictFloat, StrictInt] = Field(..., alias="couponRate", description="The coupon rate paid on each payment date of the premium leg as a fraction of 100 percent, e.g. \"0.05\" meaning 500 basis points or 5%.  For a standard corporate CDS (North American) this must be either 100bps or 500bps.")
    identifiers: Dict[str, StrictStr] = Field(..., description="External market codes and identifiers for the cds index, e.g. a RED code, BBG ID or ICE code.")
    basket: Basket = Field(...)
    convention_name: Optional[FlowConventionName] = Field(None, alias="conventionName")
    notional: Union[StrictFloat, StrictInt] = Field(..., description="The notional quantity that applies to both the premium and protection legs.")
    instrument_type: StrictStr = Field(..., alias="instrumentType", description="The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan")
    additional_properties: Dict[str, Any] = {}
    __properties = ["instrumentType", "startDate", "maturityDate", "flowConventions", "couponRate", "identifiers", "basket", "conventionName", "notional"]

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
    def from_json(cls, json_str: str) -> CdsIndex:
        """Create an instance of CdsIndex from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of flow_conventions
        if self.flow_conventions:
            _dict['flowConventions'] = self.flow_conventions.to_dict()
        # override the default output from pydantic by calling `to_dict()` of basket
        if self.basket:
            _dict['basket'] = self.basket.to_dict()
        # override the default output from pydantic by calling `to_dict()` of convention_name
        if self.convention_name:
            _dict['conventionName'] = self.convention_name.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CdsIndex:
        """Create an instance of CdsIndex from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CdsIndex.parse_obj(obj)

        _obj = CdsIndex.parse_obj({
            "instrument_type": obj.get("instrumentType"),
            "start_date": obj.get("startDate"),
            "maturity_date": obj.get("maturityDate"),
            "flow_conventions": CdsFlowConventions.from_dict(obj.get("flowConventions")) if obj.get("flowConventions") is not None else None,
            "coupon_rate": obj.get("couponRate"),
            "identifiers": obj.get("identifiers"),
            "basket": Basket.from_dict(obj.get("basket")) if obj.get("basket") is not None else None,
            "convention_name": FlowConventionName.from_dict(obj.get("conventionName")) if obj.get("conventionName") is not None else None,
            "notional": obj.get("notional")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

