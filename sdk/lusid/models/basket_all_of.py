# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.5001
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


class BasketAllOf(object):
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
        'basket_name': 'BasketIdentifier',
        'basket_type': 'str',
        'weighted_instruments': 'WeightedInstruments',
        'instrument_type': 'str'
    }

    attribute_map = {
        'basket_name': 'basketName',
        'basket_type': 'basketType',
        'weighted_instruments': 'weightedInstruments',
        'instrument_type': 'instrumentType'
    }

    required_map = {
        'basket_name': 'required',
        'basket_type': 'required',
        'weighted_instruments': 'required',
        'instrument_type': 'required'
    }

    def __init__(self, basket_name=None, basket_type=None, weighted_instruments=None, instrument_type=None, local_vars_configuration=None):  # noqa: E501
        """BasketAllOf - a model defined in OpenAPI"
        
        :param basket_name:  (required)
        :type basket_name: lusid.BasketIdentifier
        :param basket_type:  What contents does the basket have. The validation will check that the instrument types contained match those expected.    Supported string (enumeration) values are: [Bonds, Credits, Equities, EquitySwap]. (required)
        :type basket_type: str
        :param weighted_instruments:  (required)
        :type weighted_instruments: lusid.WeightedInstruments
        :param instrument_type:  The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap (required)
        :type instrument_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._basket_name = None
        self._basket_type = None
        self._weighted_instruments = None
        self._instrument_type = None
        self.discriminator = None

        self.basket_name = basket_name
        self.basket_type = basket_type
        self.weighted_instruments = weighted_instruments
        self.instrument_type = instrument_type

    @property
    def basket_name(self):
        """Gets the basket_name of this BasketAllOf.  # noqa: E501


        :return: The basket_name of this BasketAllOf.  # noqa: E501
        :rtype: lusid.BasketIdentifier
        """
        return self._basket_name

    @basket_name.setter
    def basket_name(self, basket_name):
        """Sets the basket_name of this BasketAllOf.


        :param basket_name: The basket_name of this BasketAllOf.  # noqa: E501
        :type basket_name: lusid.BasketIdentifier
        """
        if self.local_vars_configuration.client_side_validation and basket_name is None:  # noqa: E501
            raise ValueError("Invalid value for `basket_name`, must not be `None`")  # noqa: E501

        self._basket_name = basket_name

    @property
    def basket_type(self):
        """Gets the basket_type of this BasketAllOf.  # noqa: E501

        What contents does the basket have. The validation will check that the instrument types contained match those expected.    Supported string (enumeration) values are: [Bonds, Credits, Equities, EquitySwap].  # noqa: E501

        :return: The basket_type of this BasketAllOf.  # noqa: E501
        :rtype: str
        """
        return self._basket_type

    @basket_type.setter
    def basket_type(self, basket_type):
        """Sets the basket_type of this BasketAllOf.

        What contents does the basket have. The validation will check that the instrument types contained match those expected.    Supported string (enumeration) values are: [Bonds, Credits, Equities, EquitySwap].  # noqa: E501

        :param basket_type: The basket_type of this BasketAllOf.  # noqa: E501
        :type basket_type: str
        """
        if self.local_vars_configuration.client_side_validation and basket_type is None:  # noqa: E501
            raise ValueError("Invalid value for `basket_type`, must not be `None`")  # noqa: E501

        self._basket_type = basket_type

    @property
    def weighted_instruments(self):
        """Gets the weighted_instruments of this BasketAllOf.  # noqa: E501


        :return: The weighted_instruments of this BasketAllOf.  # noqa: E501
        :rtype: lusid.WeightedInstruments
        """
        return self._weighted_instruments

    @weighted_instruments.setter
    def weighted_instruments(self, weighted_instruments):
        """Sets the weighted_instruments of this BasketAllOf.


        :param weighted_instruments: The weighted_instruments of this BasketAllOf.  # noqa: E501
        :type weighted_instruments: lusid.WeightedInstruments
        """
        if self.local_vars_configuration.client_side_validation and weighted_instruments is None:  # noqa: E501
            raise ValueError("Invalid value for `weighted_instruments`, must not be `None`")  # noqa: E501

        self._weighted_instruments = weighted_instruments

    @property
    def instrument_type(self):
        """Gets the instrument_type of this BasketAllOf.  # noqa: E501

        The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap  # noqa: E501

        :return: The instrument_type of this BasketAllOf.  # noqa: E501
        :rtype: str
        """
        return self._instrument_type

    @instrument_type.setter
    def instrument_type(self, instrument_type):
        """Sets the instrument_type of this BasketAllOf.

        The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap  # noqa: E501

        :param instrument_type: The instrument_type of this BasketAllOf.  # noqa: E501
        :type instrument_type: str
        """
        if self.local_vars_configuration.client_side_validation and instrument_type is None:  # noqa: E501
            raise ValueError("Invalid value for `instrument_type`, must not be `None`")  # noqa: E501
        allowed_values = ["QuotedSecurity", "InterestRateSwap", "FxForward", "Future", "ExoticInstrument", "FxOption", "CreditDefaultSwap", "InterestRateSwaption", "Bond", "EquityOption", "FixedLeg", "FloatingLeg", "BespokeCashFlowsLeg", "Unknown", "TermDeposit", "ContractForDifference", "EquitySwap", "CashPerpetual", "CapFloor", "CashSettled", "CdsIndex", "Basket", "FundingLeg", "FxSwap", "ForwardRateAgreement", "SimpleInstrument", "Repo", "Equity", "ExchangeTradedOption", "ReferenceInstrument", "ComplexBond", "InflationLinkedBond", "InflationSwap"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and instrument_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `instrument_type` ({0}), must be one of {1}"  # noqa: E501
                .format(instrument_type, allowed_values)
            )

        self._instrument_type = instrument_type

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
        if not isinstance(other, BasketAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BasketAllOf):
            return True

        return self.to_dict() != other.to_dict()
