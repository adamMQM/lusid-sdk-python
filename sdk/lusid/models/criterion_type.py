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





class CriterionType(str, Enum):
    """
    Discriminator for MatchCriterion.
    """

    """
    allowed enum values
    """
    PROPERTYVALUEEQUALS = 'PropertyValueEquals'
    PROPERTYVALUEIN = 'PropertyValueIn'
    SUBHOLDINGKEYVALUEEQUALS = 'SubHoldingKeyValueEquals'

    @classmethod
    def from_json(cls, json_str: str) -> CriterionType:
        """Create an instance of CriterionType from a JSON string"""
        return CriterionType(json.loads(json_str))


