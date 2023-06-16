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



from pydantic import BaseModel, Field, constr
from lusid.models.block import Block
from lusid.models.order_graph_block_allocation_synopsis import OrderGraphBlockAllocationSynopsis
from lusid.models.order_graph_block_execution_synopsis import OrderGraphBlockExecutionSynopsis
from lusid.models.order_graph_block_order_synopsis import OrderGraphBlockOrderSynopsis
from lusid.models.order_graph_block_placement_synopsis import OrderGraphBlockPlacementSynopsis

class OrderGraphBlock(BaseModel):
    """
    OrderGraphBlock
    """
    block: Block = Field(...)
    ordered: OrderGraphBlockOrderSynopsis = Field(...)
    placed: OrderGraphBlockPlacementSynopsis = Field(...)
    executed: OrderGraphBlockExecutionSynopsis = Field(...)
    allocated: OrderGraphBlockAllocationSynopsis = Field(...)
    derived_state: constr(strict=True, min_length=1) = Field(..., alias="derivedState", description="A simple description of the overall state of a block.")
    derived_compliance_state: constr(strict=True, min_length=1) = Field(..., alias="derivedComplianceState", description="The overall compliance state of a block, derived from the block's orders. Possible values are 'Pending', 'Failed', 'Manually approved' and 'Passed'.")
    __properties = ["block", "ordered", "placed", "executed", "allocated", "derivedState", "derivedComplianceState"]

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
    def from_json(cls, json_str: str) -> OrderGraphBlock:
        """Create an instance of OrderGraphBlock from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of block
        if self.block:
            _dict['block'] = self.block.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ordered
        if self.ordered:
            _dict['ordered'] = self.ordered.to_dict()
        # override the default output from pydantic by calling `to_dict()` of placed
        if self.placed:
            _dict['placed'] = self.placed.to_dict()
        # override the default output from pydantic by calling `to_dict()` of executed
        if self.executed:
            _dict['executed'] = self.executed.to_dict()
        # override the default output from pydantic by calling `to_dict()` of allocated
        if self.allocated:
            _dict['allocated'] = self.allocated.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OrderGraphBlock:
        """Create an instance of OrderGraphBlock from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OrderGraphBlock.parse_obj(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in OrderGraphBlock) in the input: " + obj)

        _obj = OrderGraphBlock.parse_obj({
            "block": Block.from_dict(obj.get("block")) if obj.get("block") is not None else None,
            "ordered": OrderGraphBlockOrderSynopsis.from_dict(obj.get("ordered")) if obj.get("ordered") is not None else None,
            "placed": OrderGraphBlockPlacementSynopsis.from_dict(obj.get("placed")) if obj.get("placed") is not None else None,
            "executed": OrderGraphBlockExecutionSynopsis.from_dict(obj.get("executed")) if obj.get("executed") is not None else None,
            "allocated": OrderGraphBlockAllocationSynopsis.from_dict(obj.get("allocated")) if obj.get("allocated") is not None else None,
            "derived_state": obj.get("derivedState"),
            "derived_compliance_state": obj.get("derivedComplianceState")
        })
        return _obj

