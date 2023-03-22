# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.0.18
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


class ListAggregationReconciliation(object):
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
        'left': 'ListAggregationResponse',
        'right': 'ListAggregationResponse',
        'diff': 'list[dict(str, object)]',
        'data_schema': 'ResultDataSchema'
    }

    attribute_map = {
        'left': 'left',
        'right': 'right',
        'diff': 'diff',
        'data_schema': 'dataSchema'
    }

    required_map = {
        'left': 'optional',
        'right': 'optional',
        'diff': 'optional',
        'data_schema': 'optional'
    }

    def __init__(self, left=None, right=None, diff=None, data_schema=None, local_vars_configuration=None):  # noqa: E501
        """ListAggregationReconciliation - a model defined in OpenAPI"
        
        :param left: 
        :type left: lusid.ListAggregationResponse
        :param right: 
        :type right: lusid.ListAggregationResponse
        :param diff: 
        :type diff: list[dict(str, object)]
        :param data_schema: 
        :type data_schema: lusid.ResultDataSchema

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._left = None
        self._right = None
        self._diff = None
        self._data_schema = None
        self.discriminator = None

        if left is not None:
            self.left = left
        if right is not None:
            self.right = right
        self.diff = diff
        if data_schema is not None:
            self.data_schema = data_schema

    @property
    def left(self):
        """Gets the left of this ListAggregationReconciliation.  # noqa: E501


        :return: The left of this ListAggregationReconciliation.  # noqa: E501
        :rtype: lusid.ListAggregationResponse
        """
        return self._left

    @left.setter
    def left(self, left):
        """Sets the left of this ListAggregationReconciliation.


        :param left: The left of this ListAggregationReconciliation.  # noqa: E501
        :type left: lusid.ListAggregationResponse
        """

        self._left = left

    @property
    def right(self):
        """Gets the right of this ListAggregationReconciliation.  # noqa: E501


        :return: The right of this ListAggregationReconciliation.  # noqa: E501
        :rtype: lusid.ListAggregationResponse
        """
        return self._right

    @right.setter
    def right(self, right):
        """Sets the right of this ListAggregationReconciliation.


        :param right: The right of this ListAggregationReconciliation.  # noqa: E501
        :type right: lusid.ListAggregationResponse
        """

        self._right = right

    @property
    def diff(self):
        """Gets the diff of this ListAggregationReconciliation.  # noqa: E501


        :return: The diff of this ListAggregationReconciliation.  # noqa: E501
        :rtype: list[dict(str, object)]
        """
        return self._diff

    @diff.setter
    def diff(self, diff):
        """Sets the diff of this ListAggregationReconciliation.


        :param diff: The diff of this ListAggregationReconciliation.  # noqa: E501
        :type diff: list[dict(str, object)]
        """

        self._diff = diff

    @property
    def data_schema(self):
        """Gets the data_schema of this ListAggregationReconciliation.  # noqa: E501


        :return: The data_schema of this ListAggregationReconciliation.  # noqa: E501
        :rtype: lusid.ResultDataSchema
        """
        return self._data_schema

    @data_schema.setter
    def data_schema(self, data_schema):
        """Sets the data_schema of this ListAggregationReconciliation.


        :param data_schema: The data_schema of this ListAggregationReconciliation.  # noqa: E501
        :type data_schema: lusid.ResultDataSchema
        """

        self._data_schema = data_schema

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
        if not isinstance(other, ListAggregationReconciliation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListAggregationReconciliation):
            return True

        return self.to_dict() != other.to_dict()
