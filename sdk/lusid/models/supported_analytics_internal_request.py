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
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist

class SupportedAnalyticsInternalRequest(BaseModel):
    """
    The request body for the SupportedAnalyticsInternal endpoint
    """
    include_all_addresses: StrictBool = Field(..., alias="includeAllAddresses", description="If true, then we show every possible address key, otherwise we show the address keys specified in addresses array.")
    addresses: Optional[conlist(StrictStr)] = Field(None, description="Address keys specified here will be included in the response to the call, which will include details on whether those keys are supported.")
    group_by: conlist(StrictStr) = Field(..., alias="groupBy", description="The address keys to group by.")
    show_test_counts: Optional[StrictBool] = Field(None, alias="showTestCounts", description="If true, returns an integer matrix showing test counts for each address.  If false, masks to a boolean matrix representing whether an address is supported or unsupported.")
    __properties = ["includeAllAddresses", "addresses", "groupBy", "showTestCounts"]

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
    def from_json(cls, json_str: str) -> SupportedAnalyticsInternalRequest:
        """Create an instance of SupportedAnalyticsInternalRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if addresses (nullable) is None
        # and __fields_set__ contains the field
        if self.addresses is None and "addresses" in self.__fields_set__:
            _dict['addresses'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SupportedAnalyticsInternalRequest:
        """Create an instance of SupportedAnalyticsInternalRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SupportedAnalyticsInternalRequest.parse_obj(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in SupportedAnalyticsInternalRequest) in the input: " + obj)

        _obj = SupportedAnalyticsInternalRequest.parse_obj({
            "include_all_addresses": obj.get("includeAllAddresses"),
            "addresses": obj.get("addresses"),
            "group_by": obj.get("groupBy"),
            "show_test_counts": obj.get("showTestCounts")
        })
        return _obj

