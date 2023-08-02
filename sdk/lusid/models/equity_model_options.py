# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.0.402
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


class EquityModelOptions(object):
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
        'equity_forward_projection_type': 'str',
        'model_options_type': 'str'
    }

    attribute_map = {
        'equity_forward_projection_type': 'equityForwardProjectionType',
        'model_options_type': 'modelOptionsType'
    }

    required_map = {
        'equity_forward_projection_type': 'required',
        'model_options_type': 'required'
    }

    def __init__(self, equity_forward_projection_type=None, model_options_type=None, local_vars_configuration=None):  # noqa: E501
        """EquityModelOptions - a model defined in OpenAPI"
        
        :param equity_forward_projection_type:  Determines how forward equity prices should be projected.                Supported string (enumeration) values are: [FlatForwardCurveFromSpot, EquityCurveByPrices, ForwardProjectedFromRatesCurve]. (required)
        :type equity_forward_projection_type: str
        :param model_options_type:  The available values are: Invalid, OpaqueModelOptions, EmptyModelOptions, IndexModelOptions, FxForwardModelOptions, FundingLegModelOptions, EquityModelOptions, LookUpPricingModelOptions (required)
        :type model_options_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._equity_forward_projection_type = None
        self._model_options_type = None
        self.discriminator = None

        self.equity_forward_projection_type = equity_forward_projection_type
        self.model_options_type = model_options_type

    @property
    def equity_forward_projection_type(self):
        """Gets the equity_forward_projection_type of this EquityModelOptions.  # noqa: E501

        Determines how forward equity prices should be projected.                Supported string (enumeration) values are: [FlatForwardCurveFromSpot, EquityCurveByPrices, ForwardProjectedFromRatesCurve].  # noqa: E501

        :return: The equity_forward_projection_type of this EquityModelOptions.  # noqa: E501
        :rtype: str
        """
        return self._equity_forward_projection_type

    @equity_forward_projection_type.setter
    def equity_forward_projection_type(self, equity_forward_projection_type):
        """Sets the equity_forward_projection_type of this EquityModelOptions.

        Determines how forward equity prices should be projected.                Supported string (enumeration) values are: [FlatForwardCurveFromSpot, EquityCurveByPrices, ForwardProjectedFromRatesCurve].  # noqa: E501

        :param equity_forward_projection_type: The equity_forward_projection_type of this EquityModelOptions.  # noqa: E501
        :type equity_forward_projection_type: str
        """
        if self.local_vars_configuration.client_side_validation and equity_forward_projection_type is None:  # noqa: E501
            raise ValueError("Invalid value for `equity_forward_projection_type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                equity_forward_projection_type is not None and len(equity_forward_projection_type) < 1):
            raise ValueError("Invalid value for `equity_forward_projection_type`, length must be greater than or equal to `1`")  # noqa: E501

        self._equity_forward_projection_type = equity_forward_projection_type

    @property
    def model_options_type(self):
        """Gets the model_options_type of this EquityModelOptions.  # noqa: E501

        The available values are: Invalid, OpaqueModelOptions, EmptyModelOptions, IndexModelOptions, FxForwardModelOptions, FundingLegModelOptions, EquityModelOptions, LookUpPricingModelOptions  # noqa: E501

        :return: The model_options_type of this EquityModelOptions.  # noqa: E501
        :rtype: str
        """
        return self._model_options_type

    @model_options_type.setter
    def model_options_type(self, model_options_type):
        """Sets the model_options_type of this EquityModelOptions.

        The available values are: Invalid, OpaqueModelOptions, EmptyModelOptions, IndexModelOptions, FxForwardModelOptions, FundingLegModelOptions, EquityModelOptions, LookUpPricingModelOptions  # noqa: E501

        :param model_options_type: The model_options_type of this EquityModelOptions.  # noqa: E501
        :type model_options_type: str
        """
        if self.local_vars_configuration.client_side_validation and model_options_type is None:  # noqa: E501
            raise ValueError("Invalid value for `model_options_type`, must not be `None`")  # noqa: E501
        allowed_values = ["Invalid", "OpaqueModelOptions", "EmptyModelOptions", "IndexModelOptions", "FxForwardModelOptions", "FundingLegModelOptions", "EquityModelOptions", "LookUpPricingModelOptions"]  # noqa: E501
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
        if not isinstance(other, EquityModelOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EquityModelOptions):
            return True

        return self.to_dict() != other.to_dict()
