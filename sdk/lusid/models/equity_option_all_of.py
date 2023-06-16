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
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, constr, validator
from lusid.models.premium import Premium

class EquityOptionAllOf(BaseModel):
    """
    EquityOptionAllOf
    """
    start_date: datetime = Field(..., alias="startDate", description="The start date of the instrument. This is normally synonymous with the trade-date.")
    option_maturity_date: datetime = Field(..., alias="optionMaturityDate", description="The maturity date of the option.")
    option_settlement_date: datetime = Field(..., alias="optionSettlementDate", description="The settlement date of the option.")
    delivery_type: constr(strict=True, min_length=1) = Field(..., alias="deliveryType", description="Is the option cash settled or physical delivery of option    Supported string (enumeration) values are: [Cash, Physical].")
    option_type: constr(strict=True, min_length=1) = Field(..., alias="optionType", description="Type of optionality for the option    Supported string (enumeration) values are: [Call, Put].")
    strike: Union[StrictFloat, StrictInt] = Field(..., description="The strike of the option.")
    dom_ccy: StrictStr = Field(..., alias="domCcy", description="The domestic currency of the instrument.")
    underlying_identifier: constr(strict=True, min_length=1) = Field(..., alias="underlyingIdentifier", description="The market identifier type of the underlying code, e.g RIC.    Supported string (enumeration) values are: [LusidInstrumentId, Isin, Sedol, Cusip, ClientInternal, Figi, RIC, QuotePermId, REDCode, BBGId, ICECode].")
    code: constr(strict=True, min_length=1) = Field(..., description="The identifying code for the equity underlying, e.g. 'IBM.N'.")
    equity_option_type: Optional[StrictStr] = Field(None, alias="equityOptionType", description="Equity option types. E.g. Vanilla (default), RightsIssue, Warrant.    Supported string (enumeration) values are: [Vanilla, RightsIssue, Warrant].")
    number_of_shares: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="numberOfShares", description="The amount of shares to exchange if the option is exercised.")
    premium: Optional[Premium] = None
    exercise_type: Optional[StrictStr] = Field(None, alias="exerciseType", description="Type of optionality that is present; European, American.    Supported string (enumeration) values are: [European, American].")
    instrument_type: StrictStr = Field(..., alias="instrumentType", description="The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan")
    additional_properties: Dict[str, Any] = {}
    __properties = ["startDate", "optionMaturityDate", "optionSettlementDate", "deliveryType", "optionType", "strike", "domCcy", "underlyingIdentifier", "code", "equityOptionType", "numberOfShares", "premium", "exerciseType", "instrumentType"]

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
    def from_json(cls, json_str: str) -> EquityOptionAllOf:
        """Create an instance of EquityOptionAllOf from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of premium
        if self.premium:
            _dict['premium'] = self.premium.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if equity_option_type (nullable) is None
        # and __fields_set__ contains the field
        if self.equity_option_type is None and "equity_option_type" in self.__fields_set__:
            _dict['equityOptionType'] = None

        # set to None if number_of_shares (nullable) is None
        # and __fields_set__ contains the field
        if self.number_of_shares is None and "number_of_shares" in self.__fields_set__:
            _dict['numberOfShares'] = None

        # set to None if exercise_type (nullable) is None
        # and __fields_set__ contains the field
        if self.exercise_type is None and "exercise_type" in self.__fields_set__:
            _dict['exerciseType'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EquityOptionAllOf:
        """Create an instance of EquityOptionAllOf from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EquityOptionAllOf.parse_obj(obj)

        _obj = EquityOptionAllOf.parse_obj({
            "start_date": obj.get("startDate"),
            "option_maturity_date": obj.get("optionMaturityDate"),
            "option_settlement_date": obj.get("optionSettlementDate"),
            "delivery_type": obj.get("deliveryType"),
            "option_type": obj.get("optionType"),
            "strike": obj.get("strike"),
            "dom_ccy": obj.get("domCcy"),
            "underlying_identifier": obj.get("underlyingIdentifier"),
            "code": obj.get("code"),
            "equity_option_type": obj.get("equityOptionType"),
            "number_of_shares": obj.get("numberOfShares"),
            "premium": Premium.from_dict(obj.get("premium")) if obj.get("premium") is not None else None,
            "exercise_type": obj.get("exerciseType"),
            "instrument_type": obj.get("instrumentType")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

