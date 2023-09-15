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


class PortfolioReturnBreakdown(object):
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
        'portfolio_id': 'ResourceId',
        'rate_of_return': 'float',
        'opening_market_value': 'float',
        'closing_market_value': 'float',
        'weight': 'float',
        'constituents_in_the_composite': 'int',
        'constituents_missing': 'int',
        'currency': 'str',
        'open_fx_rate': 'float',
        'close_fx_rate': 'float',
        'local_rate_of_return': 'float',
        'local_opening_market_value': 'float',
        'local_closing_market_value': 'float'
    }

    attribute_map = {
        'portfolio_id': 'portfolioId',
        'rate_of_return': 'rateOfReturn',
        'opening_market_value': 'openingMarketValue',
        'closing_market_value': 'closingMarketValue',
        'weight': 'weight',
        'constituents_in_the_composite': 'constituentsInTheComposite',
        'constituents_missing': 'constituentsMissing',
        'currency': 'currency',
        'open_fx_rate': 'openFxRate',
        'close_fx_rate': 'closeFxRate',
        'local_rate_of_return': 'localRateOfReturn',
        'local_opening_market_value': 'localOpeningMarketValue',
        'local_closing_market_value': 'localClosingMarketValue'
    }

    required_map = {
        'portfolio_id': 'required',
        'rate_of_return': 'optional',
        'opening_market_value': 'optional',
        'closing_market_value': 'optional',
        'weight': 'optional',
        'constituents_in_the_composite': 'optional',
        'constituents_missing': 'optional',
        'currency': 'optional',
        'open_fx_rate': 'optional',
        'close_fx_rate': 'optional',
        'local_rate_of_return': 'optional',
        'local_opening_market_value': 'optional',
        'local_closing_market_value': 'optional'
    }

    def __init__(self, portfolio_id=None, rate_of_return=None, opening_market_value=None, closing_market_value=None, weight=None, constituents_in_the_composite=None, constituents_missing=None, currency=None, open_fx_rate=None, close_fx_rate=None, local_rate_of_return=None, local_opening_market_value=None, local_closing_market_value=None, local_vars_configuration=None):  # noqa: E501
        """PortfolioReturnBreakdown - a model defined in OpenAPI"
        
        :param portfolio_id:  (required)
        :type portfolio_id: lusid.ResourceId
        :param rate_of_return:  The return number.
        :type rate_of_return: float
        :param opening_market_value:  The opening market value.
        :type opening_market_value: float
        :param closing_market_value:  The closing market value.
        :type closing_market_value: float
        :param weight:  The weight of the constituent into the composite.
        :type weight: float
        :param constituents_in_the_composite:  The number of members in the Composite on the given day.
        :type constituents_in_the_composite: int
        :param constituents_missing:  The number of the constituents which have a missing return on that day.
        :type constituents_missing: int
        :param currency:  The currency of the portfolio.
        :type currency: str
        :param open_fx_rate:  The opening fxRate which is used in calculation.
        :type open_fx_rate: float
        :param close_fx_rate:  The closing fxRate which is used in calculation.
        :type close_fx_rate: float
        :param local_rate_of_return:  The rate of return in the local currency.
        :type local_rate_of_return: float
        :param local_opening_market_value:  The opening market value in the local currency.
        :type local_opening_market_value: float
        :param local_closing_market_value:  The closing market value in the local currency.
        :type local_closing_market_value: float

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._portfolio_id = None
        self._rate_of_return = None
        self._opening_market_value = None
        self._closing_market_value = None
        self._weight = None
        self._constituents_in_the_composite = None
        self._constituents_missing = None
        self._currency = None
        self._open_fx_rate = None
        self._close_fx_rate = None
        self._local_rate_of_return = None
        self._local_opening_market_value = None
        self._local_closing_market_value = None
        self.discriminator = None

        self.portfolio_id = portfolio_id
        if rate_of_return is not None:
            self.rate_of_return = rate_of_return
        self.opening_market_value = opening_market_value
        self.closing_market_value = closing_market_value
        if weight is not None:
            self.weight = weight
        if constituents_in_the_composite is not None:
            self.constituents_in_the_composite = constituents_in_the_composite
        if constituents_missing is not None:
            self.constituents_missing = constituents_missing
        self.currency = currency
        if open_fx_rate is not None:
            self.open_fx_rate = open_fx_rate
        if close_fx_rate is not None:
            self.close_fx_rate = close_fx_rate
        self.local_rate_of_return = local_rate_of_return
        self.local_opening_market_value = local_opening_market_value
        self.local_closing_market_value = local_closing_market_value

    @property
    def portfolio_id(self):
        """Gets the portfolio_id of this PortfolioReturnBreakdown.  # noqa: E501


        :return: The portfolio_id of this PortfolioReturnBreakdown.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._portfolio_id

    @portfolio_id.setter
    def portfolio_id(self, portfolio_id):
        """Sets the portfolio_id of this PortfolioReturnBreakdown.


        :param portfolio_id: The portfolio_id of this PortfolioReturnBreakdown.  # noqa: E501
        :type portfolio_id: lusid.ResourceId
        """
        if self.local_vars_configuration.client_side_validation and portfolio_id is None:  # noqa: E501
            raise ValueError("Invalid value for `portfolio_id`, must not be `None`")  # noqa: E501

        self._portfolio_id = portfolio_id

    @property
    def rate_of_return(self):
        """Gets the rate_of_return of this PortfolioReturnBreakdown.  # noqa: E501

        The return number.  # noqa: E501

        :return: The rate_of_return of this PortfolioReturnBreakdown.  # noqa: E501
        :rtype: float
        """
        return self._rate_of_return

    @rate_of_return.setter
    def rate_of_return(self, rate_of_return):
        """Sets the rate_of_return of this PortfolioReturnBreakdown.

        The return number.  # noqa: E501

        :param rate_of_return: The rate_of_return of this PortfolioReturnBreakdown.  # noqa: E501
        :type rate_of_return: float
        """

        self._rate_of_return = rate_of_return

    @property
    def opening_market_value(self):
        """Gets the opening_market_value of this PortfolioReturnBreakdown.  # noqa: E501

        The opening market value.  # noqa: E501

        :return: The opening_market_value of this PortfolioReturnBreakdown.  # noqa: E501
        :rtype: float
        """
        return self._opening_market_value

    @opening_market_value.setter
    def opening_market_value(self, opening_market_value):
        """Sets the opening_market_value of this PortfolioReturnBreakdown.

        The opening market value.  # noqa: E501

        :param opening_market_value: The opening_market_value of this PortfolioReturnBreakdown.  # noqa: E501
        :type opening_market_value: float
        """

        self._opening_market_value = opening_market_value

    @property
    def closing_market_value(self):
        """Gets the closing_market_value of this PortfolioReturnBreakdown.  # noqa: E501

        The closing market value.  # noqa: E501

        :return: The closing_market_value of this PortfolioReturnBreakdown.  # noqa: E501
        :rtype: float
        """
        return self._closing_market_value

    @closing_market_value.setter
    def closing_market_value(self, closing_market_value):
        """Sets the closing_market_value of this PortfolioReturnBreakdown.

        The closing market value.  # noqa: E501

        :param closing_market_value: The closing_market_value of this PortfolioReturnBreakdown.  # noqa: E501
        :type closing_market_value: float
        """

        self._closing_market_value = closing_market_value

    @property
    def weight(self):
        """Gets the weight of this PortfolioReturnBreakdown.  # noqa: E501

        The weight of the constituent into the composite.  # noqa: E501

        :return: The weight of this PortfolioReturnBreakdown.  # noqa: E501
        :rtype: float
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this PortfolioReturnBreakdown.

        The weight of the constituent into the composite.  # noqa: E501

        :param weight: The weight of this PortfolioReturnBreakdown.  # noqa: E501
        :type weight: float
        """

        self._weight = weight

    @property
    def constituents_in_the_composite(self):
        """Gets the constituents_in_the_composite of this PortfolioReturnBreakdown.  # noqa: E501

        The number of members in the Composite on the given day.  # noqa: E501

        :return: The constituents_in_the_composite of this PortfolioReturnBreakdown.  # noqa: E501
        :rtype: int
        """
        return self._constituents_in_the_composite

    @constituents_in_the_composite.setter
    def constituents_in_the_composite(self, constituents_in_the_composite):
        """Sets the constituents_in_the_composite of this PortfolioReturnBreakdown.

        The number of members in the Composite on the given day.  # noqa: E501

        :param constituents_in_the_composite: The constituents_in_the_composite of this PortfolioReturnBreakdown.  # noqa: E501
        :type constituents_in_the_composite: int
        """

        self._constituents_in_the_composite = constituents_in_the_composite

    @property
    def constituents_missing(self):
        """Gets the constituents_missing of this PortfolioReturnBreakdown.  # noqa: E501

        The number of the constituents which have a missing return on that day.  # noqa: E501

        :return: The constituents_missing of this PortfolioReturnBreakdown.  # noqa: E501
        :rtype: int
        """
        return self._constituents_missing

    @constituents_missing.setter
    def constituents_missing(self, constituents_missing):
        """Sets the constituents_missing of this PortfolioReturnBreakdown.

        The number of the constituents which have a missing return on that day.  # noqa: E501

        :param constituents_missing: The constituents_missing of this PortfolioReturnBreakdown.  # noqa: E501
        :type constituents_missing: int
        """

        self._constituents_missing = constituents_missing

    @property
    def currency(self):
        """Gets the currency of this PortfolioReturnBreakdown.  # noqa: E501

        The currency of the portfolio.  # noqa: E501

        :return: The currency of this PortfolioReturnBreakdown.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this PortfolioReturnBreakdown.

        The currency of the portfolio.  # noqa: E501

        :param currency: The currency of this PortfolioReturnBreakdown.  # noqa: E501
        :type currency: str
        """

        self._currency = currency

    @property
    def open_fx_rate(self):
        """Gets the open_fx_rate of this PortfolioReturnBreakdown.  # noqa: E501

        The opening fxRate which is used in calculation.  # noqa: E501

        :return: The open_fx_rate of this PortfolioReturnBreakdown.  # noqa: E501
        :rtype: float
        """
        return self._open_fx_rate

    @open_fx_rate.setter
    def open_fx_rate(self, open_fx_rate):
        """Sets the open_fx_rate of this PortfolioReturnBreakdown.

        The opening fxRate which is used in calculation.  # noqa: E501

        :param open_fx_rate: The open_fx_rate of this PortfolioReturnBreakdown.  # noqa: E501
        :type open_fx_rate: float
        """

        self._open_fx_rate = open_fx_rate

    @property
    def close_fx_rate(self):
        """Gets the close_fx_rate of this PortfolioReturnBreakdown.  # noqa: E501

        The closing fxRate which is used in calculation.  # noqa: E501

        :return: The close_fx_rate of this PortfolioReturnBreakdown.  # noqa: E501
        :rtype: float
        """
        return self._close_fx_rate

    @close_fx_rate.setter
    def close_fx_rate(self, close_fx_rate):
        """Sets the close_fx_rate of this PortfolioReturnBreakdown.

        The closing fxRate which is used in calculation.  # noqa: E501

        :param close_fx_rate: The close_fx_rate of this PortfolioReturnBreakdown.  # noqa: E501
        :type close_fx_rate: float
        """

        self._close_fx_rate = close_fx_rate

    @property
    def local_rate_of_return(self):
        """Gets the local_rate_of_return of this PortfolioReturnBreakdown.  # noqa: E501

        The rate of return in the local currency.  # noqa: E501

        :return: The local_rate_of_return of this PortfolioReturnBreakdown.  # noqa: E501
        :rtype: float
        """
        return self._local_rate_of_return

    @local_rate_of_return.setter
    def local_rate_of_return(self, local_rate_of_return):
        """Sets the local_rate_of_return of this PortfolioReturnBreakdown.

        The rate of return in the local currency.  # noqa: E501

        :param local_rate_of_return: The local_rate_of_return of this PortfolioReturnBreakdown.  # noqa: E501
        :type local_rate_of_return: float
        """

        self._local_rate_of_return = local_rate_of_return

    @property
    def local_opening_market_value(self):
        """Gets the local_opening_market_value of this PortfolioReturnBreakdown.  # noqa: E501

        The opening market value in the local currency.  # noqa: E501

        :return: The local_opening_market_value of this PortfolioReturnBreakdown.  # noqa: E501
        :rtype: float
        """
        return self._local_opening_market_value

    @local_opening_market_value.setter
    def local_opening_market_value(self, local_opening_market_value):
        """Sets the local_opening_market_value of this PortfolioReturnBreakdown.

        The opening market value in the local currency.  # noqa: E501

        :param local_opening_market_value: The local_opening_market_value of this PortfolioReturnBreakdown.  # noqa: E501
        :type local_opening_market_value: float
        """

        self._local_opening_market_value = local_opening_market_value

    @property
    def local_closing_market_value(self):
        """Gets the local_closing_market_value of this PortfolioReturnBreakdown.  # noqa: E501

        The closing market value in the local currency.  # noqa: E501

        :return: The local_closing_market_value of this PortfolioReturnBreakdown.  # noqa: E501
        :rtype: float
        """
        return self._local_closing_market_value

    @local_closing_market_value.setter
    def local_closing_market_value(self, local_closing_market_value):
        """Sets the local_closing_market_value of this PortfolioReturnBreakdown.

        The closing market value in the local currency.  # noqa: E501

        :param local_closing_market_value: The local_closing_market_value of this PortfolioReturnBreakdown.  # noqa: E501
        :type local_closing_market_value: float
        """

        self._local_closing_market_value = local_closing_market_value

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
        if not isinstance(other, PortfolioReturnBreakdown):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PortfolioReturnBreakdown):
            return True

        return self.to_dict() != other.to_dict()