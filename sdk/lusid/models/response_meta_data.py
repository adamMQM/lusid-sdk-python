# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.4646
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


class ResponseMetaData(object):
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
        'type': 'str',
        'description': 'str',
        'identifier_type': 'str',
        'identifiers': 'list[str]'
    }

    attribute_map = {
        'type': 'type',
        'description': 'description',
        'identifier_type': 'identifierType',
        'identifiers': 'identifiers'
    }

    required_map = {
        'type': 'optional',
        'description': 'optional',
        'identifier_type': 'optional',
        'identifiers': 'optional'
    }

    def __init__(self, type=None, description=None, identifier_type=None, identifiers=None, local_vars_configuration=None):  # noqa: E501
        """ResponseMetaData - a model defined in OpenAPI"
        
        :param type:  The type of meta data information being provided
        :type type: str
        :param description:  The description of what occured for this specific piece of meta data
        :type description: str
        :param identifier_type:  The type of the listed identifiers
        :type identifier_type: str
        :param identifiers:  The related identifiers that were impacted by this event
        :type identifiers: list[str]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._description = None
        self._identifier_type = None
        self._identifiers = None
        self.discriminator = None

        self.type = type
        self.description = description
        self.identifier_type = identifier_type
        self.identifiers = identifiers

    @property
    def type(self):
        """Gets the type of this ResponseMetaData.  # noqa: E501

        The type of meta data information being provided  # noqa: E501

        :return: The type of this ResponseMetaData.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ResponseMetaData.

        The type of meta data information being provided  # noqa: E501

        :param type: The type of this ResponseMetaData.  # noqa: E501
        :type type: str
        """

        self._type = type

    @property
    def description(self):
        """Gets the description of this ResponseMetaData.  # noqa: E501

        The description of what occured for this specific piece of meta data  # noqa: E501

        :return: The description of this ResponseMetaData.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ResponseMetaData.

        The description of what occured for this specific piece of meta data  # noqa: E501

        :param description: The description of this ResponseMetaData.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def identifier_type(self):
        """Gets the identifier_type of this ResponseMetaData.  # noqa: E501

        The type of the listed identifiers  # noqa: E501

        :return: The identifier_type of this ResponseMetaData.  # noqa: E501
        :rtype: str
        """
        return self._identifier_type

    @identifier_type.setter
    def identifier_type(self, identifier_type):
        """Sets the identifier_type of this ResponseMetaData.

        The type of the listed identifiers  # noqa: E501

        :param identifier_type: The identifier_type of this ResponseMetaData.  # noqa: E501
        :type identifier_type: str
        """

        self._identifier_type = identifier_type

    @property
    def identifiers(self):
        """Gets the identifiers of this ResponseMetaData.  # noqa: E501

        The related identifiers that were impacted by this event  # noqa: E501

        :return: The identifiers of this ResponseMetaData.  # noqa: E501
        :rtype: list[str]
        """
        return self._identifiers

    @identifiers.setter
    def identifiers(self, identifiers):
        """Sets the identifiers of this ResponseMetaData.

        The related identifiers that were impacted by this event  # noqa: E501

        :param identifiers: The identifiers of this ResponseMetaData.  # noqa: E501
        :type identifiers: list[str]
        """

        self._identifiers = identifiers

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
        if not isinstance(other, ResponseMetaData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResponseMetaData):
            return True

        return self.to_dict() != other.to_dict()
