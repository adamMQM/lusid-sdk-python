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


from typing import List, Optional
from pydantic import BaseModel, Field, conlist
from lusid.models.market_context_suppliers import MarketContextSuppliers
from lusid.models.market_data_key_rule import MarketDataKeyRule
from lusid.models.market_data_specific_rule import MarketDataSpecificRule
from lusid.models.market_options import MarketOptions

class MarketContext(BaseModel):
    """
    Market context node. This defines how LUSID processes parts of a request that require resolution of market data such as instrument prices or  Fx rates. It controls where the data is loaded from and which sources take precedence.
    """
    market_rules: Optional[conlist(MarketDataKeyRule)] = Field(None, alias="marketRules", description="The set of rules that define how to resolve particular use cases. These can be relatively general or specific in nature.  Nominally any number are possible and will be processed in order where applicable. However, there is evidently a potential  for increased computational cost where many rules must be applied to resolve data. Ensuring that portfolios are structured in  such a way as to reduce the number of rules required is therefore sensible.")
    suppliers: Optional[MarketContextSuppliers] = None
    options: Optional[MarketOptions] = None
    specific_rules: Optional[conlist(MarketDataSpecificRule)] = Field(None, alias="specificRules", description="Extends market data key rules to be able to catch dependencies depending on where the dependency comes from, as opposed to what the dependency is asking for.  Using two specific rules, one could instruct rates curves requested by bonds to be retrieved from a different scope than rates curves requested by swaps.  WARNING: The use of specific rules impacts performance. Where possible, one should use MarketDataKeyRules only.")
    __properties = ["marketRules", "suppliers", "options", "specificRules"]

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
    def from_json(cls, json_str: str) -> MarketContext:
        """Create an instance of MarketContext from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in market_rules (list)
        _items = []
        if self.market_rules:
            for _item in self.market_rules:
                if _item:
                    _items.append(_item.to_dict())
            _dict['marketRules'] = _items
        # override the default output from pydantic by calling `to_dict()` of suppliers
        if self.suppliers:
            _dict['suppliers'] = self.suppliers.to_dict()
        # override the default output from pydantic by calling `to_dict()` of options
        if self.options:
            _dict['options'] = self.options.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in specific_rules (list)
        _items = []
        if self.specific_rules:
            for _item in self.specific_rules:
                if _item:
                    _items.append(_item.to_dict())
            _dict['specificRules'] = _items
        # set to None if market_rules (nullable) is None
        # and __fields_set__ contains the field
        if self.market_rules is None and "market_rules" in self.__fields_set__:
            _dict['marketRules'] = None

        # set to None if suppliers (nullable) is None
        # and __fields_set__ contains the field
        if self.suppliers is None and "suppliers" in self.__fields_set__:
            _dict['suppliers'] = None

        # set to None if specific_rules (nullable) is None
        # and __fields_set__ contains the field
        if self.specific_rules is None and "specific_rules" in self.__fields_set__:
            _dict['specificRules'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MarketContext:
        """Create an instance of MarketContext from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MarketContext.parse_obj(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in MarketContext) in the input: " + obj)

        _obj = MarketContext.parse_obj({
            "market_rules": [MarketDataKeyRule.from_dict(_item) for _item in obj.get("marketRules")] if obj.get("marketRules") is not None else None,
            "suppliers": MarketContextSuppliers.from_dict(obj.get("suppliers")) if obj.get("suppliers") is not None else None,
            "options": MarketOptions.from_dict(obj.get("options")) if obj.get("options") is not None else None,
            "specific_rules": [MarketDataSpecificRule.from_dict(_item) for _item in obj.get("specificRules")] if obj.get("specificRules") is not None else None
        })
        return _obj

