# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.0.578
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


class TranslateEntitiesInlinedRequest(object):
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
        'entity_payloads': 'dict(str, TranslationInput)',
        'script_body': 'str',
        'schema': 'DialectSchema'
    }

    attribute_map = {
        'entity_payloads': 'entityPayloads',
        'script_body': 'scriptBody',
        'schema': 'schema'
    }

    required_map = {
        'entity_payloads': 'required',
        'script_body': 'required',
        'schema': 'optional'
    }

    def __init__(self, entity_payloads=None, script_body=None, schema=None, local_vars_configuration=None):  # noqa: E501
        """TranslateEntitiesInlinedRequest - a model defined in OpenAPI"
        
        :param entity_payloads:  Entity payloads to be translated indexed by (ephemeral) unique correlation ids. (required)
        :type entity_payloads: dict[str, lusid.TranslationInput]
        :param script_body:  The body of the translation script to use for translating the entities. (required)
        :type script_body: str
        :param schema: 
        :type schema: lusid.DialectSchema

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._entity_payloads = None
        self._script_body = None
        self._schema = None
        self.discriminator = None

        self.entity_payloads = entity_payloads
        self.script_body = script_body
        if schema is not None:
            self.schema = schema

    @property
    def entity_payloads(self):
        """Gets the entity_payloads of this TranslateEntitiesInlinedRequest.  # noqa: E501

        Entity payloads to be translated indexed by (ephemeral) unique correlation ids.  # noqa: E501

        :return: The entity_payloads of this TranslateEntitiesInlinedRequest.  # noqa: E501
        :rtype: dict[str, lusid.TranslationInput]
        """
        return self._entity_payloads

    @entity_payloads.setter
    def entity_payloads(self, entity_payloads):
        """Sets the entity_payloads of this TranslateEntitiesInlinedRequest.

        Entity payloads to be translated indexed by (ephemeral) unique correlation ids.  # noqa: E501

        :param entity_payloads: The entity_payloads of this TranslateEntitiesInlinedRequest.  # noqa: E501
        :type entity_payloads: dict[str, lusid.TranslationInput]
        """
        if self.local_vars_configuration.client_side_validation and entity_payloads is None:  # noqa: E501
            raise ValueError("Invalid value for `entity_payloads`, must not be `None`")  # noqa: E501

        self._entity_payloads = entity_payloads

    @property
    def script_body(self):
        """Gets the script_body of this TranslateEntitiesInlinedRequest.  # noqa: E501

        The body of the translation script to use for translating the entities.  # noqa: E501

        :return: The script_body of this TranslateEntitiesInlinedRequest.  # noqa: E501
        :rtype: str
        """
        return self._script_body

    @script_body.setter
    def script_body(self, script_body):
        """Sets the script_body of this TranslateEntitiesInlinedRequest.

        The body of the translation script to use for translating the entities.  # noqa: E501

        :param script_body: The script_body of this TranslateEntitiesInlinedRequest.  # noqa: E501
        :type script_body: str
        """
        if self.local_vars_configuration.client_side_validation and script_body is None:  # noqa: E501
            raise ValueError("Invalid value for `script_body`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                script_body is not None and len(script_body) > 500000):
            raise ValueError("Invalid value for `script_body`, length must be less than or equal to `500000`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                script_body is not None and len(script_body) < 0):
            raise ValueError("Invalid value for `script_body`, length must be greater than or equal to `0`")  # noqa: E501

        self._script_body = script_body

    @property
    def schema(self):
        """Gets the schema of this TranslateEntitiesInlinedRequest.  # noqa: E501


        :return: The schema of this TranslateEntitiesInlinedRequest.  # noqa: E501
        :rtype: lusid.DialectSchema
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this TranslateEntitiesInlinedRequest.


        :param schema: The schema of this TranslateEntitiesInlinedRequest.  # noqa: E501
        :type schema: lusid.DialectSchema
        """

        self._schema = schema

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
        if not isinstance(other, TranslateEntitiesInlinedRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TranslateEntitiesInlinedRequest):
            return True

        return self.to_dict() != other.to_dict()
