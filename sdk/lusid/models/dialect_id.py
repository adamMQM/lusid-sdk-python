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


class DialectId(object):
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
        'scope': 'str',
        'vendor': 'str',
        'source_system': 'str',
        'version': 'str',
        'serialisation_format': 'str',
        'entity_type': 'str'
    }

    attribute_map = {
        'scope': 'scope',
        'vendor': 'vendor',
        'source_system': 'sourceSystem',
        'version': 'version',
        'serialisation_format': 'serialisationFormat',
        'entity_type': 'entityType'
    }

    required_map = {
        'scope': 'required',
        'vendor': 'required',
        'source_system': 'required',
        'version': 'required',
        'serialisation_format': 'required',
        'entity_type': 'required'
    }

    def __init__(self, scope=None, vendor=None, source_system=None, version=None, serialisation_format=None, entity_type=None, local_vars_configuration=None):  # noqa: E501
        """DialectId - a model defined in OpenAPI"
        
        :param scope:  The Scope of the dialect. (required)
        :type scope: str
        :param vendor:  The vendor of the dialect, the entity that created it. e.g. ISDA, FINBOURNE. (required)
        :type vendor: str
        :param source_system:  The source system of the dialect, the system that understands it. e.g. LUSID, QuantLib. (required)
        :type source_system: str
        :param version:  The semantic version of the dialect: MAJOR.MINOR.PATCH. (required)
        :type version: str
        :param serialisation_format:  The serialisation format of a document in this dialect. e.g. JSON, XML. (required)
        :type serialisation_format: str
        :param entity_type:  The type of entity this dialect describes e.g. Instrument. (required)
        :type entity_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._scope = None
        self._vendor = None
        self._source_system = None
        self._version = None
        self._serialisation_format = None
        self._entity_type = None
        self.discriminator = None

        self.scope = scope
        self.vendor = vendor
        self.source_system = source_system
        self.version = version
        self.serialisation_format = serialisation_format
        self.entity_type = entity_type

    @property
    def scope(self):
        """Gets the scope of this DialectId.  # noqa: E501

        The Scope of the dialect.  # noqa: E501

        :return: The scope of this DialectId.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this DialectId.

        The Scope of the dialect.  # noqa: E501

        :param scope: The scope of this DialectId.  # noqa: E501
        :type scope: str
        """
        if self.local_vars_configuration.client_side_validation and scope is None:  # noqa: E501
            raise ValueError("Invalid value for `scope`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                scope is not None and len(scope) > 64):
            raise ValueError("Invalid value for `scope`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                scope is not None and len(scope) < 1):
            raise ValueError("Invalid value for `scope`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                scope is not None and not re.search(r'^[a-zA-Z0-9\-_]+$', scope)):  # noqa: E501
            raise ValueError(r"Invalid value for `scope`, must be a follow pattern or equal to `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501

        self._scope = scope

    @property
    def vendor(self):
        """Gets the vendor of this DialectId.  # noqa: E501

        The vendor of the dialect, the entity that created it. e.g. ISDA, FINBOURNE.  # noqa: E501

        :return: The vendor of this DialectId.  # noqa: E501
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """Sets the vendor of this DialectId.

        The vendor of the dialect, the entity that created it. e.g. ISDA, FINBOURNE.  # noqa: E501

        :param vendor: The vendor of this DialectId.  # noqa: E501
        :type vendor: str
        """
        if self.local_vars_configuration.client_side_validation and vendor is None:  # noqa: E501
            raise ValueError("Invalid value for `vendor`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                vendor is not None and len(vendor) > 64):
            raise ValueError("Invalid value for `vendor`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                vendor is not None and len(vendor) < 1):
            raise ValueError("Invalid value for `vendor`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                vendor is not None and not re.search(r'^[a-zA-Z0-9\-_]+$', vendor)):  # noqa: E501
            raise ValueError(r"Invalid value for `vendor`, must be a follow pattern or equal to `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501

        self._vendor = vendor

    @property
    def source_system(self):
        """Gets the source_system of this DialectId.  # noqa: E501

        The source system of the dialect, the system that understands it. e.g. LUSID, QuantLib.  # noqa: E501

        :return: The source_system of this DialectId.  # noqa: E501
        :rtype: str
        """
        return self._source_system

    @source_system.setter
    def source_system(self, source_system):
        """Sets the source_system of this DialectId.

        The source system of the dialect, the system that understands it. e.g. LUSID, QuantLib.  # noqa: E501

        :param source_system: The source_system of this DialectId.  # noqa: E501
        :type source_system: str
        """
        if self.local_vars_configuration.client_side_validation and source_system is None:  # noqa: E501
            raise ValueError("Invalid value for `source_system`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                source_system is not None and len(source_system) > 64):
            raise ValueError("Invalid value for `source_system`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                source_system is not None and len(source_system) < 1):
            raise ValueError("Invalid value for `source_system`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                source_system is not None and not re.search(r'^[a-zA-Z0-9\-_]+$', source_system)):  # noqa: E501
            raise ValueError(r"Invalid value for `source_system`, must be a follow pattern or equal to `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501

        self._source_system = source_system

    @property
    def version(self):
        """Gets the version of this DialectId.  # noqa: E501

        The semantic version of the dialect: MAJOR.MINOR.PATCH.  # noqa: E501

        :return: The version of this DialectId.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this DialectId.

        The semantic version of the dialect: MAJOR.MINOR.PATCH.  # noqa: E501

        :param version: The version of this DialectId.  # noqa: E501
        :type version: str
        """
        if self.local_vars_configuration.client_side_validation and version is None:  # noqa: E501
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                version is not None and len(version) > 30):
            raise ValueError("Invalid value for `version`, length must be less than or equal to `30`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                version is not None and len(version) < 1):
            raise ValueError("Invalid value for `version`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                version is not None and not re.search(r'^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$', version)):  # noqa: E501
            raise ValueError(r"Invalid value for `version`, must be a follow pattern or equal to `/^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$/`")  # noqa: E501

        self._version = version

    @property
    def serialisation_format(self):
        """Gets the serialisation_format of this DialectId.  # noqa: E501

        The serialisation format of a document in this dialect. e.g. JSON, XML.  # noqa: E501

        :return: The serialisation_format of this DialectId.  # noqa: E501
        :rtype: str
        """
        return self._serialisation_format

    @serialisation_format.setter
    def serialisation_format(self, serialisation_format):
        """Sets the serialisation_format of this DialectId.

        The serialisation format of a document in this dialect. e.g. JSON, XML.  # noqa: E501

        :param serialisation_format: The serialisation_format of this DialectId.  # noqa: E501
        :type serialisation_format: str
        """
        if self.local_vars_configuration.client_side_validation and serialisation_format is None:  # noqa: E501
            raise ValueError("Invalid value for `serialisation_format`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                serialisation_format is not None and len(serialisation_format) < 1):
            raise ValueError("Invalid value for `serialisation_format`, length must be greater than or equal to `1`")  # noqa: E501

        self._serialisation_format = serialisation_format

    @property
    def entity_type(self):
        """Gets the entity_type of this DialectId.  # noqa: E501

        The type of entity this dialect describes e.g. Instrument.  # noqa: E501

        :return: The entity_type of this DialectId.  # noqa: E501
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this DialectId.

        The type of entity this dialect describes e.g. Instrument.  # noqa: E501

        :param entity_type: The entity_type of this DialectId.  # noqa: E501
        :type entity_type: str
        """
        if self.local_vars_configuration.client_side_validation and entity_type is None:  # noqa: E501
            raise ValueError("Invalid value for `entity_type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                entity_type is not None and len(entity_type) < 1):
            raise ValueError("Invalid value for `entity_type`, length must be greater than or equal to `1`")  # noqa: E501

        self._entity_type = entity_type

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
        if not isinstance(other, DialectId):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DialectId):
            return True

        return self.to_dict() != other.to_dict()
