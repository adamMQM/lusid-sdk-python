# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.0.454
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


class UpsertInstrumentEventRequest(object):
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
        'instrument_event_id': 'str',
        'instrument_identifiers': 'dict(str, str)',
        'description': 'str',
        'instrument_event': 'InstrumentEvent',
        'properties': 'list[PerpetualProperty]'
    }

    attribute_map = {
        'instrument_event_id': 'instrumentEventId',
        'instrument_identifiers': 'instrumentIdentifiers',
        'description': 'description',
        'instrument_event': 'instrumentEvent',
        'properties': 'properties'
    }

    required_map = {
        'instrument_event_id': 'required',
        'instrument_identifiers': 'required',
        'description': 'optional',
        'instrument_event': 'required',
        'properties': 'optional'
    }

    def __init__(self, instrument_event_id=None, instrument_identifiers=None, description=None, instrument_event=None, properties=None, local_vars_configuration=None):  # noqa: E501
        """UpsertInstrumentEventRequest - a model defined in OpenAPI"
        
        :param instrument_event_id:  Free string that uniquely identifies the event within the corporate action source (required)
        :type instrument_event_id: str
        :param instrument_identifiers:  The set of identifiers which determine the instrument this event relates to. (required)
        :type instrument_identifiers: dict(str, str)
        :param description:  The description of the instrument event.
        :type description: str
        :param instrument_event:  (required)
        :type instrument_event: lusid.InstrumentEvent
        :param properties:  The properties attached to this instrument event.
        :type properties: list[lusid.PerpetualProperty]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._instrument_event_id = None
        self._instrument_identifiers = None
        self._description = None
        self._instrument_event = None
        self._properties = None
        self.discriminator = None

        self.instrument_event_id = instrument_event_id
        self.instrument_identifiers = instrument_identifiers
        self.description = description
        self.instrument_event = instrument_event
        self.properties = properties

    @property
    def instrument_event_id(self):
        """Gets the instrument_event_id of this UpsertInstrumentEventRequest.  # noqa: E501

        Free string that uniquely identifies the event within the corporate action source  # noqa: E501

        :return: The instrument_event_id of this UpsertInstrumentEventRequest.  # noqa: E501
        :rtype: str
        """
        return self._instrument_event_id

    @instrument_event_id.setter
    def instrument_event_id(self, instrument_event_id):
        """Sets the instrument_event_id of this UpsertInstrumentEventRequest.

        Free string that uniquely identifies the event within the corporate action source  # noqa: E501

        :param instrument_event_id: The instrument_event_id of this UpsertInstrumentEventRequest.  # noqa: E501
        :type instrument_event_id: str
        """
        if self.local_vars_configuration.client_side_validation and instrument_event_id is None:  # noqa: E501
            raise ValueError("Invalid value for `instrument_event_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                instrument_event_id is not None and len(instrument_event_id) > 64):
            raise ValueError("Invalid value for `instrument_event_id`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                instrument_event_id is not None and len(instrument_event_id) < 1):
            raise ValueError("Invalid value for `instrument_event_id`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                instrument_event_id is not None and not re.search(r'^[a-zA-Z0-9\-_]+$', instrument_event_id)):  # noqa: E501
            raise ValueError(r"Invalid value for `instrument_event_id`, must be a follow pattern or equal to `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501

        self._instrument_event_id = instrument_event_id

    @property
    def instrument_identifiers(self):
        """Gets the instrument_identifiers of this UpsertInstrumentEventRequest.  # noqa: E501

        The set of identifiers which determine the instrument this event relates to.  # noqa: E501

        :return: The instrument_identifiers of this UpsertInstrumentEventRequest.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._instrument_identifiers

    @instrument_identifiers.setter
    def instrument_identifiers(self, instrument_identifiers):
        """Sets the instrument_identifiers of this UpsertInstrumentEventRequest.

        The set of identifiers which determine the instrument this event relates to.  # noqa: E501

        :param instrument_identifiers: The instrument_identifiers of this UpsertInstrumentEventRequest.  # noqa: E501
        :type instrument_identifiers: dict(str, str)
        """
        if self.local_vars_configuration.client_side_validation and instrument_identifiers is None:  # noqa: E501
            raise ValueError("Invalid value for `instrument_identifiers`, must not be `None`")  # noqa: E501

        self._instrument_identifiers = instrument_identifiers

    @property
    def description(self):
        """Gets the description of this UpsertInstrumentEventRequest.  # noqa: E501

        The description of the instrument event.  # noqa: E501

        :return: The description of this UpsertInstrumentEventRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpsertInstrumentEventRequest.

        The description of the instrument event.  # noqa: E501

        :param description: The description of this UpsertInstrumentEventRequest.  # noqa: E501
        :type description: str
        """
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) > 1024):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `1024`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) < 0):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and not re.search(r'^[\s\S]*$', description)):  # noqa: E501
            raise ValueError(r"Invalid value for `description`, must be a follow pattern or equal to `/^[\s\S]*$/`")  # noqa: E501

        self._description = description

    @property
    def instrument_event(self):
        """Gets the instrument_event of this UpsertInstrumentEventRequest.  # noqa: E501


        :return: The instrument_event of this UpsertInstrumentEventRequest.  # noqa: E501
        :rtype: lusid.InstrumentEvent
        """
        return self._instrument_event

    @instrument_event.setter
    def instrument_event(self, instrument_event):
        """Sets the instrument_event of this UpsertInstrumentEventRequest.


        :param instrument_event: The instrument_event of this UpsertInstrumentEventRequest.  # noqa: E501
        :type instrument_event: lusid.InstrumentEvent
        """
        if self.local_vars_configuration.client_side_validation and instrument_event is None:  # noqa: E501
            raise ValueError("Invalid value for `instrument_event`, must not be `None`")  # noqa: E501

        self._instrument_event = instrument_event

    @property
    def properties(self):
        """Gets the properties of this UpsertInstrumentEventRequest.  # noqa: E501

        The properties attached to this instrument event.  # noqa: E501

        :return: The properties of this UpsertInstrumentEventRequest.  # noqa: E501
        :rtype: list[lusid.PerpetualProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this UpsertInstrumentEventRequest.

        The properties attached to this instrument event.  # noqa: E501

        :param properties: The properties of this UpsertInstrumentEventRequest.  # noqa: E501
        :type properties: list[lusid.PerpetualProperty]
        """

        self._properties = properties

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
        if not isinstance(other, UpsertInstrumentEventRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpsertInstrumentEventRequest):
            return True

        return self.to_dict() != other.to_dict()
