# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3093
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from lusid.api_client import ApiClient
from lusid.exceptions import (
    ApiTypeError,
    ApiValueError
)


class EntitiesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_portfolio_changes(self, scope, effective_at, **kwargs):  # noqa: E501
        """[EARLY ACCESS] Get the next change to each portfolio in a scope.  # noqa: E501

        Gets the time of the next (earliest effective at) modification (correction and/or amendment) to each portfolio in a scope relative to a point in bitemporal time.  Includes changes from parent portfolios in different scopes.  Excludes changes from subcriptions (e.g corporate actions).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_portfolio_changes(scope, effective_at, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str scope: The scope (required)
        :param str effective_at: The effective date of the origin. (required)
        :param datetime as_at: The as-at date of the origin.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ResourceListOfChange
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_portfolio_changes_with_http_info(scope, effective_at, **kwargs)  # noqa: E501

    def get_portfolio_changes_with_http_info(self, scope, effective_at, **kwargs):  # noqa: E501
        """[EARLY ACCESS] Get the next change to each portfolio in a scope.  # noqa: E501

        Gets the time of the next (earliest effective at) modification (correction and/or amendment) to each portfolio in a scope relative to a point in bitemporal time.  Includes changes from parent portfolios in different scopes.  Excludes changes from subcriptions (e.g corporate actions).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_portfolio_changes_with_http_info(scope, effective_at, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str scope: The scope (required)
        :param str effective_at: The effective date of the origin. (required)
        :param datetime as_at: The as-at date of the origin.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ResourceListOfChange, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['scope', 'effective_at', 'as_at']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_portfolio_changes" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'scope' is set
        if ('scope' not in local_var_params or
                local_var_params['scope'] is None):
            raise ApiValueError("Missing the required parameter `scope` when calling `get_portfolio_changes`")  # noqa: E501
        # verify the required parameter 'effective_at' is set
        if ('effective_at' not in local_var_params or
                local_var_params['effective_at'] is None):
            raise ApiValueError("Missing the required parameter `effective_at` when calling `get_portfolio_changes`")  # noqa: E501

        if ('scope' in local_var_params and
                len(local_var_params['scope']) > 64):
            raise ApiValueError("Invalid value for parameter `scope` when calling `get_portfolio_changes`, length must be less than or equal to `64`")  # noqa: E501
        if ('scope' in local_var_params and
                len(local_var_params['scope']) < 1):
            raise ApiValueError("Invalid value for parameter `scope` when calling `get_portfolio_changes`, length must be greater than or equal to `1`")  # noqa: E501
        if 'scope' in local_var_params and not re.search(r'^[a-zA-Z0-9\-_]+$', local_var_params['scope']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `scope` when calling `get_portfolio_changes`, must conform to the pattern `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501
        if ('effective_at' in local_var_params and
                len(local_var_params['effective_at']) > 256):
            raise ApiValueError("Invalid value for parameter `effective_at` when calling `get_portfolio_changes`, length must be less than or equal to `256`")  # noqa: E501
        if ('effective_at' in local_var_params and
                len(local_var_params['effective_at']) < 0):
            raise ApiValueError("Invalid value for parameter `effective_at` when calling `get_portfolio_changes`, length must be greater than or equal to `0`")  # noqa: E501
        if 'effective_at' in local_var_params and not re.search(r'^[a-zA-Z0-9\-_\+:\.]+$', local_var_params['effective_at']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `effective_at` when calling `get_portfolio_changes`, must conform to the pattern `/^[a-zA-Z0-9\-_\+:\.]+$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'scope' in local_var_params:
            query_params.append(('scope', local_var_params['scope']))  # noqa: E501
        if 'effective_at' in local_var_params:
            query_params.append(('effectiveAt', local_var_params['effective_at']))  # noqa: E501
        if 'as_at' in local_var_params:
            query_params.append(('asAt', local_var_params['as_at']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501


        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        # set the LUSID header
        header_params['X-LUSID-SDK-Language'] = 'Python'
        header_params['X-LUSID-SDK-Version'] = '0.11.3093'

        return self.api_client.call_api(
            '/api/entities/changes/portfolios', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResourceListOfChange',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
