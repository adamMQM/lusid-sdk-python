# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.4516
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


class AnnulQuotesResponse(object):
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
        'values': 'dict(str, datetime)',
        'failed': 'dict(str, ErrorDetail)',
        'links': 'list[Link]'
    }

    attribute_map = {
        'href': 'href',
        'values': 'values',
        'failed': 'failed',
        'links': 'links'
    }

    required_map = {
        'href': 'optional',
        'values': 'optional',
        'failed': 'optional',
        'links': 'optional'
    }

    def __init__(self, href=None, values=None, failed=None, links=None, local_vars_configuration=None):  # noqa: E501
        """AnnulQuotesResponse - a model defined in OpenAPI"
        
        :param href:  The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
        :type href: str
        :param values:  The quotes which have been successfully deleted along with the asAt datetime at which the deletion was committed to LUSID.
        :type values: dict(str, datetime)
        :param failed:  The quotes that could not be deleted along with a reason for their failure.
        :type failed: dict[str, lusid.ErrorDetail]
        :param links:  Collection of links.
        :type links: list[lusid.Link]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._href = None
        self._values = None
        self._failed = None
        self._links = None
        self.discriminator = None

        self.href = href
        self.values = values
        self.failed = failed
        self.links = links

    @property
    def href(self):
        """Gets the href of this AnnulQuotesResponse.  # noqa: E501

        The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.  # noqa: E501

        :return: The href of this AnnulQuotesResponse.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this AnnulQuotesResponse.

        The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.  # noqa: E501

        :param href: The href of this AnnulQuotesResponse.  # noqa: E501
        :type href: str
        """

        self._href = href

    @property
    def values(self):
        """Gets the values of this AnnulQuotesResponse.  # noqa: E501

        The quotes which have been successfully deleted along with the asAt datetime at which the deletion was committed to LUSID.  # noqa: E501

        :return: The values of this AnnulQuotesResponse.  # noqa: E501
        :rtype: dict(str, datetime)
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this AnnulQuotesResponse.

        The quotes which have been successfully deleted along with the asAt datetime at which the deletion was committed to LUSID.  # noqa: E501

        :param values: The values of this AnnulQuotesResponse.  # noqa: E501
        :type values: dict(str, datetime)
        """

        self._values = values

    @property
    def failed(self):
        """Gets the failed of this AnnulQuotesResponse.  # noqa: E501

        The quotes that could not be deleted along with a reason for their failure.  # noqa: E501

        :return: The failed of this AnnulQuotesResponse.  # noqa: E501
        :rtype: dict[str, lusid.ErrorDetail]
        """
        return self._failed

    @failed.setter
    def failed(self, failed):
        """Sets the failed of this AnnulQuotesResponse.

        The quotes that could not be deleted along with a reason for their failure.  # noqa: E501

        :param failed: The failed of this AnnulQuotesResponse.  # noqa: E501
        :type failed: dict[str, lusid.ErrorDetail]
        """

        self._failed = failed

    @property
    def links(self):
        """Gets the links of this AnnulQuotesResponse.  # noqa: E501

        Collection of links.  # noqa: E501

        :return: The links of this AnnulQuotesResponse.  # noqa: E501
        :rtype: list[lusid.Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this AnnulQuotesResponse.

        Collection of links.  # noqa: E501

        :param links: The links of this AnnulQuotesResponse.  # noqa: E501
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
        if not isinstance(other, AnnulQuotesResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AnnulQuotesResponse):
            return True

        return self.to_dict() != other.to_dict()
