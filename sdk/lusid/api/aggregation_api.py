# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.4657
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from lusid.api_client import ApiClient
from lusid.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)
from lusid.models.inline_valuation_request import InlineValuationRequest
from lusid.models.list_aggregation_response import ListAggregationResponse
from lusid.models.lusid_problem_details import LusidProblemDetails
from lusid.models.lusid_validation_problem_details import LusidValidationProblemDetails
from lusid.models.valuation_request import ValuationRequest


class AggregationApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_valuation(self, **kwargs):  # noqa: E501
        """GetValuation: Perform valuation for a list of portfolios and/or portfolio groups  # noqa: E501

        Perform valuation on specified list of portfolio and/or portfolio groups for a set of dates.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_valuation(async_req=True)
        >>> result = thread.get()

        :param valuation_request: The request specifying the set of portfolios and dates on which to calculate a set of valuation metrics
        :type valuation_request: ValuationRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ListAggregationResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.get_valuation_with_http_info(**kwargs)  # noqa: E501

    def get_valuation_with_http_info(self, **kwargs):  # noqa: E501
        """GetValuation: Perform valuation for a list of portfolios and/or portfolio groups  # noqa: E501

        Perform valuation on specified list of portfolio and/or portfolio groups for a set of dates.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_valuation_with_http_info(async_req=True)
        >>> result = thread.get()

        :param valuation_request: The request specifying the set of portfolios and dates on which to calculate a set of valuation metrics
        :type valuation_request: ValuationRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object, the HTTP status code, and the headers.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: (ListAggregationResponse, int, HTTPHeaderDict)
        """

        local_var_params = locals()

        all_params = [
            'valuation_request'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_valuation" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        if 'valuation_request' in local_var_params:
            body_params = local_var_params['valuation_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        header_params['Accept-Encoding'] = "gzip, deflate, br"

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # set the LUSID header
        header_params['X-LUSID-SDK-Language'] = 'Python'
        header_params['X-LUSID-SDK-Version'] = '0.11.4657'

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        response_types_map = {
            200: "ListAggregationResponse",
            400: "LusidValidationProblemDetails",
        }

        return self.api_client.call_api(
            '/api/aggregation/$valuation', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def get_valuation_of_weighted_instruments(self, **kwargs):  # noqa: E501
        """GetValuationOfWeightedInstruments: Perform valuation for an inlined portfolio  # noqa: E501

        Perform valuation on the portfolio that is defined by the weighted set of instruments passed to the request.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_valuation_of_weighted_instruments(async_req=True)
        >>> result = thread.get()

        :param inline_valuation_request: The request specifying the set of portfolios and dates on which to calculate a set of valuation metrics
        :type inline_valuation_request: InlineValuationRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ListAggregationResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.get_valuation_of_weighted_instruments_with_http_info(**kwargs)  # noqa: E501

    def get_valuation_of_weighted_instruments_with_http_info(self, **kwargs):  # noqa: E501
        """GetValuationOfWeightedInstruments: Perform valuation for an inlined portfolio  # noqa: E501

        Perform valuation on the portfolio that is defined by the weighted set of instruments passed to the request.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_valuation_of_weighted_instruments_with_http_info(async_req=True)
        >>> result = thread.get()

        :param inline_valuation_request: The request specifying the set of portfolios and dates on which to calculate a set of valuation metrics
        :type inline_valuation_request: InlineValuationRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object, the HTTP status code, and the headers.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: (ListAggregationResponse, int, HTTPHeaderDict)
        """

        local_var_params = locals()

        all_params = [
            'inline_valuation_request'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_valuation_of_weighted_instruments" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        if 'inline_valuation_request' in local_var_params:
            body_params = local_var_params['inline_valuation_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        header_params['Accept-Encoding'] = "gzip, deflate, br"

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # set the LUSID header
        header_params['X-LUSID-SDK-Language'] = 'Python'
        header_params['X-LUSID-SDK-Version'] = '0.11.4657'

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        response_types_map = {
            200: "ListAggregationResponse",
            400: "LusidValidationProblemDetails",
        }

        return self.api_client.call_api(
            '/api/aggregation/$valuationinlined', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))
