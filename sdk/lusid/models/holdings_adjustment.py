# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.0.574
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


class HoldingsAdjustment(object):
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
        'version': 'Version',
        'unmatched_holding_method': 'str',
        'adjustments': 'list[HoldingAdjustment]',
        'links': 'list[Link]'
    }

    attribute_map = {
        'effective_at': 'effectiveAt',
        'version': 'version',
        'unmatched_holding_method': 'unmatchedHoldingMethod',
        'adjustments': 'adjustments',
        'links': 'links'
    }

    required_map = {
        'effective_at': 'required',
        'version': 'required',
        'unmatched_holding_method': 'required',
        'adjustments': 'required',
        'links': 'optional'
    }

    def __init__(self, effective_at=None, version=None, unmatched_holding_method=None, adjustments=None, links=None, local_vars_configuration=None):  # noqa: E501
        """HoldingsAdjustment - a model defined in OpenAPI"
        
        :param effective_at:  The effective datetime from which the adjustment is valid. There can only be one holdings adjustment for a transaction portfolio at a specific effective datetime, so this uniquely identifies the adjustment. (required)
        :type effective_at: datetime
        :param version:  (required)
        :type version: lusid.Version
        :param unmatched_holding_method:  Describes how the holdings were adjusted. If 'PositionToZero' the entire transaction portfolio's holdings were set via a call to 'Set holdings'. If 'KeepTheSame' only the specified holdings were adjusted via a call to 'Adjust holdings'. The available values are: PositionToZero, KeepTheSame (required)
        :type unmatched_holding_method: str
        :param adjustments:  The holding adjustments. (required)
        :type adjustments: list[lusid.HoldingAdjustment]
        :param links:  Collection of links.
        :type links: list[lusid.Link]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._effective_at = None
        self._version = None
        self._unmatched_holding_method = None
        self._adjustments = None
        self._links = None
        self.discriminator = None

        self.effective_at = effective_at
        self.version = version
        self.unmatched_holding_method = unmatched_holding_method
        self.adjustments = adjustments
        self.links = links

    @property
    def effective_at(self):
        """Gets the effective_at of this HoldingsAdjustment.  # noqa: E501

        The effective datetime from which the adjustment is valid. There can only be one holdings adjustment for a transaction portfolio at a specific effective datetime, so this uniquely identifies the adjustment.  # noqa: E501

        :return: The effective_at of this HoldingsAdjustment.  # noqa: E501
        :rtype: datetime
        """
        return self._effective_at

    @effective_at.setter
    def effective_at(self, effective_at):
        """Sets the effective_at of this HoldingsAdjustment.

        The effective datetime from which the adjustment is valid. There can only be one holdings adjustment for a transaction portfolio at a specific effective datetime, so this uniquely identifies the adjustment.  # noqa: E501

        :param effective_at: The effective_at of this HoldingsAdjustment.  # noqa: E501
        :type effective_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and effective_at is None:  # noqa: E501
            raise ValueError("Invalid value for `effective_at`, must not be `None`")  # noqa: E501

        self._effective_at = effective_at

    @property
    def version(self):
        """Gets the version of this HoldingsAdjustment.  # noqa: E501


        :return: The version of this HoldingsAdjustment.  # noqa: E501
        :rtype: lusid.Version
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this HoldingsAdjustment.


        :param version: The version of this HoldingsAdjustment.  # noqa: E501
        :type version: lusid.Version
        """
        if self.local_vars_configuration.client_side_validation and version is None:  # noqa: E501
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    @property
    def unmatched_holding_method(self):
        """Gets the unmatched_holding_method of this HoldingsAdjustment.  # noqa: E501

        Describes how the holdings were adjusted. If 'PositionToZero' the entire transaction portfolio's holdings were set via a call to 'Set holdings'. If 'KeepTheSame' only the specified holdings were adjusted via a call to 'Adjust holdings'. The available values are: PositionToZero, KeepTheSame  # noqa: E501

        :return: The unmatched_holding_method of this HoldingsAdjustment.  # noqa: E501
        :rtype: str
        """
        return self._unmatched_holding_method

    @unmatched_holding_method.setter
    def unmatched_holding_method(self, unmatched_holding_method):
        """Sets the unmatched_holding_method of this HoldingsAdjustment.

        Describes how the holdings were adjusted. If 'PositionToZero' the entire transaction portfolio's holdings were set via a call to 'Set holdings'. If 'KeepTheSame' only the specified holdings were adjusted via a call to 'Adjust holdings'. The available values are: PositionToZero, KeepTheSame  # noqa: E501

        :param unmatched_holding_method: The unmatched_holding_method of this HoldingsAdjustment.  # noqa: E501
        :type unmatched_holding_method: str
        """
        if self.local_vars_configuration.client_side_validation and unmatched_holding_method is None:  # noqa: E501
            raise ValueError("Invalid value for `unmatched_holding_method`, must not be `None`")  # noqa: E501
        allowed_values = ["PositionToZero", "KeepTheSame"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and unmatched_holding_method not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `unmatched_holding_method` ({0}), must be one of {1}"  # noqa: E501
                .format(unmatched_holding_method, allowed_values)
            )

        self._unmatched_holding_method = unmatched_holding_method

    @property
    def adjustments(self):
        """Gets the adjustments of this HoldingsAdjustment.  # noqa: E501

        The holding adjustments.  # noqa: E501

        :return: The adjustments of this HoldingsAdjustment.  # noqa: E501
        :rtype: list[lusid.HoldingAdjustment]
        """
        return self._adjustments

    @adjustments.setter
    def adjustments(self, adjustments):
        """Sets the adjustments of this HoldingsAdjustment.

        The holding adjustments.  # noqa: E501

        :param adjustments: The adjustments of this HoldingsAdjustment.  # noqa: E501
        :type adjustments: list[lusid.HoldingAdjustment]
        """
        if self.local_vars_configuration.client_side_validation and adjustments is None:  # noqa: E501
            raise ValueError("Invalid value for `adjustments`, must not be `None`")  # noqa: E501

        self._adjustments = adjustments

    @property
    def links(self):
        """Gets the links of this HoldingsAdjustment.  # noqa: E501

        Collection of links.  # noqa: E501

        :return: The links of this HoldingsAdjustment.  # noqa: E501
        :rtype: list[lusid.Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this HoldingsAdjustment.

        Collection of links.  # noqa: E501

        :param links: The links of this HoldingsAdjustment.  # noqa: E501
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
        if not isinstance(other, HoldingsAdjustment):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HoldingsAdjustment):
            return True

        return self.to_dict() != other.to_dict()
