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
from pydantic import BaseModel, Field, StrictFloat, StrictInt
from lusid.models.currency_and_amount import CurrencyAndAmount

class TargetTaxLotRequest(BaseModel):
    """
    TargetTaxLotRequest
    """
    units: Union[StrictFloat, StrictInt] = Field(..., description="The number of units of the instrument in this tax-lot.")
    cost: Optional[CurrencyAndAmount] = None
    portfolio_cost: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="portfolioCost", description="The total cost of the tax-lot in the transaction portfolio's base currency.")
    price: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="The purchase price of each unit of the instrument held in this tax-lot. This forms part of the unique key required for multiple tax-lots.")
    purchase_date: Optional[datetime] = Field(None, alias="purchaseDate", description="The purchase date of this tax-lot. This forms part of the unique key required for multiple tax-lots.")
    settlement_date: Optional[datetime] = Field(None, alias="settlementDate", description="The settlement date of the tax-lot's opening transaction.")
    __properties = ["units", "cost", "portfolioCost", "price", "purchaseDate", "settlementDate"]

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
    def from_json(cls, json_str: str) -> TargetTaxLotRequest:
        """Create an instance of TargetTaxLotRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of cost
        if self.cost:
            _dict['cost'] = self.cost.to_dict()
        # set to None if portfolio_cost (nullable) is None
        # and __fields_set__ contains the field
        if self.portfolio_cost is None and "portfolio_cost" in self.__fields_set__:
            _dict['portfolioCost'] = None

        # set to None if price (nullable) is None
        # and __fields_set__ contains the field
        if self.price is None and "price" in self.__fields_set__:
            _dict['price'] = None

        # set to None if purchase_date (nullable) is None
        # and __fields_set__ contains the field
        if self.purchase_date is None and "purchase_date" in self.__fields_set__:
            _dict['purchaseDate'] = None

        # set to None if settlement_date (nullable) is None
        # and __fields_set__ contains the field
        if self.settlement_date is None and "settlement_date" in self.__fields_set__:
            _dict['settlementDate'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TargetTaxLotRequest:
        """Create an instance of TargetTaxLotRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TargetTaxLotRequest.parse_obj(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in TargetTaxLotRequest) in the input: " + obj)

        _obj = TargetTaxLotRequest.parse_obj({
            "units": obj.get("units"),
            "cost": CurrencyAndAmount.from_dict(obj.get("cost")) if obj.get("cost") is not None else None,
            "portfolio_cost": obj.get("portfolioCost"),
            "price": obj.get("price"),
            "purchase_date": obj.get("purchaseDate"),
            "settlement_date": obj.get("settlementDate")
        })
        return _obj

