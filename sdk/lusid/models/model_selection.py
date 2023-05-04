# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.0.134
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


class ModelSelection(object):
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
        'library': 'str',
        'model': 'str'
    }

    attribute_map = {
        'library': 'library',
        'model': 'model'
    }

    required_map = {
        'library': 'required',
        'model': 'required'
    }

    def __init__(self, library=None, model=None, local_vars_configuration=None):  # noqa: E501
        """ModelSelection - a model defined in OpenAPI"
        
        :param library:  The available values are: Lusid, RefinitivQps, RefinitivTracsWeb, VolMaster, IsdaCds, YieldBook, LusidCalc (required)
        :type library: str
        :param model:  The available values are: SimpleStatic, Discounting, VendorDefault, BlackScholes, ConstantTimeValueOfMoney, Bachelier, ForwardWithPoints, ForwardWithPointsUndiscounted, ForwardSpecifiedRate, ForwardSpecifiedRateUndiscounted, IndexNav, IndexPrice, InlinedIndex, ForwardFromCurve, ForwardFromCurveUndiscounted, BlackScholesDigital, BjerksundStensland1993 (required)
        :type model: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._library = None
        self._model = None
        self.discriminator = None

        self.library = library
        self.model = model

    @property
    def library(self):
        """Gets the library of this ModelSelection.  # noqa: E501

        The available values are: Lusid, RefinitivQps, RefinitivTracsWeb, VolMaster, IsdaCds, YieldBook, LusidCalc  # noqa: E501

        :return: The library of this ModelSelection.  # noqa: E501
        :rtype: str
        """
        return self._library

    @library.setter
    def library(self, library):
        """Sets the library of this ModelSelection.

        The available values are: Lusid, RefinitivQps, RefinitivTracsWeb, VolMaster, IsdaCds, YieldBook, LusidCalc  # noqa: E501

        :param library: The library of this ModelSelection.  # noqa: E501
        :type library: str
        """
        if self.local_vars_configuration.client_side_validation and library is None:  # noqa: E501
            raise ValueError("Invalid value for `library`, must not be `None`")  # noqa: E501
        allowed_values = ["Lusid", "RefinitivQps", "RefinitivTracsWeb", "VolMaster", "IsdaCds", "YieldBook", "LusidCalc"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and library not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `library` ({0}), must be one of {1}"  # noqa: E501
                .format(library, allowed_values)
            )

        self._library = library

    @property
    def model(self):
        """Gets the model of this ModelSelection.  # noqa: E501

        The available values are: SimpleStatic, Discounting, VendorDefault, BlackScholes, ConstantTimeValueOfMoney, Bachelier, ForwardWithPoints, ForwardWithPointsUndiscounted, ForwardSpecifiedRate, ForwardSpecifiedRateUndiscounted, IndexNav, IndexPrice, InlinedIndex, ForwardFromCurve, ForwardFromCurveUndiscounted, BlackScholesDigital, BjerksundStensland1993  # noqa: E501

        :return: The model of this ModelSelection.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this ModelSelection.

        The available values are: SimpleStatic, Discounting, VendorDefault, BlackScholes, ConstantTimeValueOfMoney, Bachelier, ForwardWithPoints, ForwardWithPointsUndiscounted, ForwardSpecifiedRate, ForwardSpecifiedRateUndiscounted, IndexNav, IndexPrice, InlinedIndex, ForwardFromCurve, ForwardFromCurveUndiscounted, BlackScholesDigital, BjerksundStensland1993  # noqa: E501

        :param model: The model of this ModelSelection.  # noqa: E501
        :type model: str
        """
        if self.local_vars_configuration.client_side_validation and model is None:  # noqa: E501
            raise ValueError("Invalid value for `model`, must not be `None`")  # noqa: E501
        allowed_values = ["SimpleStatic", "Discounting", "VendorDefault", "BlackScholes", "ConstantTimeValueOfMoney", "Bachelier", "ForwardWithPoints", "ForwardWithPointsUndiscounted", "ForwardSpecifiedRate", "ForwardSpecifiedRateUndiscounted", "IndexNav", "IndexPrice", "InlinedIndex", "ForwardFromCurve", "ForwardFromCurveUndiscounted", "BlackScholesDigital", "BjerksundStensland1993"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and model not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `model` ({0}), must be one of {1}"  # noqa: E501
                .format(model, allowed_values)
            )

        self._model = model

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
        if not isinstance(other, ModelSelection):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelSelection):
            return True

        return self.to_dict() != other.to_dict()
