# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.5200
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


class Barrier(object):
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
        'direction': 'str',
        'level': 'float',
        'monitoring': 'str',
        'type': 'str'
    }

    attribute_map = {
        'direction': 'direction',
        'level': 'level',
        'monitoring': 'monitoring',
        'type': 'type'
    }

    required_map = {
        'direction': 'required',
        'level': 'required',
        'monitoring': 'optional',
        'type': 'required'
    }

    def __init__(self, direction=None, level=None, monitoring=None, type=None, local_vars_configuration=None):  # noqa: E501
        """Barrier - a model defined in OpenAPI"
        
        :param direction:  Supported string (enumeration) values are: [Down, Up]. (required)
        :type direction: str
        :param level:  Trigger level, which the underlying should (or should not) cross/touch. (required)
        :type level: float
        :param monitoring:  Supported string (enumeration) values are: [European, Bermudan, American].
        :type monitoring: str
        :param type:  Supported string (enumeration) values are: [Knockin, Knockout]. (required)
        :type type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._direction = None
        self._level = None
        self._monitoring = None
        self._type = None
        self.discriminator = None

        self.direction = direction
        self.level = level
        self.monitoring = monitoring
        self.type = type

    @property
    def direction(self):
        """Gets the direction of this Barrier.  # noqa: E501

        Supported string (enumeration) values are: [Down, Up].  # noqa: E501

        :return: The direction of this Barrier.  # noqa: E501
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this Barrier.

        Supported string (enumeration) values are: [Down, Up].  # noqa: E501

        :param direction: The direction of this Barrier.  # noqa: E501
        :type direction: str
        """
        if self.local_vars_configuration.client_side_validation and direction is None:  # noqa: E501
            raise ValueError("Invalid value for `direction`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                direction is not None and len(direction) < 1):
            raise ValueError("Invalid value for `direction`, length must be greater than or equal to `1`")  # noqa: E501

        self._direction = direction

    @property
    def level(self):
        """Gets the level of this Barrier.  # noqa: E501

        Trigger level, which the underlying should (or should not) cross/touch.  # noqa: E501

        :return: The level of this Barrier.  # noqa: E501
        :rtype: float
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this Barrier.

        Trigger level, which the underlying should (or should not) cross/touch.  # noqa: E501

        :param level: The level of this Barrier.  # noqa: E501
        :type level: float
        """
        if self.local_vars_configuration.client_side_validation and level is None:  # noqa: E501
            raise ValueError("Invalid value for `level`, must not be `None`")  # noqa: E501

        self._level = level

    @property
    def monitoring(self):
        """Gets the monitoring of this Barrier.  # noqa: E501

        Supported string (enumeration) values are: [European, Bermudan, American].  # noqa: E501

        :return: The monitoring of this Barrier.  # noqa: E501
        :rtype: str
        """
        return self._monitoring

    @monitoring.setter
    def monitoring(self, monitoring):
        """Sets the monitoring of this Barrier.

        Supported string (enumeration) values are: [European, Bermudan, American].  # noqa: E501

        :param monitoring: The monitoring of this Barrier.  # noqa: E501
        :type monitoring: str
        """

        self._monitoring = monitoring

    @property
    def type(self):
        """Gets the type of this Barrier.  # noqa: E501

        Supported string (enumeration) values are: [Knockin, Knockout].  # noqa: E501

        :return: The type of this Barrier.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Barrier.

        Supported string (enumeration) values are: [Knockin, Knockout].  # noqa: E501

        :param type: The type of this Barrier.  # noqa: E501
        :type type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                type is not None and len(type) < 1):
            raise ValueError("Invalid value for `type`, length must be greater than or equal to `1`")  # noqa: E501

        self._type = type

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
        if not isinstance(other, Barrier):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Barrier):
            return True

        return self.to_dict() != other.to_dict()
