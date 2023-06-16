# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    Contact: info@finbourne.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class EconomicDependencyType(str, Enum):
    """
    Discriminator for EconomicDependency.
    """

    """
    allowed enum values
    """
    OPAQUEDEPENDENCY = 'OpaqueDependency'
    CASHDEPENDENCY = 'CashDependency'
    DISCOUNTINGDEPENDENCY = 'DiscountingDependency'
    EQUITYCURVEDEPENDENCY = 'EquityCurveDependency'
    EQUITYVOLDEPENDENCY = 'EquityVolDependency'
    FXDEPENDENCY = 'FxDependency'
    FXFORWARDSDEPENDENCY = 'FxForwardsDependency'
    FXVOLDEPENDENCY = 'FxVolDependency'
    INDEXPROJECTIONDEPENDENCY = 'IndexProjectionDependency'
    IRVOLDEPENDENCY = 'IrVolDependency'
    QUOTEDEPENDENCY = 'QuoteDependency'
    VENDOR = 'Vendor'

    @classmethod
    def from_json(cls, json_str: str) -> EconomicDependencyType:
        """Create an instance of EconomicDependencyType from a JSON string"""
        return EconomicDependencyType(json.loads(json_str))


