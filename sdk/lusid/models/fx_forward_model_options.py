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



from pydantic import BaseModel, Field, StrictBool, StrictStr, validator
from lusid.models.model_options import ModelOptions

class FxForwardModelOptions(ModelOptions):
    """
    FxForwardModelOptions
    """
    forward_rate_observable_type: StrictStr = Field(..., alias="forwardRateObservableType", description="The available values are: ForwardPoints, ForwardRate, RatesCurve, FxForwardCurve, Invalid")
    discounting_method: StrictStr = Field(..., alias="discountingMethod", description="The available values are: Standard, ConstantTimeValueOfMoney, Invalid")
    convert_to_report_ccy: StrictBool = Field(..., alias="convertToReportCcy", description="Convert all FX flows to the report currency  By setting this all FX forwards will be priced using Forward Curves that have Report Currency as the base.")
    model_options_type: StrictStr = Field(..., alias="modelOptionsType", description="The available values are: Invalid, OpaqueModelOptions, EmptyModelOptions, IndexModelOptions, FxForwardModelOptions, FundingLegModelOptions, EquityModelOptions")
    additional_properties: Dict[str, Any] = {}
    __properties = ["modelOptionsType", "forwardRateObservableType", "discountingMethod", "convertToReportCcy"]

    @validator('forward_rate_observable_type')
    def forward_rate_observable_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('ForwardPoints', 'ForwardRate', 'RatesCurve', 'FxForwardCurve', 'Invalid'):
            raise ValueError("must be one of enum values ('ForwardPoints', 'ForwardRate', 'RatesCurve', 'FxForwardCurve', 'Invalid')")
        return value

    @validator('discounting_method')
    def discounting_method_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('Standard', 'ConstantTimeValueOfMoney', 'Invalid'):
            raise ValueError("must be one of enum values ('Standard', 'ConstantTimeValueOfMoney', 'Invalid')")
        return value

    @validator('model_options_type')
    def model_options_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('Invalid', 'OpaqueModelOptions', 'EmptyModelOptions', 'IndexModelOptions', 'FxForwardModelOptions', 'FundingLegModelOptions', 'EquityModelOptions'):
            raise ValueError("must be one of enum values ('Invalid', 'OpaqueModelOptions', 'EmptyModelOptions', 'IndexModelOptions', 'FxForwardModelOptions', 'FundingLegModelOptions', 'EquityModelOptions')")
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
    def from_json(cls, json_str: str) -> FxForwardModelOptions:
        """Create an instance of FxForwardModelOptions from a JSON string"""
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
    def from_dict(cls, obj: dict) -> FxForwardModelOptions:
        """Create an instance of FxForwardModelOptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FxForwardModelOptions.parse_obj(obj)

        _obj = FxForwardModelOptions.parse_obj({
            "model_options_type": obj.get("modelOptionsType"),
            "forward_rate_observable_type": obj.get("forwardRateObservableType"),
            "discounting_method": obj.get("discountingMethod"),
            "convert_to_report_ccy": obj.get("convertToReportCcy")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

