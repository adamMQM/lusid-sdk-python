# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3121
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class PortfolioDetails(object):
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
        'href': 'str',
        'origin_portfolio_id': 'ResourceId',
        'version': 'Version',
        'base_currency': 'str',
        'corporate_action_source_id': 'ResourceId',
        'sub_holding_keys': 'list[str]',
        'links': 'list[Link]'
    }

    attribute_map = {
        'href': 'href',
        'origin_portfolio_id': 'originPortfolioId',
        'version': 'version',
        'base_currency': 'baseCurrency',
        'corporate_action_source_id': 'corporateActionSourceId',
        'sub_holding_keys': 'subHoldingKeys',
        'links': 'links'
    }

    required_map = {
        'href': 'optional',
        'origin_portfolio_id': 'required',
        'version': 'required',
        'base_currency': 'required',
        'corporate_action_source_id': 'optional',
        'sub_holding_keys': 'optional',
        'links': 'optional'
    }

    def __init__(self, href=None, origin_portfolio_id=None, version=None, base_currency=None, corporate_action_source_id=None, sub_holding_keys=None, links=None):  # noqa: E501
        """
        PortfolioDetails - a model defined in OpenAPI

        :param href:  The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
        :type href: str
        :param origin_portfolio_id:  (required)
        :type origin_portfolio_id: lusid.ResourceId
        :param version:  (required)
        :type version: lusid.Version
        :param base_currency:  The base currency of the transaction portfolio. (required)
        :type base_currency: str
        :param corporate_action_source_id: 
        :type corporate_action_source_id: lusid.ResourceId
        :param sub_holding_keys: 
        :type sub_holding_keys: list[str]
        :param links: 
        :type links: list[lusid.Link]

        """  # noqa: E501

        self._href = None
        self._origin_portfolio_id = None
        self._version = None
        self._base_currency = None
        self._corporate_action_source_id = None
        self._sub_holding_keys = None
        self._links = None
        self.discriminator = None

        self.href = href
        self.origin_portfolio_id = origin_portfolio_id
        self.version = version
        self.base_currency = base_currency
        if corporate_action_source_id is not None:
            self.corporate_action_source_id = corporate_action_source_id
        self.sub_holding_keys = sub_holding_keys
        self.links = links

    @property
    def href(self):
        """Gets the href of this PortfolioDetails.  # noqa: E501

        The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.  # noqa: E501

        :return: The href of this PortfolioDetails.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this PortfolioDetails.

        The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.  # noqa: E501

        :param href: The href of this PortfolioDetails.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def origin_portfolio_id(self):
        """Gets the origin_portfolio_id of this PortfolioDetails.  # noqa: E501


        :return: The origin_portfolio_id of this PortfolioDetails.  # noqa: E501
        :rtype: ResourceId
        """
        return self._origin_portfolio_id

    @origin_portfolio_id.setter
    def origin_portfolio_id(self, origin_portfolio_id):
        """Sets the origin_portfolio_id of this PortfolioDetails.


        :param origin_portfolio_id: The origin_portfolio_id of this PortfolioDetails.  # noqa: E501
        :type: ResourceId
        """
        if origin_portfolio_id is None:
            raise ValueError("Invalid value for `origin_portfolio_id`, must not be `None`")  # noqa: E501

        self._origin_portfolio_id = origin_portfolio_id

    @property
    def version(self):
        """Gets the version of this PortfolioDetails.  # noqa: E501


        :return: The version of this PortfolioDetails.  # noqa: E501
        :rtype: Version
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this PortfolioDetails.


        :param version: The version of this PortfolioDetails.  # noqa: E501
        :type: Version
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    @property
    def base_currency(self):
        """Gets the base_currency of this PortfolioDetails.  # noqa: E501

        The base currency of the transaction portfolio.  # noqa: E501

        :return: The base_currency of this PortfolioDetails.  # noqa: E501
        :rtype: str
        """
        return self._base_currency

    @base_currency.setter
    def base_currency(self, base_currency):
        """Sets the base_currency of this PortfolioDetails.

        The base currency of the transaction portfolio.  # noqa: E501

        :param base_currency: The base_currency of this PortfolioDetails.  # noqa: E501
        :type: str
        """
        if base_currency is None:
            raise ValueError("Invalid value for `base_currency`, must not be `None`")  # noqa: E501

        self._base_currency = base_currency

    @property
    def corporate_action_source_id(self):
        """Gets the corporate_action_source_id of this PortfolioDetails.  # noqa: E501


        :return: The corporate_action_source_id of this PortfolioDetails.  # noqa: E501
        :rtype: ResourceId
        """
        return self._corporate_action_source_id

    @corporate_action_source_id.setter
    def corporate_action_source_id(self, corporate_action_source_id):
        """Sets the corporate_action_source_id of this PortfolioDetails.


        :param corporate_action_source_id: The corporate_action_source_id of this PortfolioDetails.  # noqa: E501
        :type: ResourceId
        """

        self._corporate_action_source_id = corporate_action_source_id

    @property
    def sub_holding_keys(self):
        """Gets the sub_holding_keys of this PortfolioDetails.  # noqa: E501


        :return: The sub_holding_keys of this PortfolioDetails.  # noqa: E501
        :rtype: list[str]
        """
        return self._sub_holding_keys

    @sub_holding_keys.setter
    def sub_holding_keys(self, sub_holding_keys):
        """Sets the sub_holding_keys of this PortfolioDetails.


        :param sub_holding_keys: The sub_holding_keys of this PortfolioDetails.  # noqa: E501
        :type: list[str]
        """

        self._sub_holding_keys = sub_holding_keys

    @property
    def links(self):
        """Gets the links of this PortfolioDetails.  # noqa: E501


        :return: The links of this PortfolioDetails.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this PortfolioDetails.


        :param links: The links of this PortfolioDetails.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PortfolioDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
