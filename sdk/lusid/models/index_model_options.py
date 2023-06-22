# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.0.282
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


class IndexModelOptions(object):
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
        'portfolio_scaling': 'str',
        'model_options_type': 'str'
    }

    attribute_map = {
        'portfolio_scaling': 'portfolioScaling',
        'model_options_type': 'modelOptionsType'
    }

    required_map = {
        'portfolio_scaling': 'required',
        'model_options_type': 'required'
    }

    def __init__(self, portfolio_scaling=None, model_options_type=None, local_vars_configuration=None):  # noqa: E501
        """IndexModelOptions - a model defined in OpenAPI"
        
        :param portfolio_scaling:  The available values are: Sum, AbsoluteSum, Unity (required)
        :type portfolio_scaling: str
        :param model_options_type:  The available values are: Invalid, OpaqueModelOptions, EmptyModelOptions, IndexModelOptions, FxForwardModelOptions, FundingLegModelOptions, EquityModelOptions (required)
        :type model_options_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._portfolio_scaling = None
        self._model_options_type = None
        self.discriminator = None

        self.portfolio_scaling = portfolio_scaling
        self.model_options_type = model_options_type

    @property
    def portfolio_scaling(self):
        """Gets the portfolio_scaling of this IndexModelOptions.  # noqa: E501

        The available values are: Sum, AbsoluteSum, Unity  # noqa: E501

        :return: The portfolio_scaling of this IndexModelOptions.  # noqa: E501
        :rtype: str
        """
        return self._portfolio_scaling

    @portfolio_scaling.setter
    def portfolio_scaling(self, portfolio_scaling):
        """Sets the portfolio_scaling of this IndexModelOptions.

        The available values are: Sum, AbsoluteSum, Unity  # noqa: E501

        :param portfolio_scaling: The portfolio_scaling of this IndexModelOptions.  # noqa: E501
        :type portfolio_scaling: str
        """
        if self.local_vars_configuration.client_side_validation and portfolio_scaling is None:  # noqa: E501
            raise ValueError("Invalid value for `portfolio_scaling`, must not be `None`")  # noqa: E501
        allowed_values = ["Sum", "AbsoluteSum", "Unity"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and portfolio_scaling not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `portfolio_scaling` ({0}), must be one of {1}"  # noqa: E501
                .format(portfolio_scaling, allowed_values)
            )

        self._portfolio_scaling = portfolio_scaling

    @property
    def model_options_type(self):
        """Gets the model_options_type of this IndexModelOptions.  # noqa: E501

        The available values are: Invalid, OpaqueModelOptions, EmptyModelOptions, IndexModelOptions, FxForwardModelOptions, FundingLegModelOptions, EquityModelOptions  # noqa: E501

        :return: The model_options_type of this IndexModelOptions.  # noqa: E501
        :rtype: str
        """
        return self._model_options_type

    @model_options_type.setter
    def model_options_type(self, model_options_type):
        """Sets the model_options_type of this IndexModelOptions.

        The available values are: Invalid, OpaqueModelOptions, EmptyModelOptions, IndexModelOptions, FxForwardModelOptions, FundingLegModelOptions, EquityModelOptions  # noqa: E501

        :param model_options_type: The model_options_type of this IndexModelOptions.  # noqa: E501
        :type model_options_type: str
        """
        if self.local_vars_configuration.client_side_validation and model_options_type is None:  # noqa: E501
            raise ValueError("Invalid value for `model_options_type`, must not be `None`")  # noqa: E501
        allowed_values = ["Invalid", "OpaqueModelOptions", "EmptyModelOptions", "IndexModelOptions", "FxForwardModelOptions", "FundingLegModelOptions", "EquityModelOptions"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and model_options_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `model_options_type` ({0}), must be one of {1}"  # noqa: E501
                .format(model_options_type, allowed_values)
            )

        self._model_options_type = model_options_type

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
        if not isinstance(other, IndexModelOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IndexModelOptions):
            return True

        return self.to_dict() != other.to_dict()
