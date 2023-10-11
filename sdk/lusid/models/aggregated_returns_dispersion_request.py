# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.0.599
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


class AggregatedReturnsDispersionRequest(object):
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
        'to_effective_at': 'str',
        'years_count': 'int',
        'return_ids': 'list[ResourceId]',
        'recipe_id': 'ResourceId',
        'composite_method': 'str',
        'alternative_inception_date': 'str'
    }

    attribute_map = {
        'to_effective_at': 'toEffectiveAt',
        'years_count': 'yearsCount',
        'return_ids': 'returnIds',
        'recipe_id': 'recipeId',
        'composite_method': 'compositeMethod',
        'alternative_inception_date': 'alternativeInceptionDate'
    }

    required_map = {
        'to_effective_at': 'optional',
        'years_count': 'optional',
        'return_ids': 'optional',
        'recipe_id': 'optional',
        'composite_method': 'optional',
        'alternative_inception_date': 'optional'
    }

    def __init__(self, to_effective_at=None, years_count=None, return_ids=None, recipe_id=None, composite_method=None, alternative_inception_date=None, local_vars_configuration=None):  # noqa: E501
        """AggregatedReturnsDispersionRequest - a model defined in OpenAPI"
        
        :param to_effective_at:  The end date for when the you want the dispersion to be calculated.
        :type to_effective_at: str
        :param years_count:  For how many years to calculate the dispersion. Default to 10.
        :type years_count: int
        :param return_ids:  The Scope and code of the returns.
        :type return_ids: list[lusid.ResourceId]
        :param recipe_id: 
        :type recipe_id: lusid.ResourceId
        :param composite_method:  The method used to calculate the Portfolio performance: Equal/Asset.
        :type composite_method: str
        :param alternative_inception_date:  Optional - either a date, or the key for a portfolio property containing a date. If provided, the given date will override the inception date for this request.
        :type alternative_inception_date: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._to_effective_at = None
        self._years_count = None
        self._return_ids = None
        self._recipe_id = None
        self._composite_method = None
        self._alternative_inception_date = None
        self.discriminator = None

        self.to_effective_at = to_effective_at
        if years_count is not None:
            self.years_count = years_count
        self.return_ids = return_ids
        if recipe_id is not None:
            self.recipe_id = recipe_id
        self.composite_method = composite_method
        self.alternative_inception_date = alternative_inception_date

    @property
    def to_effective_at(self):
        """Gets the to_effective_at of this AggregatedReturnsDispersionRequest.  # noqa: E501

        The end date for when the you want the dispersion to be calculated.  # noqa: E501

        :return: The to_effective_at of this AggregatedReturnsDispersionRequest.  # noqa: E501
        :rtype: str
        """
        return self._to_effective_at

    @to_effective_at.setter
    def to_effective_at(self, to_effective_at):
        """Sets the to_effective_at of this AggregatedReturnsDispersionRequest.

        The end date for when the you want the dispersion to be calculated.  # noqa: E501

        :param to_effective_at: The to_effective_at of this AggregatedReturnsDispersionRequest.  # noqa: E501
        :type to_effective_at: str
        """
        if (self.local_vars_configuration.client_side_validation and
                to_effective_at is not None and len(to_effective_at) > 256):
            raise ValueError("Invalid value for `to_effective_at`, length must be less than or equal to `256`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                to_effective_at is not None and len(to_effective_at) < 0):
            raise ValueError("Invalid value for `to_effective_at`, length must be greater than or equal to `0`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                to_effective_at is not None and not re.search(r'^[a-zA-Z0-9\-_\+:\.]+$', to_effective_at)):  # noqa: E501
            raise ValueError(r"Invalid value for `to_effective_at`, must be a follow pattern or equal to `/^[a-zA-Z0-9\-_\+:\.]+$/`")  # noqa: E501

        self._to_effective_at = to_effective_at

    @property
    def years_count(self):
        """Gets the years_count of this AggregatedReturnsDispersionRequest.  # noqa: E501

        For how many years to calculate the dispersion. Default to 10.  # noqa: E501

        :return: The years_count of this AggregatedReturnsDispersionRequest.  # noqa: E501
        :rtype: int
        """
        return self._years_count

    @years_count.setter
    def years_count(self, years_count):
        """Sets the years_count of this AggregatedReturnsDispersionRequest.

        For how many years to calculate the dispersion. Default to 10.  # noqa: E501

        :param years_count: The years_count of this AggregatedReturnsDispersionRequest.  # noqa: E501
        :type years_count: int
        """

        self._years_count = years_count

    @property
    def return_ids(self):
        """Gets the return_ids of this AggregatedReturnsDispersionRequest.  # noqa: E501

        The Scope and code of the returns.  # noqa: E501

        :return: The return_ids of this AggregatedReturnsDispersionRequest.  # noqa: E501
        :rtype: list[lusid.ResourceId]
        """
        return self._return_ids

    @return_ids.setter
    def return_ids(self, return_ids):
        """Sets the return_ids of this AggregatedReturnsDispersionRequest.

        The Scope and code of the returns.  # noqa: E501

        :param return_ids: The return_ids of this AggregatedReturnsDispersionRequest.  # noqa: E501
        :type return_ids: list[lusid.ResourceId]
        """

        self._return_ids = return_ids

    @property
    def recipe_id(self):
        """Gets the recipe_id of this AggregatedReturnsDispersionRequest.  # noqa: E501


        :return: The recipe_id of this AggregatedReturnsDispersionRequest.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._recipe_id

    @recipe_id.setter
    def recipe_id(self, recipe_id):
        """Sets the recipe_id of this AggregatedReturnsDispersionRequest.


        :param recipe_id: The recipe_id of this AggregatedReturnsDispersionRequest.  # noqa: E501
        :type recipe_id: lusid.ResourceId
        """

        self._recipe_id = recipe_id

    @property
    def composite_method(self):
        """Gets the composite_method of this AggregatedReturnsDispersionRequest.  # noqa: E501

        The method used to calculate the Portfolio performance: Equal/Asset.  # noqa: E501

        :return: The composite_method of this AggregatedReturnsDispersionRequest.  # noqa: E501
        :rtype: str
        """
        return self._composite_method

    @composite_method.setter
    def composite_method(self, composite_method):
        """Sets the composite_method of this AggregatedReturnsDispersionRequest.

        The method used to calculate the Portfolio performance: Equal/Asset.  # noqa: E501

        :param composite_method: The composite_method of this AggregatedReturnsDispersionRequest.  # noqa: E501
        :type composite_method: str
        """

        self._composite_method = composite_method

    @property
    def alternative_inception_date(self):
        """Gets the alternative_inception_date of this AggregatedReturnsDispersionRequest.  # noqa: E501

        Optional - either a date, or the key for a portfolio property containing a date. If provided, the given date will override the inception date for this request.  # noqa: E501

        :return: The alternative_inception_date of this AggregatedReturnsDispersionRequest.  # noqa: E501
        :rtype: str
        """
        return self._alternative_inception_date

    @alternative_inception_date.setter
    def alternative_inception_date(self, alternative_inception_date):
        """Sets the alternative_inception_date of this AggregatedReturnsDispersionRequest.

        Optional - either a date, or the key for a portfolio property containing a date. If provided, the given date will override the inception date for this request.  # noqa: E501

        :param alternative_inception_date: The alternative_inception_date of this AggregatedReturnsDispersionRequest.  # noqa: E501
        :type alternative_inception_date: str
        """
        if (self.local_vars_configuration.client_side_validation and
                alternative_inception_date is not None and len(alternative_inception_date) > 1024):
            raise ValueError("Invalid value for `alternative_inception_date`, length must be less than or equal to `1024`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                alternative_inception_date is not None and len(alternative_inception_date) < 0):
            raise ValueError("Invalid value for `alternative_inception_date`, length must be greater than or equal to `0`")  # noqa: E501

        self._alternative_inception_date = alternative_inception_date

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
        if not isinstance(other, AggregatedReturnsDispersionRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AggregatedReturnsDispersionRequest):
            return True

        return self.to_dict() != other.to_dict()
