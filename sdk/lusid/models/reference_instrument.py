# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.0.242
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


class ReferenceInstrument(object):
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
        'instrument_id': 'str',
        'instrument_id_type': 'str',
        'scope': 'str',
        'instrument_type': 'str'
    }

    attribute_map = {
        'instrument_id': 'instrumentId',
        'instrument_id_type': 'instrumentIdType',
        'scope': 'scope',
        'instrument_type': 'instrumentType'
    }

    required_map = {
        'instrument_id': 'required',
        'instrument_id_type': 'required',
        'scope': 'required',
        'instrument_type': 'required'
    }

    def __init__(self, instrument_id=None, instrument_id_type=None, scope=None, instrument_type=None, local_vars_configuration=None):  # noqa: E501
        """ReferenceInstrument - a model defined in OpenAPI"
        
        :param instrument_id:  The Identifier code (required)
        :type instrument_id: str
        :param instrument_id_type:  The type of the instrument id e.g. LusidInstrument Id (required)
        :type instrument_id_type: str
        :param scope:  Scope for the instrument (optional) (required)
        :type scope: str
        :param instrument_type:  The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan (required)
        :type instrument_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._instrument_id = None
        self._instrument_id_type = None
        self._scope = None
        self._instrument_type = None
        self.discriminator = None

        self.instrument_id = instrument_id
        self.instrument_id_type = instrument_id_type
        self.scope = scope
        self.instrument_type = instrument_type

    @property
    def instrument_id(self):
        """Gets the instrument_id of this ReferenceInstrument.  # noqa: E501

        The Identifier code  # noqa: E501

        :return: The instrument_id of this ReferenceInstrument.  # noqa: E501
        :rtype: str
        """
        return self._instrument_id

    @instrument_id.setter
    def instrument_id(self, instrument_id):
        """Sets the instrument_id of this ReferenceInstrument.

        The Identifier code  # noqa: E501

        :param instrument_id: The instrument_id of this ReferenceInstrument.  # noqa: E501
        :type instrument_id: str
        """
        if self.local_vars_configuration.client_side_validation and instrument_id is None:  # noqa: E501
            raise ValueError("Invalid value for `instrument_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                instrument_id is not None and len(instrument_id) < 1):
            raise ValueError("Invalid value for `instrument_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._instrument_id = instrument_id

    @property
    def instrument_id_type(self):
        """Gets the instrument_id_type of this ReferenceInstrument.  # noqa: E501

        The type of the instrument id e.g. LusidInstrument Id  # noqa: E501

        :return: The instrument_id_type of this ReferenceInstrument.  # noqa: E501
        :rtype: str
        """
        return self._instrument_id_type

    @instrument_id_type.setter
    def instrument_id_type(self, instrument_id_type):
        """Sets the instrument_id_type of this ReferenceInstrument.

        The type of the instrument id e.g. LusidInstrument Id  # noqa: E501

        :param instrument_id_type: The instrument_id_type of this ReferenceInstrument.  # noqa: E501
        :type instrument_id_type: str
        """
        if self.local_vars_configuration.client_side_validation and instrument_id_type is None:  # noqa: E501
            raise ValueError("Invalid value for `instrument_id_type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                instrument_id_type is not None and len(instrument_id_type) < 1):
            raise ValueError("Invalid value for `instrument_id_type`, length must be greater than or equal to `1`")  # noqa: E501

        self._instrument_id_type = instrument_id_type

    @property
    def scope(self):
        """Gets the scope of this ReferenceInstrument.  # noqa: E501

        Scope for the instrument (optional)  # noqa: E501

        :return: The scope of this ReferenceInstrument.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this ReferenceInstrument.

        Scope for the instrument (optional)  # noqa: E501

        :param scope: The scope of this ReferenceInstrument.  # noqa: E501
        :type scope: str
        """
        if self.local_vars_configuration.client_side_validation and scope is None:  # noqa: E501
            raise ValueError("Invalid value for `scope`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                scope is not None and len(scope) < 1):
            raise ValueError("Invalid value for `scope`, length must be greater than or equal to `1`")  # noqa: E501

        self._scope = scope

    @property
    def instrument_type(self):
        """Gets the instrument_type of this ReferenceInstrument.  # noqa: E501

        The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan  # noqa: E501

        :return: The instrument_type of this ReferenceInstrument.  # noqa: E501
        :rtype: str
        """
        return self._instrument_type

    @instrument_type.setter
    def instrument_type(self, instrument_type):
        """Sets the instrument_type of this ReferenceInstrument.

        The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan  # noqa: E501

        :param instrument_type: The instrument_type of this ReferenceInstrument.  # noqa: E501
        :type instrument_type: str
        """
        if self.local_vars_configuration.client_side_validation and instrument_type is None:  # noqa: E501
            raise ValueError("Invalid value for `instrument_type`, must not be `None`")  # noqa: E501
        allowed_values = ["QuotedSecurity", "InterestRateSwap", "FxForward", "Future", "ExoticInstrument", "FxOption", "CreditDefaultSwap", "InterestRateSwaption", "Bond", "EquityOption", "FixedLeg", "FloatingLeg", "BespokeCashFlowsLeg", "Unknown", "TermDeposit", "ContractForDifference", "EquitySwap", "CashPerpetual", "CapFloor", "CashSettled", "CdsIndex", "Basket", "FundingLeg", "FxSwap", "ForwardRateAgreement", "SimpleInstrument", "Repo", "Equity", "ExchangeTradedOption", "ReferenceInstrument", "ComplexBond", "InflationLinkedBond", "InflationSwap", "SimpleCashFlowLoan"]  # noqa: E501
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
        if not isinstance(other, ReferenceInstrument):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReferenceInstrument):
            return True

        return self.to_dict() != other.to_dict()
