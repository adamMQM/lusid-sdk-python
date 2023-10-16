# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.0.614
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


class DecimalListAllOf(object):
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
        'values': 'list[float]',
        'reference_list_type': 'str'
    }

    attribute_map = {
        'values': 'values',
        'reference_list_type': 'referenceListType'
    }

    required_map = {
        'values': 'required',
        'reference_list_type': 'required'
    }

    def __init__(self, values=None, reference_list_type=None, local_vars_configuration=None):  # noqa: E501
        """DecimalListAllOf - a model defined in OpenAPI"
        
        :param values:  (required)
        :type values: list[float]
        :param reference_list_type:  The reference list values. The available values are: PortfolioGroupIdList, PortfolioIdList, AddressKeyList, StringList, InstrumentList, DecimalList (required)
        :type reference_list_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._values = None
        self._reference_list_type = None
        self.discriminator = None

        self.values = values
        self.reference_list_type = reference_list_type

    @property
    def values(self):
        """Gets the values of this DecimalListAllOf.  # noqa: E501


        :return: The values of this DecimalListAllOf.  # noqa: E501
        :rtype: list[float]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this DecimalListAllOf.


        :param values: The values of this DecimalListAllOf.  # noqa: E501
        :type values: list[float]
        """
        if self.local_vars_configuration.client_side_validation and values is None:  # noqa: E501
            raise ValueError("Invalid value for `values`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                values is not None and len(values) > 100):
            raise ValueError("Invalid value for `values`, number of items must be less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                values is not None and len(values) < 0):
            raise ValueError("Invalid value for `values`, number of items must be greater than or equal to `0`")  # noqa: E501

        self._values = values

    @property
    def reference_list_type(self):
        """Gets the reference_list_type of this DecimalListAllOf.  # noqa: E501

        The reference list values. The available values are: PortfolioGroupIdList, PortfolioIdList, AddressKeyList, StringList, InstrumentList, DecimalList  # noqa: E501

        :return: The reference_list_type of this DecimalListAllOf.  # noqa: E501
        :rtype: str
        """
        return self._reference_list_type

    @reference_list_type.setter
    def reference_list_type(self, reference_list_type):
        """Sets the reference_list_type of this DecimalListAllOf.

        The reference list values. The available values are: PortfolioGroupIdList, PortfolioIdList, AddressKeyList, StringList, InstrumentList, DecimalList  # noqa: E501

        :param reference_list_type: The reference_list_type of this DecimalListAllOf.  # noqa: E501
        :type reference_list_type: str
        """
        if self.local_vars_configuration.client_side_validation and reference_list_type is None:  # noqa: E501
            raise ValueError("Invalid value for `reference_list_type`, must not be `None`")  # noqa: E501
        allowed_values = ["PortfolioGroupIdList", "PortfolioIdList", "AddressKeyList", "StringList", "InstrumentList", "DecimalList"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and reference_list_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `reference_list_type` ({0}), must be one of {1}"  # noqa: E501
                .format(reference_list_type, allowed_values)
            )

        self._reference_list_type = reference_list_type

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
        if not isinstance(other, DecimalListAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DecimalListAllOf):
            return True

        return self.to_dict() != other.to_dict()
