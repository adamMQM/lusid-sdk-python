# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.4862
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from lusid.configuration import Configuration


class ReconciliationBreak(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'instrument_scope': 'str',
        'instrument_uid': 'str',
        'sub_holding_keys': 'dict(str, PerpetualProperty)',
        'left_units': 'float',
        'right_units': 'float',
        'difference_units': 'float',
        'left_cost': 'CurrencyAndAmount',
        'right_cost': 'CurrencyAndAmount',
        'difference_cost': 'CurrencyAndAmount',
        'instrument_properties': 'list[ModelProperty]'
    }

    attribute_map = {
        'instrument_scope': 'instrumentScope',
        'instrument_uid': 'instrumentUid',
        'sub_holding_keys': 'subHoldingKeys',
        'left_units': 'leftUnits',
        'right_units': 'rightUnits',
        'difference_units': 'differenceUnits',
        'left_cost': 'leftCost',
        'right_cost': 'rightCost',
        'difference_cost': 'differenceCost',
        'instrument_properties': 'instrumentProperties'
    }

    required_map = {
        'instrument_scope': 'optional',
        'instrument_uid': 'required',
        'sub_holding_keys': 'required',
        'left_units': 'required',
        'right_units': 'required',
        'difference_units': 'required',
        'left_cost': 'required',
        'right_cost': 'required',
        'difference_cost': 'required',
        'instrument_properties': 'required'
    }

    def __init__(self, instrument_scope=None, instrument_uid=None, sub_holding_keys=None, left_units=None, right_units=None, difference_units=None, left_cost=None, right_cost=None, difference_cost=None, instrument_properties=None, local_vars_configuration=None):  # noqa: E501
        """ReconciliationBreak - a model defined in OpenAPI"
        
        :param instrument_scope:  The scope in which the instrument lies.
        :type instrument_scope: str
        :param instrument_uid:  Unique instrument identifier (required)
        :type instrument_uid: str
        :param sub_holding_keys:  Any other properties that comprise the Sub-Holding Key (required)
        :type sub_holding_keys: dict[str, lusid.PerpetualProperty]
        :param left_units:  Units from the left hand side (required)
        :type left_units: float
        :param right_units:  Units from the right hand side (required)
        :type right_units: float
        :param difference_units:  Difference in units (required)
        :type difference_units: float
        :param left_cost:  (required)
        :type left_cost: lusid.CurrencyAndAmount
        :param right_cost:  (required)
        :type right_cost: lusid.CurrencyAndAmount
        :param difference_cost:  (required)
        :type difference_cost: lusid.CurrencyAndAmount
        :param instrument_properties:  Additional features relating to the instrument (required)
        :type instrument_properties: list[lusid.ModelProperty]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._instrument_scope = None
        self._instrument_uid = None
        self._sub_holding_keys = None
        self._left_units = None
        self._right_units = None
        self._difference_units = None
        self._left_cost = None
        self._right_cost = None
        self._difference_cost = None
        self._instrument_properties = None
        self.discriminator = None

        self.instrument_scope = instrument_scope
        self.instrument_uid = instrument_uid
        self.sub_holding_keys = sub_holding_keys
        self.left_units = left_units
        self.right_units = right_units
        self.difference_units = difference_units
        self.left_cost = left_cost
        self.right_cost = right_cost
        self.difference_cost = difference_cost
        self.instrument_properties = instrument_properties

    @property
    def instrument_scope(self):
        """Gets the instrument_scope of this ReconciliationBreak.  # noqa: E501

        The scope in which the instrument lies.  # noqa: E501

        :return: The instrument_scope of this ReconciliationBreak.  # noqa: E501
        :rtype: str
        """
        return self._instrument_scope

    @instrument_scope.setter
    def instrument_scope(self, instrument_scope):
        """Sets the instrument_scope of this ReconciliationBreak.

        The scope in which the instrument lies.  # noqa: E501

        :param instrument_scope: The instrument_scope of this ReconciliationBreak.  # noqa: E501
        :type instrument_scope: str
        """

        self._instrument_scope = instrument_scope

    @property
    def instrument_uid(self):
        """Gets the instrument_uid of this ReconciliationBreak.  # noqa: E501

        Unique instrument identifier  # noqa: E501

        :return: The instrument_uid of this ReconciliationBreak.  # noqa: E501
        :rtype: str
        """
        return self._instrument_uid

    @instrument_uid.setter
    def instrument_uid(self, instrument_uid):
        """Sets the instrument_uid of this ReconciliationBreak.

        Unique instrument identifier  # noqa: E501

        :param instrument_uid: The instrument_uid of this ReconciliationBreak.  # noqa: E501
        :type instrument_uid: str
        """
        if self.local_vars_configuration.client_side_validation and instrument_uid is None:  # noqa: E501
            raise ValueError("Invalid value for `instrument_uid`, must not be `None`")  # noqa: E501

        self._instrument_uid = instrument_uid

    @property
    def sub_holding_keys(self):
        """Gets the sub_holding_keys of this ReconciliationBreak.  # noqa: E501

        Any other properties that comprise the Sub-Holding Key  # noqa: E501

        :return: The sub_holding_keys of this ReconciliationBreak.  # noqa: E501
        :rtype: dict[str, lusid.PerpetualProperty]
        """
        return self._sub_holding_keys

    @sub_holding_keys.setter
    def sub_holding_keys(self, sub_holding_keys):
        """Sets the sub_holding_keys of this ReconciliationBreak.

        Any other properties that comprise the Sub-Holding Key  # noqa: E501

        :param sub_holding_keys: The sub_holding_keys of this ReconciliationBreak.  # noqa: E501
        :type sub_holding_keys: dict[str, lusid.PerpetualProperty]
        """
        if self.local_vars_configuration.client_side_validation and sub_holding_keys is None:  # noqa: E501
            raise ValueError("Invalid value for `sub_holding_keys`, must not be `None`")  # noqa: E501

        self._sub_holding_keys = sub_holding_keys

    @property
    def left_units(self):
        """Gets the left_units of this ReconciliationBreak.  # noqa: E501

        Units from the left hand side  # noqa: E501

        :return: The left_units of this ReconciliationBreak.  # noqa: E501
        :rtype: float
        """
        return self._left_units

    @left_units.setter
    def left_units(self, left_units):
        """Sets the left_units of this ReconciliationBreak.

        Units from the left hand side  # noqa: E501

        :param left_units: The left_units of this ReconciliationBreak.  # noqa: E501
        :type left_units: float
        """
        if self.local_vars_configuration.client_side_validation and left_units is None:  # noqa: E501
            raise ValueError("Invalid value for `left_units`, must not be `None`")  # noqa: E501

        self._left_units = left_units

    @property
    def right_units(self):
        """Gets the right_units of this ReconciliationBreak.  # noqa: E501

        Units from the right hand side  # noqa: E501

        :return: The right_units of this ReconciliationBreak.  # noqa: E501
        :rtype: float
        """
        return self._right_units

    @right_units.setter
    def right_units(self, right_units):
        """Sets the right_units of this ReconciliationBreak.

        Units from the right hand side  # noqa: E501

        :param right_units: The right_units of this ReconciliationBreak.  # noqa: E501
        :type right_units: float
        """
        if self.local_vars_configuration.client_side_validation and right_units is None:  # noqa: E501
            raise ValueError("Invalid value for `right_units`, must not be `None`")  # noqa: E501

        self._right_units = right_units

    @property
    def difference_units(self):
        """Gets the difference_units of this ReconciliationBreak.  # noqa: E501

        Difference in units  # noqa: E501

        :return: The difference_units of this ReconciliationBreak.  # noqa: E501
        :rtype: float
        """
        return self._difference_units

    @difference_units.setter
    def difference_units(self, difference_units):
        """Sets the difference_units of this ReconciliationBreak.

        Difference in units  # noqa: E501

        :param difference_units: The difference_units of this ReconciliationBreak.  # noqa: E501
        :type difference_units: float
        """
        if self.local_vars_configuration.client_side_validation and difference_units is None:  # noqa: E501
            raise ValueError("Invalid value for `difference_units`, must not be `None`")  # noqa: E501

        self._difference_units = difference_units

    @property
    def left_cost(self):
        """Gets the left_cost of this ReconciliationBreak.  # noqa: E501


        :return: The left_cost of this ReconciliationBreak.  # noqa: E501
        :rtype: lusid.CurrencyAndAmount
        """
        return self._left_cost

    @left_cost.setter
    def left_cost(self, left_cost):
        """Sets the left_cost of this ReconciliationBreak.


        :param left_cost: The left_cost of this ReconciliationBreak.  # noqa: E501
        :type left_cost: lusid.CurrencyAndAmount
        """
        if self.local_vars_configuration.client_side_validation and left_cost is None:  # noqa: E501
            raise ValueError("Invalid value for `left_cost`, must not be `None`")  # noqa: E501

        self._left_cost = left_cost

    @property
    def right_cost(self):
        """Gets the right_cost of this ReconciliationBreak.  # noqa: E501


        :return: The right_cost of this ReconciliationBreak.  # noqa: E501
        :rtype: lusid.CurrencyAndAmount
        """
        return self._right_cost

    @right_cost.setter
    def right_cost(self, right_cost):
        """Sets the right_cost of this ReconciliationBreak.


        :param right_cost: The right_cost of this ReconciliationBreak.  # noqa: E501
        :type right_cost: lusid.CurrencyAndAmount
        """
        if self.local_vars_configuration.client_side_validation and right_cost is None:  # noqa: E501
            raise ValueError("Invalid value for `right_cost`, must not be `None`")  # noqa: E501

        self._right_cost = right_cost

    @property
    def difference_cost(self):
        """Gets the difference_cost of this ReconciliationBreak.  # noqa: E501


        :return: The difference_cost of this ReconciliationBreak.  # noqa: E501
        :rtype: lusid.CurrencyAndAmount
        """
        return self._difference_cost

    @difference_cost.setter
    def difference_cost(self, difference_cost):
        """Sets the difference_cost of this ReconciliationBreak.


        :param difference_cost: The difference_cost of this ReconciliationBreak.  # noqa: E501
        :type difference_cost: lusid.CurrencyAndAmount
        """
        if self.local_vars_configuration.client_side_validation and difference_cost is None:  # noqa: E501
            raise ValueError("Invalid value for `difference_cost`, must not be `None`")  # noqa: E501

        self._difference_cost = difference_cost

    @property
    def instrument_properties(self):
        """Gets the instrument_properties of this ReconciliationBreak.  # noqa: E501

        Additional features relating to the instrument  # noqa: E501

        :return: The instrument_properties of this ReconciliationBreak.  # noqa: E501
        :rtype: list[lusid.ModelProperty]
        """
        return self._instrument_properties

    @instrument_properties.setter
    def instrument_properties(self, instrument_properties):
        """Sets the instrument_properties of this ReconciliationBreak.

        Additional features relating to the instrument  # noqa: E501

        :param instrument_properties: The instrument_properties of this ReconciliationBreak.  # noqa: E501
        :type instrument_properties: list[lusid.ModelProperty]
        """
        if self.local_vars_configuration.client_side_validation and instrument_properties is None:  # noqa: E501
            raise ValueError("Invalid value for `instrument_properties`, must not be `None`")  # noqa: E501

        self._instrument_properties = instrument_properties

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ReconciliationBreak):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReconciliationBreak):
            return True

        return self.to_dict() != other.to_dict()
