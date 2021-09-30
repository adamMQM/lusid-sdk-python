# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3559
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


class InstrumentIdTypeDescriptor(object):
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
        'identifier_type': 'str',
        'property_key': 'str',
        'is_unique_identifier_type': 'bool'
    }

    attribute_map = {
        'identifier_type': 'identifierType',
        'property_key': 'propertyKey',
        'is_unique_identifier_type': 'isUniqueIdentifierType'
    }

    required_map = {
        'identifier_type': 'required',
        'property_key': 'required',
        'is_unique_identifier_type': 'required'
    }

    def __init__(self, identifier_type=None, property_key=None, is_unique_identifier_type=None, local_vars_configuration=None):  # noqa: E501
        """InstrumentIdTypeDescriptor - a model defined in OpenAPI"
        
        :param identifier_type:  The name of the identifier type. (required)
        :type identifier_type: str
        :param property_key:  The property key that corresponds to the identifier type. (required)
        :type property_key: str
        :param is_unique_identifier_type:  Whether or not the identifier type is enforced to be unique. (required)
        :type is_unique_identifier_type: bool

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._identifier_type = None
        self._property_key = None
        self._is_unique_identifier_type = None
        self.discriminator = None

        self.identifier_type = identifier_type
        self.property_key = property_key
        self.is_unique_identifier_type = is_unique_identifier_type

    @property
    def identifier_type(self):
        """Gets the identifier_type of this InstrumentIdTypeDescriptor.  # noqa: E501

        The name of the identifier type.  # noqa: E501

        :return: The identifier_type of this InstrumentIdTypeDescriptor.  # noqa: E501
        :rtype: str
        """
        return self._identifier_type

    @identifier_type.setter
    def identifier_type(self, identifier_type):
        """Sets the identifier_type of this InstrumentIdTypeDescriptor.

        The name of the identifier type.  # noqa: E501

        :param identifier_type: The identifier_type of this InstrumentIdTypeDescriptor.  # noqa: E501
        :type identifier_type: str
        """
        if self.local_vars_configuration.client_side_validation and identifier_type is None:  # noqa: E501
            raise ValueError("Invalid value for `identifier_type`, must not be `None`")  # noqa: E501

        self._identifier_type = identifier_type

    @property
    def property_key(self):
        """Gets the property_key of this InstrumentIdTypeDescriptor.  # noqa: E501

        The property key that corresponds to the identifier type.  # noqa: E501

        :return: The property_key of this InstrumentIdTypeDescriptor.  # noqa: E501
        :rtype: str
        """
        return self._property_key

    @property_key.setter
    def property_key(self, property_key):
        """Sets the property_key of this InstrumentIdTypeDescriptor.

        The property key that corresponds to the identifier type.  # noqa: E501

        :param property_key: The property_key of this InstrumentIdTypeDescriptor.  # noqa: E501
        :type property_key: str
        """
        if self.local_vars_configuration.client_side_validation and property_key is None:  # noqa: E501
            raise ValueError("Invalid value for `property_key`, must not be `None`")  # noqa: E501

        self._property_key = property_key

    @property
    def is_unique_identifier_type(self):
        """Gets the is_unique_identifier_type of this InstrumentIdTypeDescriptor.  # noqa: E501

        Whether or not the identifier type is enforced to be unique.  # noqa: E501

        :return: The is_unique_identifier_type of this InstrumentIdTypeDescriptor.  # noqa: E501
        :rtype: bool
        """
        return self._is_unique_identifier_type

    @is_unique_identifier_type.setter
    def is_unique_identifier_type(self, is_unique_identifier_type):
        """Sets the is_unique_identifier_type of this InstrumentIdTypeDescriptor.

        Whether or not the identifier type is enforced to be unique.  # noqa: E501

        :param is_unique_identifier_type: The is_unique_identifier_type of this InstrumentIdTypeDescriptor.  # noqa: E501
        :type is_unique_identifier_type: bool
        """
        if self.local_vars_configuration.client_side_validation and is_unique_identifier_type is None:  # noqa: E501
            raise ValueError("Invalid value for `is_unique_identifier_type`, must not be `None`")  # noqa: E501

        self._is_unique_identifier_type = is_unique_identifier_type

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
        if not isinstance(other, InstrumentIdTypeDescriptor):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InstrumentIdTypeDescriptor):
            return True

        return self.to_dict() != other.to_dict()
