# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.0.352
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


class RoundingConfigurationComponent(object):
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
        'rounding_type': 'str'
    }

    attribute_map = {
        'rounding_type': 'roundingType'
    }

    required_map = {
        'rounding_type': 'required'
    }

    def __init__(self, rounding_type=None, local_vars_configuration=None):  # noqa: E501
        """RoundingConfigurationComponent - a model defined in OpenAPI"
        
        :param rounding_type:  The type of rounding that should be used, eg: Up, Down, NearestRoundHalfAwayFromZero (required)
        :type rounding_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._rounding_type = None
        self.discriminator = None

        self.rounding_type = rounding_type

    @property
    def rounding_type(self):
        """Gets the rounding_type of this RoundingConfigurationComponent.  # noqa: E501

        The type of rounding that should be used, eg: Up, Down, NearestRoundHalfAwayFromZero  # noqa: E501

        :return: The rounding_type of this RoundingConfigurationComponent.  # noqa: E501
        :rtype: str
        """
        return self._rounding_type

    @rounding_type.setter
    def rounding_type(self, rounding_type):
        """Sets the rounding_type of this RoundingConfigurationComponent.

        The type of rounding that should be used, eg: Up, Down, NearestRoundHalfAwayFromZero  # noqa: E501

        :param rounding_type: The rounding_type of this RoundingConfigurationComponent.  # noqa: E501
        :type rounding_type: str
        """
        if self.local_vars_configuration.client_side_validation and rounding_type is None:  # noqa: E501
            raise ValueError("Invalid value for `rounding_type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                rounding_type is not None and len(rounding_type) < 1):
            raise ValueError("Invalid value for `rounding_type`, length must be greater than or equal to `1`")  # noqa: E501

        self._rounding_type = rounding_type

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
        if not isinstance(other, RoundingConfigurationComponent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RoundingConfigurationComponent):
            return True

        return self.to_dict() != other.to_dict()