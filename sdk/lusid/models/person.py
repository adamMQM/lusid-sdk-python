# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.0.628
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


class Person(object):
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
        'display_name': 'str',
        'description': 'str',
        'href': 'str',
        'lusid_person_id': 'str',
        'identifiers': 'dict(str, ModelProperty)',
        'properties': 'dict(str, ModelProperty)',
        'relationships': 'list[Relationship]',
        'version': 'Version'
    }

    attribute_map = {
        'display_name': 'displayName',
        'description': 'description',
        'href': 'href',
        'lusid_person_id': 'lusidPersonId',
        'identifiers': 'identifiers',
        'properties': 'properties',
        'relationships': 'relationships',
        'version': 'version'
    }

    required_map = {
        'display_name': 'optional',
        'description': 'optional',
        'href': 'optional',
        'lusid_person_id': 'optional',
        'identifiers': 'optional',
        'properties': 'optional',
        'relationships': 'optional',
        'version': 'optional'
    }

    def __init__(self, display_name=None, description=None, href=None, lusid_person_id=None, identifiers=None, properties=None, relationships=None, version=None, local_vars_configuration=None):  # noqa: E501
        """Person - a model defined in OpenAPI"
        
        :param display_name:  The display name of the Person
        :type display_name: str
        :param description:  The description of the Person
        :type description: str
        :param href:  The specifc Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
        :type href: str
        :param lusid_person_id:  The unique LUSID Person Identifier of the Person.
        :type lusid_person_id: str
        :param identifiers:  Unique client-defined identifiers of the Person.
        :type identifiers: dict[str, lusid.ModelProperty]
        :param properties:  A set of properties associated to the Person. There can be multiple properties associated with a property key.
        :type properties: dict[str, lusid.ModelProperty]
        :param relationships:  A set of relationships associated to the Person.
        :type relationships: list[lusid.Relationship]
        :param version: 
        :type version: lusid.Version

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._display_name = None
        self._description = None
        self._href = None
        self._lusid_person_id = None
        self._identifiers = None
        self._properties = None
        self._relationships = None
        self._version = None
        self.discriminator = None

        self.display_name = display_name
        self.description = description
        self.href = href
        self.lusid_person_id = lusid_person_id
        self.identifiers = identifiers
        self.properties = properties
        self.relationships = relationships
        if version is not None:
            self.version = version

    @property
    def display_name(self):
        """Gets the display_name of this Person.  # noqa: E501

        The display name of the Person  # noqa: E501

        :return: The display_name of this Person.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this Person.

        The display name of the Person  # noqa: E501

        :param display_name: The display_name of this Person.  # noqa: E501
        :type display_name: str
        """

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this Person.  # noqa: E501

        The description of the Person  # noqa: E501

        :return: The description of this Person.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Person.

        The description of the Person  # noqa: E501

        :param description: The description of this Person.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def href(self):
        """Gets the href of this Person.  # noqa: E501

        The specifc Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.  # noqa: E501

        :return: The href of this Person.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this Person.

        The specifc Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.  # noqa: E501

        :param href: The href of this Person.  # noqa: E501
        :type href: str
        """

        self._href = href

    @property
    def lusid_person_id(self):
        """Gets the lusid_person_id of this Person.  # noqa: E501

        The unique LUSID Person Identifier of the Person.  # noqa: E501

        :return: The lusid_person_id of this Person.  # noqa: E501
        :rtype: str
        """
        return self._lusid_person_id

    @lusid_person_id.setter
    def lusid_person_id(self, lusid_person_id):
        """Sets the lusid_person_id of this Person.

        The unique LUSID Person Identifier of the Person.  # noqa: E501

        :param lusid_person_id: The lusid_person_id of this Person.  # noqa: E501
        :type lusid_person_id: str
        """

        self._lusid_person_id = lusid_person_id

    @property
    def identifiers(self):
        """Gets the identifiers of this Person.  # noqa: E501

        Unique client-defined identifiers of the Person.  # noqa: E501

        :return: The identifiers of this Person.  # noqa: E501
        :rtype: dict[str, lusid.ModelProperty]
        """
        return self._identifiers

    @identifiers.setter
    def identifiers(self, identifiers):
        """Sets the identifiers of this Person.

        Unique client-defined identifiers of the Person.  # noqa: E501

        :param identifiers: The identifiers of this Person.  # noqa: E501
        :type identifiers: dict[str, lusid.ModelProperty]
        """

        self._identifiers = identifiers

    @property
    def properties(self):
        """Gets the properties of this Person.  # noqa: E501

        A set of properties associated to the Person. There can be multiple properties associated with a property key.  # noqa: E501

        :return: The properties of this Person.  # noqa: E501
        :rtype: dict[str, lusid.ModelProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this Person.

        A set of properties associated to the Person. There can be multiple properties associated with a property key.  # noqa: E501

        :param properties: The properties of this Person.  # noqa: E501
        :type properties: dict[str, lusid.ModelProperty]
        """

        self._properties = properties

    @property
    def relationships(self):
        """Gets the relationships of this Person.  # noqa: E501

        A set of relationships associated to the Person.  # noqa: E501

        :return: The relationships of this Person.  # noqa: E501
        :rtype: list[lusid.Relationship]
        """
        return self._relationships

    @relationships.setter
    def relationships(self, relationships):
        """Sets the relationships of this Person.

        A set of relationships associated to the Person.  # noqa: E501

        :param relationships: The relationships of this Person.  # noqa: E501
        :type relationships: list[lusid.Relationship]
        """

        self._relationships = relationships

    @property
    def version(self):
        """Gets the version of this Person.  # noqa: E501


        :return: The version of this Person.  # noqa: E501
        :rtype: lusid.Version
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Person.


        :param version: The version of this Person.  # noqa: E501
        :type version: lusid.Version
        """

        self._version = version

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
        if not isinstance(other, Person):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Person):
            return True

        return self.to_dict() != other.to_dict()
