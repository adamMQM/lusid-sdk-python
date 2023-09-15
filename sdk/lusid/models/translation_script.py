# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.0.521
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


class TranslationScript(object):
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
        'id': 'TranslationScriptId',
        'body': 'str'
    }

    attribute_map = {
        'id': 'id',
        'body': 'body'
    }

    required_map = {
        'id': 'required',
        'body': 'required'
    }

    def __init__(self, id=None, body=None, local_vars_configuration=None):  # noqa: E501
        """TranslationScript - a model defined in OpenAPI"
        
        :param id:  (required)
        :type id: lusid.TranslationScriptId
        :param body:  Body of the translation script, i.e. the actual translation code. (required)
        :type body: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._body = None
        self.discriminator = None

        self.id = id
        self.body = body

    @property
    def id(self):
        """Gets the id of this TranslationScript.  # noqa: E501


        :return: The id of this TranslationScript.  # noqa: E501
        :rtype: lusid.TranslationScriptId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TranslationScript.


        :param id: The id of this TranslationScript.  # noqa: E501
        :type id: lusid.TranslationScriptId
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def body(self):
        """Gets the body of this TranslationScript.  # noqa: E501

        Body of the translation script, i.e. the actual translation code.  # noqa: E501

        :return: The body of this TranslationScript.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this TranslationScript.

        Body of the translation script, i.e. the actual translation code.  # noqa: E501

        :param body: The body of this TranslationScript.  # noqa: E501
        :type body: str
        """
        if self.local_vars_configuration.client_side_validation and body is None:  # noqa: E501
            raise ValueError("Invalid value for `body`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                body is not None and len(body) > 500000):
            raise ValueError("Invalid value for `body`, length must be less than or equal to `500000`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                body is not None and len(body) < 0):
            raise ValueError("Invalid value for `body`, length must be greater than or equal to `0`")  # noqa: E501

        self._body = body

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
        if not isinstance(other, TranslationScript):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TranslationScript):
            return True

        return self.to_dict() != other.to_dict()