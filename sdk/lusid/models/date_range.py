# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3507
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


class DateRange(object):
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
        'from_date': 'datetime',
        'until_date': 'datetime'
    }

    attribute_map = {
        'from_date': 'fromDate',
        'until_date': 'untilDate'
    }

    required_map = {
        'from_date': 'required',
        'until_date': 'optional'
    }

    def __init__(self, from_date=None, until_date=None, local_vars_configuration=None):  # noqa: E501
        """DateRange - a model defined in OpenAPI"
        
        :param from_date:  (required)
        :type from_date: datetime
        :param until_date: 
        :type until_date: datetime

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._from_date = None
        self._until_date = None
        self.discriminator = None

        self.from_date = from_date
        self.until_date = until_date

    @property
    def from_date(self):
        """Gets the from_date of this DateRange.  # noqa: E501


        :return: The from_date of this DateRange.  # noqa: E501
        :rtype: datetime
        """
        return self._from_date

    @from_date.setter
    def from_date(self, from_date):
        """Sets the from_date of this DateRange.


        :param from_date: The from_date of this DateRange.  # noqa: E501
        :type from_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and from_date is None:  # noqa: E501
            raise ValueError("Invalid value for `from_date`, must not be `None`")  # noqa: E501

        self._from_date = from_date

    @property
    def until_date(self):
        """Gets the until_date of this DateRange.  # noqa: E501


        :return: The until_date of this DateRange.  # noqa: E501
        :rtype: datetime
        """
        return self._until_date

    @until_date.setter
    def until_date(self, until_date):
        """Sets the until_date of this DateRange.


        :param until_date: The until_date of this DateRange.  # noqa: E501
        :type until_date: datetime
        """

        self._until_date = until_date

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
        if not isinstance(other, DateRange):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DateRange):
            return True

        return self.to_dict() != other.to_dict()
