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





class ResultKeyRuleType(str, Enum):
    """
    ResultKeyRuleType
    """

    """
    allowed enum values
    """
    INVALID = 'Invalid'
    RESULTDATAKEYRULE = 'ResultDataKeyRule'
    PORTFOLIORESULTDATAKEYRULE = 'PortfolioResultDataKeyRule'

    @classmethod
    def from_json(cls, json_str: str) -> ResultKeyRuleType:
        """Create an instance of ResultKeyRuleType from a JSON string"""
        return ResultKeyRuleType(json.loads(json_str))


