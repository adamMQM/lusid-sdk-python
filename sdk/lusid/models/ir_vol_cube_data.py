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
from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist, constr, validator
from lusid.models.complex_market_data import ComplexMarketData
from lusid.models.lusid_instrument import LusidInstrument
from lusid.models.market_quote import MarketQuote

class IrVolCubeData(ComplexMarketData):
    """
    Market Data required to build a volatility cube for swaption pricing,  represented by a list of instruments and corresponding market quotes
    """
    base_date: datetime = Field(..., alias="baseDate", description="Base date of the cube - this is the start date of the swaptions on the cube.")
    instruments: conlist(LusidInstrument) = Field(..., description="Retrieve the set of instruments that define the cube.")
    quotes: conlist(MarketQuote) = Field(..., description="Access the set of quotes that define the cube.")
    lineage: Optional[constr(strict=True, max_length=1024, min_length=0)] = Field(None, description="Description of the complex market data's lineage e.g. 'FundAccountant_GreenQuality'.")
    market_data_type: StrictStr = Field(..., alias="marketDataType", description="The available values are: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData, EquityCurveByPricesData")
    additional_properties: Dict[str, Any] = {}
    __properties = ["marketDataType", "baseDate", "instruments", "quotes", "lineage"]

    @validator('market_data_type')
    def market_data_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('DiscountFactorCurveData', 'EquityVolSurfaceData', 'FxVolSurfaceData', 'IrVolCubeData', 'OpaqueMarketData', 'YieldCurveData', 'FxForwardCurveData', 'FxForwardPipsCurveData', 'FxForwardTenorCurveData', 'FxForwardTenorPipsCurveData', 'FxForwardCurveByQuoteReference', 'CreditSpreadCurveData', 'EquityCurveByPricesData'):
            raise ValueError("must be one of enum values ('DiscountFactorCurveData', 'EquityVolSurfaceData', 'FxVolSurfaceData', 'IrVolCubeData', 'OpaqueMarketData', 'YieldCurveData', 'FxForwardCurveData', 'FxForwardPipsCurveData', 'FxForwardTenorCurveData', 'FxForwardTenorPipsCurveData', 'FxForwardCurveByQuoteReference', 'CreditSpreadCurveData', 'EquityCurveByPricesData')")
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
    def from_json(cls, json_str: str) -> IrVolCubeData:
        """Create an instance of IrVolCubeData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in instruments (list)
        _items = []
        if self.instruments:
            for _item in self.instruments:
                if _item:
                    _items.append(_item.to_dict())
            _dict['instruments'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in quotes (list)
        _items = []
        if self.quotes:
            for _item in self.quotes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['quotes'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if lineage (nullable) is None
        # and __fields_set__ contains the field
        if self.lineage is None and "lineage" in self.__fields_set__:
            _dict['lineage'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> IrVolCubeData:
        """Create an instance of IrVolCubeData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return IrVolCubeData.parse_obj(obj)

        _obj = IrVolCubeData.parse_obj({
            "market_data_type": obj.get("marketDataType"),
            "base_date": obj.get("baseDate"),
            "instruments": [LusidInstrument.from_dict(_item) for _item in obj.get("instruments")] if obj.get("instruments") is not None else None,
            "quotes": [MarketQuote.from_dict(_item) for _item in obj.get("quotes")] if obj.get("quotes") is not None else None,
            "lineage": obj.get("lineage")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

