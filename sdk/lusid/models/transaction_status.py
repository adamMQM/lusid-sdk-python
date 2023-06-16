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





class TransactionStatus(str, Enum):
    """
    TransactionStatus
    """

    """
    allowed enum values
    """
    ACTIVE = 'Active'
    AMENDED = 'Amended'
    CANCELLED = 'Cancelled'

    @classmethod
    def from_json(cls, json_str: str) -> TransactionStatus:
        """Create an instance of TransactionStatus from a JSON string"""
        return TransactionStatus(json.loads(json_str))


