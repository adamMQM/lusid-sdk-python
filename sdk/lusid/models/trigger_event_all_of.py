# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.0.610
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


class TriggerEventAllOf(object):
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
        'level': 'float',
        'trigger_type': 'str',
        'trigger_direction': 'str',
        'trigger_date': 'datetime',
        'maturity_date': 'datetime',
        'instrument_event_type': 'str'
    }

    attribute_map = {
        'level': 'level',
        'trigger_type': 'triggerType',
        'trigger_direction': 'triggerDirection',
        'trigger_date': 'triggerDate',
        'maturity_date': 'maturityDate',
        'instrument_event_type': 'instrumentEventType'
    }

    required_map = {
        'level': 'required',
        'trigger_type': 'required',
        'trigger_direction': 'required',
        'trigger_date': 'required',
        'maturity_date': 'required',
        'instrument_event_type': 'required'
    }

    def __init__(self, level=None, trigger_type=None, trigger_direction=None, trigger_date=None, maturity_date=None, instrument_event_type=None, local_vars_configuration=None):  # noqa: E501
        """TriggerEventAllOf - a model defined in OpenAPI"
        
        :param level:  The underlying price level that triggers the event (required)
        :type level: float
        :param trigger_type:  The type of the trigger; valid options are Knock-In, Knock-Out, Touch or No-Touch (required)
        :type trigger_type: str
        :param trigger_direction:  The direction of the trigger; valid options are Up and Down (required)
        :type trigger_direction: str
        :param trigger_date:  The date the trigger happens at. (required)
        :type trigger_date: datetime
        :param maturity_date:  The date the trigger takes effect. (required)
        :type maturity_date: datetime
        :param instrument_event_type:  The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent (required)
        :type instrument_event_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._level = None
        self._trigger_type = None
        self._trigger_direction = None
        self._trigger_date = None
        self._maturity_date = None
        self._instrument_event_type = None
        self.discriminator = None

        self.level = level
        self.trigger_type = trigger_type
        self.trigger_direction = trigger_direction
        self.trigger_date = trigger_date
        self.maturity_date = maturity_date
        self.instrument_event_type = instrument_event_type

    @property
    def level(self):
        """Gets the level of this TriggerEventAllOf.  # noqa: E501

        The underlying price level that triggers the event  # noqa: E501

        :return: The level of this TriggerEventAllOf.  # noqa: E501
        :rtype: float
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this TriggerEventAllOf.

        The underlying price level that triggers the event  # noqa: E501

        :param level: The level of this TriggerEventAllOf.  # noqa: E501
        :type level: float
        """
        if self.local_vars_configuration.client_side_validation and level is None:  # noqa: E501
            raise ValueError("Invalid value for `level`, must not be `None`")  # noqa: E501

        self._level = level

    @property
    def trigger_type(self):
        """Gets the trigger_type of this TriggerEventAllOf.  # noqa: E501

        The type of the trigger; valid options are Knock-In, Knock-Out, Touch or No-Touch  # noqa: E501

        :return: The trigger_type of this TriggerEventAllOf.  # noqa: E501
        :rtype: str
        """
        return self._trigger_type

    @trigger_type.setter
    def trigger_type(self, trigger_type):
        """Sets the trigger_type of this TriggerEventAllOf.

        The type of the trigger; valid options are Knock-In, Knock-Out, Touch or No-Touch  # noqa: E501

        :param trigger_type: The trigger_type of this TriggerEventAllOf.  # noqa: E501
        :type trigger_type: str
        """
        if self.local_vars_configuration.client_side_validation and trigger_type is None:  # noqa: E501
            raise ValueError("Invalid value for `trigger_type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                trigger_type is not None and len(trigger_type) < 1):
            raise ValueError("Invalid value for `trigger_type`, length must be greater than or equal to `1`")  # noqa: E501

        self._trigger_type = trigger_type

    @property
    def trigger_direction(self):
        """Gets the trigger_direction of this TriggerEventAllOf.  # noqa: E501

        The direction of the trigger; valid options are Up and Down  # noqa: E501

        :return: The trigger_direction of this TriggerEventAllOf.  # noqa: E501
        :rtype: str
        """
        return self._trigger_direction

    @trigger_direction.setter
    def trigger_direction(self, trigger_direction):
        """Sets the trigger_direction of this TriggerEventAllOf.

        The direction of the trigger; valid options are Up and Down  # noqa: E501

        :param trigger_direction: The trigger_direction of this TriggerEventAllOf.  # noqa: E501
        :type trigger_direction: str
        """
        if self.local_vars_configuration.client_side_validation and trigger_direction is None:  # noqa: E501
            raise ValueError("Invalid value for `trigger_direction`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                trigger_direction is not None and len(trigger_direction) < 1):
            raise ValueError("Invalid value for `trigger_direction`, length must be greater than or equal to `1`")  # noqa: E501

        self._trigger_direction = trigger_direction

    @property
    def trigger_date(self):
        """Gets the trigger_date of this TriggerEventAllOf.  # noqa: E501

        The date the trigger happens at.  # noqa: E501

        :return: The trigger_date of this TriggerEventAllOf.  # noqa: E501
        :rtype: datetime
        """
        return self._trigger_date

    @trigger_date.setter
    def trigger_date(self, trigger_date):
        """Sets the trigger_date of this TriggerEventAllOf.

        The date the trigger happens at.  # noqa: E501

        :param trigger_date: The trigger_date of this TriggerEventAllOf.  # noqa: E501
        :type trigger_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and trigger_date is None:  # noqa: E501
            raise ValueError("Invalid value for `trigger_date`, must not be `None`")  # noqa: E501

        self._trigger_date = trigger_date

    @property
    def maturity_date(self):
        """Gets the maturity_date of this TriggerEventAllOf.  # noqa: E501

        The date the trigger takes effect.  # noqa: E501

        :return: The maturity_date of this TriggerEventAllOf.  # noqa: E501
        :rtype: datetime
        """
        return self._maturity_date

    @maturity_date.setter
    def maturity_date(self, maturity_date):
        """Sets the maturity_date of this TriggerEventAllOf.

        The date the trigger takes effect.  # noqa: E501

        :param maturity_date: The maturity_date of this TriggerEventAllOf.  # noqa: E501
        :type maturity_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and maturity_date is None:  # noqa: E501
            raise ValueError("Invalid value for `maturity_date`, must not be `None`")  # noqa: E501

        self._maturity_date = maturity_date

    @property
    def instrument_event_type(self):
        """Gets the instrument_event_type of this TriggerEventAllOf.  # noqa: E501

        The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent  # noqa: E501

        :return: The instrument_event_type of this TriggerEventAllOf.  # noqa: E501
        :rtype: str
        """
        return self._instrument_event_type

    @instrument_event_type.setter
    def instrument_event_type(self, instrument_event_type):
        """Sets the instrument_event_type of this TriggerEventAllOf.

        The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent  # noqa: E501

        :param instrument_event_type: The instrument_event_type of this TriggerEventAllOf.  # noqa: E501
        :type instrument_event_type: str
        """
        if self.local_vars_configuration.client_side_validation and instrument_event_type is None:  # noqa: E501
            raise ValueError("Invalid value for `instrument_event_type`, must not be `None`")  # noqa: E501
        allowed_values = ["TransitionEvent", "InformationalEvent", "OpenEvent", "CloseEvent", "StockSplitEvent", "BondDefaultEvent", "CashDividendEvent", "AmortisationEvent", "CashFlowEvent", "ExerciseEvent", "ResetEvent", "TriggerEvent", "RawVendorEvent", "InformationalErrorEvent"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and instrument_event_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `instrument_event_type` ({0}), must be one of {1}"  # noqa: E501
                .format(instrument_event_type, allowed_values)
            )

        self._instrument_event_type = instrument_event_type

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
        if not isinstance(other, TriggerEventAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TriggerEventAllOf):
            return True

        return self.to_dict() != other.to_dict()
