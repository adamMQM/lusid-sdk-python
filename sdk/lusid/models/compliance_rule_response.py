# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.0.554
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


class ComplianceRuleResponse(object):
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
        'id': 'ResourceId',
        'name': 'str',
        'description': 'str',
        'active': 'bool',
        'template_id': 'ResourceId',
        'variation': 'str',
        'portfolio_group_id': 'ResourceId',
        'parameters': 'dict(str, ComplianceParameter)',
        'properties': 'dict(str, PerpetualProperty)',
        'version': 'Version',
        'links': 'list[Link]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'active': 'active',
        'template_id': 'templateId',
        'variation': 'variation',
        'portfolio_group_id': 'portfolioGroupId',
        'parameters': 'parameters',
        'properties': 'properties',
        'version': 'version',
        'links': 'links'
    }

    required_map = {
        'id': 'optional',
        'name': 'optional',
        'description': 'optional',
        'active': 'optional',
        'template_id': 'optional',
        'variation': 'optional',
        'portfolio_group_id': 'optional',
        'parameters': 'optional',
        'properties': 'optional',
        'version': 'optional',
        'links': 'optional'
    }

    def __init__(self, id=None, name=None, description=None, active=None, template_id=None, variation=None, portfolio_group_id=None, parameters=None, properties=None, version=None, links=None, local_vars_configuration=None):  # noqa: E501
        """ComplianceRuleResponse - a model defined in OpenAPI"
        
        :param id: 
        :type id: lusid.ResourceId
        :param name: 
        :type name: str
        :param description: 
        :type description: str
        :param active: 
        :type active: bool
        :param template_id: 
        :type template_id: lusid.ResourceId
        :param variation: 
        :type variation: str
        :param portfolio_group_id: 
        :type portfolio_group_id: lusid.ResourceId
        :param parameters: 
        :type parameters: dict[str, lusid.ComplianceParameter]
        :param properties: 
        :type properties: dict[str, lusid.PerpetualProperty]
        :param version: 
        :type version: lusid.Version
        :param links:  Collection of links.
        :type links: list[lusid.Link]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._description = None
        self._active = None
        self._template_id = None
        self._variation = None
        self._portfolio_group_id = None
        self._parameters = None
        self._properties = None
        self._version = None
        self._links = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        self.description = description
        if active is not None:
            self.active = active
        if template_id is not None:
            self.template_id = template_id
        self.variation = variation
        if portfolio_group_id is not None:
            self.portfolio_group_id = portfolio_group_id
        self.parameters = parameters
        self.properties = properties
        if version is not None:
            self.version = version
        self.links = links

    @property
    def id(self):
        """Gets the id of this ComplianceRuleResponse.  # noqa: E501


        :return: The id of this ComplianceRuleResponse.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ComplianceRuleResponse.


        :param id: The id of this ComplianceRuleResponse.  # noqa: E501
        :type id: lusid.ResourceId
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ComplianceRuleResponse.  # noqa: E501


        :return: The name of this ComplianceRuleResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ComplianceRuleResponse.


        :param name: The name of this ComplianceRuleResponse.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this ComplianceRuleResponse.  # noqa: E501


        :return: The description of this ComplianceRuleResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ComplianceRuleResponse.


        :param description: The description of this ComplianceRuleResponse.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def active(self):
        """Gets the active of this ComplianceRuleResponse.  # noqa: E501


        :return: The active of this ComplianceRuleResponse.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this ComplianceRuleResponse.


        :param active: The active of this ComplianceRuleResponse.  # noqa: E501
        :type active: bool
        """

        self._active = active

    @property
    def template_id(self):
        """Gets the template_id of this ComplianceRuleResponse.  # noqa: E501


        :return: The template_id of this ComplianceRuleResponse.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this ComplianceRuleResponse.


        :param template_id: The template_id of this ComplianceRuleResponse.  # noqa: E501
        :type template_id: lusid.ResourceId
        """

        self._template_id = template_id

    @property
    def variation(self):
        """Gets the variation of this ComplianceRuleResponse.  # noqa: E501


        :return: The variation of this ComplianceRuleResponse.  # noqa: E501
        :rtype: str
        """
        return self._variation

    @variation.setter
    def variation(self, variation):
        """Sets the variation of this ComplianceRuleResponse.


        :param variation: The variation of this ComplianceRuleResponse.  # noqa: E501
        :type variation: str
        """

        self._variation = variation

    @property
    def portfolio_group_id(self):
        """Gets the portfolio_group_id of this ComplianceRuleResponse.  # noqa: E501


        :return: The portfolio_group_id of this ComplianceRuleResponse.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._portfolio_group_id

    @portfolio_group_id.setter
    def portfolio_group_id(self, portfolio_group_id):
        """Sets the portfolio_group_id of this ComplianceRuleResponse.


        :param portfolio_group_id: The portfolio_group_id of this ComplianceRuleResponse.  # noqa: E501
        :type portfolio_group_id: lusid.ResourceId
        """

        self._portfolio_group_id = portfolio_group_id

    @property
    def parameters(self):
        """Gets the parameters of this ComplianceRuleResponse.  # noqa: E501


        :return: The parameters of this ComplianceRuleResponse.  # noqa: E501
        :rtype: dict[str, lusid.ComplianceParameter]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this ComplianceRuleResponse.


        :param parameters: The parameters of this ComplianceRuleResponse.  # noqa: E501
        :type parameters: dict[str, lusid.ComplianceParameter]
        """

        self._parameters = parameters

    @property
    def properties(self):
        """Gets the properties of this ComplianceRuleResponse.  # noqa: E501


        :return: The properties of this ComplianceRuleResponse.  # noqa: E501
        :rtype: dict[str, lusid.PerpetualProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this ComplianceRuleResponse.


        :param properties: The properties of this ComplianceRuleResponse.  # noqa: E501
        :type properties: dict[str, lusid.PerpetualProperty]
        """

        self._properties = properties

    @property
    def version(self):
        """Gets the version of this ComplianceRuleResponse.  # noqa: E501


        :return: The version of this ComplianceRuleResponse.  # noqa: E501
        :rtype: lusid.Version
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ComplianceRuleResponse.


        :param version: The version of this ComplianceRuleResponse.  # noqa: E501
        :type version: lusid.Version
        """

        self._version = version

    @property
    def links(self):
        """Gets the links of this ComplianceRuleResponse.  # noqa: E501

        Collection of links.  # noqa: E501

        :return: The links of this ComplianceRuleResponse.  # noqa: E501
        :rtype: list[lusid.Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ComplianceRuleResponse.

        Collection of links.  # noqa: E501

        :param links: The links of this ComplianceRuleResponse.  # noqa: E501
        :type links: list[lusid.Link]
        """

        self._links = links

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
        if not isinstance(other, ComplianceRuleResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComplianceRuleResponse):
            return True

        return self.to_dict() != other.to_dict()
