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


class AdditionalPayment(object):
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
        'amount': 'float',
        'currency': 'str',
        'pay_date': 'datetime',
        'pay_receive': 'str'
    }

    attribute_map = {
        'amount': 'amount',
        'currency': 'currency',
        'pay_date': 'payDate',
        'pay_receive': 'payReceive'
    }

    required_map = {
        'amount': 'required',
        'currency': 'required',
        'pay_date': 'required',
        'pay_receive': 'required'
    }

    def __init__(self, amount=None, currency=None, pay_date=None, pay_receive=None, local_vars_configuration=None):  # noqa: E501
        """AdditionalPayment - a model defined in OpenAPI"
        
        :param amount:  The upfront amount. (required)
        :type amount: float
        :param currency:  The upfront currency. (required)
        :type currency: str
        :param pay_date:  Date when the upfront is paid. (required)
        :type pay_date: datetime
        :param pay_receive:  Is it pay or receive.    Supported string (enumeration) values are: [Pay, Receive]. (required)
        :type pay_receive: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._amount = None
        self._currency = None
        self._pay_date = None
        self._pay_receive = None
        self.discriminator = None

        self.amount = amount
        self.currency = currency
        self.pay_date = pay_date
        self.pay_receive = pay_receive

    @property
    def amount(self):
        """Gets the amount of this AdditionalPayment.  # noqa: E501

        The upfront amount.  # noqa: E501

        :return: The amount of this AdditionalPayment.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this AdditionalPayment.

        The upfront amount.  # noqa: E501

        :param amount: The amount of this AdditionalPayment.  # noqa: E501
        :type amount: float
        """
        if self.local_vars_configuration.client_side_validation and amount is None:  # noqa: E501
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def currency(self):
        """Gets the currency of this AdditionalPayment.  # noqa: E501

        The upfront currency.  # noqa: E501

        :return: The currency of this AdditionalPayment.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this AdditionalPayment.

        The upfront currency.  # noqa: E501

        :param currency: The currency of this AdditionalPayment.  # noqa: E501
        :type currency: str
        """
        if self.local_vars_configuration.client_side_validation and currency is None:  # noqa: E501
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def pay_date(self):
        """Gets the pay_date of this AdditionalPayment.  # noqa: E501

        Date when the upfront is paid.  # noqa: E501

        :return: The pay_date of this AdditionalPayment.  # noqa: E501
        :rtype: datetime
        """
        return self._pay_date

    @pay_date.setter
    def pay_date(self, pay_date):
        """Sets the pay_date of this AdditionalPayment.

        Date when the upfront is paid.  # noqa: E501

        :param pay_date: The pay_date of this AdditionalPayment.  # noqa: E501
        :type pay_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and pay_date is None:  # noqa: E501
            raise ValueError("Invalid value for `pay_date`, must not be `None`")  # noqa: E501

        self._pay_date = pay_date

    @property
    def pay_receive(self):
        """Gets the pay_receive of this AdditionalPayment.  # noqa: E501

        Is it pay or receive.    Supported string (enumeration) values are: [Pay, Receive].  # noqa: E501

        :return: The pay_receive of this AdditionalPayment.  # noqa: E501
        :rtype: str
        """
        return self._pay_receive

    @pay_receive.setter
    def pay_receive(self, pay_receive):
        """Sets the pay_receive of this AdditionalPayment.

        Is it pay or receive.    Supported string (enumeration) values are: [Pay, Receive].  # noqa: E501

        :param pay_receive: The pay_receive of this AdditionalPayment.  # noqa: E501
        :type pay_receive: str
        """
        if self.local_vars_configuration.client_side_validation and pay_receive is None:  # noqa: E501
            raise ValueError("Invalid value for `pay_receive`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                pay_receive is not None and len(pay_receive) < 1):
            raise ValueError("Invalid value for `pay_receive`, length must be greater than or equal to `1`")  # noqa: E501

        self._pay_receive = pay_receive

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
        if not isinstance(other, AdditionalPayment):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AdditionalPayment):
            return True

        return self.to_dict() != other.to_dict()
