# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.0.428
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


class IUnitDefinitionDto(object):
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
        'schema': 'str',
        'code': 'str',
        'display_name': 'str',
        'description': 'str'
    }

    attribute_map = {
        'schema': 'schema',
        'code': 'code',
        'display_name': 'displayName',
        'description': 'description'
    }

    required_map = {
        'schema': 'optional',
        'code': 'optional',
        'display_name': 'optional',
        'description': 'optional'
    }

    def __init__(self, schema=None, code=None, display_name=None, description=None, local_vars_configuration=None):  # noqa: E501
        """IUnitDefinitionDto - a model defined in OpenAPI"
        
        :param schema:  The available values are: NoUnits, Basic, Iso4217Currency
        :type schema: str
        :param code: 
        :type code: str
        :param display_name: 
        :type display_name: str
        :param description: 
        :type description: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._schema = None
        self._code = None
        self._display_name = None
        self._description = None
        self.discriminator = None

        if schema is not None:
            self.schema = schema
        self.code = code
        self.display_name = display_name
        self.description = description

    @property
    def schema(self):
        """Gets the schema of this IUnitDefinitionDto.  # noqa: E501

        The available values are: NoUnits, Basic, Iso4217Currency  # noqa: E501

        :return: The schema of this IUnitDefinitionDto.  # noqa: E501
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this IUnitDefinitionDto.

        The available values are: NoUnits, Basic, Iso4217Currency  # noqa: E501

        :param schema: The schema of this IUnitDefinitionDto.  # noqa: E501
        :type schema: str
        """
        allowed_values = ["NoUnits", "Basic", "Iso4217Currency"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and schema not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `schema` ({0}), must be one of {1}"  # noqa: E501
                .format(schema, allowed_values)
            )

        self._schema = schema

    @property
    def code(self):
        """Gets the code of this IUnitDefinitionDto.  # noqa: E501


        :return: The code of this IUnitDefinitionDto.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this IUnitDefinitionDto.


        :param code: The code of this IUnitDefinitionDto.  # noqa: E501
        :type code: str
        """

        self._code = code

    @property
    def display_name(self):
        """Gets the display_name of this IUnitDefinitionDto.  # noqa: E501


        :return: The display_name of this IUnitDefinitionDto.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this IUnitDefinitionDto.


        :param display_name: The display_name of this IUnitDefinitionDto.  # noqa: E501
        :type display_name: str
        """

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this IUnitDefinitionDto.  # noqa: E501


        :return: The description of this IUnitDefinitionDto.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this IUnitDefinitionDto.


        :param description: The description of this IUnitDefinitionDto.  # noqa: E501
        :type description: str
        """

        self._description = description

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
        if not isinstance(other, IUnitDefinitionDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IUnitDefinitionDto):
            return True

        return self.to_dict() != other.to_dict()
