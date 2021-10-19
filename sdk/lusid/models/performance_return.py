# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3623
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


class PerformanceReturn(object):
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
        'effective_at': 'datetime',
        'rate_of_return': 'float',
        'opening_market_value': 'float',
        'closing_market_value': 'float',
        'period': 'str'
    }

    attribute_map = {
        'effective_at': 'effectiveAt',
        'rate_of_return': 'rateOfReturn',
        'opening_market_value': 'openingMarketValue',
        'closing_market_value': 'closingMarketValue',
        'period': 'period'
    }

    required_map = {
        'effective_at': 'required',
        'rate_of_return': 'required',
        'opening_market_value': 'optional',
        'closing_market_value': 'optional',
        'period': 'optional'
    }

    def __init__(self, effective_at=None, rate_of_return=None, opening_market_value=None, closing_market_value=None, period=None, local_vars_configuration=None):  # noqa: E501
        """PerformanceReturn - a model defined in OpenAPI"
        
        :param effective_at:  The effectiveAt for the return. (required)
        :type effective_at: datetime
        :param rate_of_return:  The return number. (required)
        :type rate_of_return: float
        :param opening_market_value:  The opening market value.
        :type opening_market_value: float
        :param closing_market_value:  The closing market value.
        :type closing_market_value: float
        :param period:  Upsert the returns on a Daily or Monthly period. Defaults to Daily.
        :type period: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._effective_at = None
        self._rate_of_return = None
        self._opening_market_value = None
        self._closing_market_value = None
        self._period = None
        self.discriminator = None

        self.effective_at = effective_at
        self.rate_of_return = rate_of_return
        self.opening_market_value = opening_market_value
        self.closing_market_value = closing_market_value
        self.period = period

    @property
    def effective_at(self):
        """Gets the effective_at of this PerformanceReturn.  # noqa: E501

        The effectiveAt for the return.  # noqa: E501

        :return: The effective_at of this PerformanceReturn.  # noqa: E501
        :rtype: datetime
        """
        return self._effective_at

    @effective_at.setter
    def effective_at(self, effective_at):
        """Sets the effective_at of this PerformanceReturn.

        The effectiveAt for the return.  # noqa: E501

        :param effective_at: The effective_at of this PerformanceReturn.  # noqa: E501
        :type effective_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and effective_at is None:  # noqa: E501
            raise ValueError("Invalid value for `effective_at`, must not be `None`")  # noqa: E501

        self._effective_at = effective_at

    @property
    def rate_of_return(self):
        """Gets the rate_of_return of this PerformanceReturn.  # noqa: E501

        The return number.  # noqa: E501

        :return: The rate_of_return of this PerformanceReturn.  # noqa: E501
        :rtype: float
        """
        return self._rate_of_return

    @rate_of_return.setter
    def rate_of_return(self, rate_of_return):
        """Sets the rate_of_return of this PerformanceReturn.

        The return number.  # noqa: E501

        :param rate_of_return: The rate_of_return of this PerformanceReturn.  # noqa: E501
        :type rate_of_return: float
        """
        if self.local_vars_configuration.client_side_validation and rate_of_return is None:  # noqa: E501
            raise ValueError("Invalid value for `rate_of_return`, must not be `None`")  # noqa: E501

        self._rate_of_return = rate_of_return

    @property
    def opening_market_value(self):
        """Gets the opening_market_value of this PerformanceReturn.  # noqa: E501

        The opening market value.  # noqa: E501

        :return: The opening_market_value of this PerformanceReturn.  # noqa: E501
        :rtype: float
        """
        return self._opening_market_value

    @opening_market_value.setter
    def opening_market_value(self, opening_market_value):
        """Sets the opening_market_value of this PerformanceReturn.

        The opening market value.  # noqa: E501

        :param opening_market_value: The opening_market_value of this PerformanceReturn.  # noqa: E501
        :type opening_market_value: float
        """

        self._opening_market_value = opening_market_value

    @property
    def closing_market_value(self):
        """Gets the closing_market_value of this PerformanceReturn.  # noqa: E501

        The closing market value.  # noqa: E501

        :return: The closing_market_value of this PerformanceReturn.  # noqa: E501
        :rtype: float
        """
        return self._closing_market_value

    @closing_market_value.setter
    def closing_market_value(self, closing_market_value):
        """Sets the closing_market_value of this PerformanceReturn.

        The closing market value.  # noqa: E501

        :param closing_market_value: The closing_market_value of this PerformanceReturn.  # noqa: E501
        :type closing_market_value: float
        """

        self._closing_market_value = closing_market_value

    @property
    def period(self):
        """Gets the period of this PerformanceReturn.  # noqa: E501

        Upsert the returns on a Daily or Monthly period. Defaults to Daily.  # noqa: E501

        :return: The period of this PerformanceReturn.  # noqa: E501
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this PerformanceReturn.

        Upsert the returns on a Daily or Monthly period. Defaults to Daily.  # noqa: E501

        :param period: The period of this PerformanceReturn.  # noqa: E501
        :type period: str
        """

        self._period = period

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
        if not isinstance(other, PerformanceReturn):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PerformanceReturn):
            return True

        return self.to_dict() != other.to_dict()
