# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.0.599
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
from lusid.models.je_lines_query_parameters import JELinesQueryParameters
from lusid.models.lusid_problem_details import LusidProblemDetails
from lusid.models.lusid_validation_problem_details import LusidValidationProblemDetails
from lusid.models.versioned_resource_list_of_journal_entry_line import VersionedResourceListOfJournalEntryLine


class AborApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_je_lines(self, scope, code, je_lines_query_parameters, **kwargs):  # noqa: E501
        """[DEPRECATED] GetJELines: DEPRECATED: please use GetJournalEntryLines instead. Get the JELines for the given Abor.  # noqa: E501

        DEPRECATED: please use GetJournalEntryLines instead. Gets the JELines for the given Abor                The JE Lines have been generated from transactions and translated via posting rules  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_je_lines(scope, code, je_lines_query_parameters, async_req=True)
        >>> result = thread.get()

        :param scope: The scope of the Abor. (required)
        :type scope: str
        :param code: The code of the Abor. Together with the scope is creating the unique identifier for the given Abor. (required)
        :type code: str
        :param je_lines_query_parameters: The query parameters used in running the generation of the JELines. (required)
        :type je_lines_query_parameters: JELinesQueryParameters
        :param as_at: The asAt datetime at which to retrieve JELines. Defaults to returning the latest version               of each transaction if not specified.
        :type as_at: datetime
        :param limit: When paginating, limit the number of returned results to this many. Defaults to 100 if not specified.
        :type limit: int
        :param page: The pagination token to use to continue listing JELines from a previous call to GetJELines.
        :type page: str
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
        :rtype: VersionedResourceListOfJournalEntryLine
        """
        kwargs['_return_http_data_only'] = True
        return self.get_je_lines_with_http_info(scope, code, je_lines_query_parameters, **kwargs)  # noqa: E501

    def get_je_lines_with_http_info(self, scope, code, je_lines_query_parameters, **kwargs):  # noqa: E501
        """[DEPRECATED] GetJELines: DEPRECATED: please use GetJournalEntryLines instead. Get the JELines for the given Abor.  # noqa: E501

        DEPRECATED: please use GetJournalEntryLines instead. Gets the JELines for the given Abor                The JE Lines have been generated from transactions and translated via posting rules  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_je_lines_with_http_info(scope, code, je_lines_query_parameters, async_req=True)
        >>> result = thread.get()

        :param scope: The scope of the Abor. (required)
        :type scope: str
        :param code: The code of the Abor. Together with the scope is creating the unique identifier for the given Abor. (required)
        :type code: str
        :param je_lines_query_parameters: The query parameters used in running the generation of the JELines. (required)
        :type je_lines_query_parameters: JELinesQueryParameters
        :param as_at: The asAt datetime at which to retrieve JELines. Defaults to returning the latest version               of each transaction if not specified.
        :type as_at: datetime
        :param limit: When paginating, limit the number of returned results to this many. Defaults to 100 if not specified.
        :type limit: int
        :param page: The pagination token to use to continue listing JELines from a previous call to GetJELines.
        :type page: str
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
        :rtype: (VersionedResourceListOfJournalEntryLine, int, HTTPHeaderDict)
        """

        local_var_params = locals()

        all_params = [
            'scope',
            'code',
            'je_lines_query_parameters',
            'as_at',
            'limit',
            'page'
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
                    " to method get_je_lines" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'scope' is set
        if self.api_client.client_side_validation and ('scope' not in local_var_params or  # noqa: E501
                                                        local_var_params['scope'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `scope` when calling `get_je_lines`")  # noqa: E501
        # verify the required parameter 'code' is set
        if self.api_client.client_side_validation and ('code' not in local_var_params or  # noqa: E501
                                                        local_var_params['code'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `code` when calling `get_je_lines`")  # noqa: E501
        # verify the required parameter 'je_lines_query_parameters' is set
        if self.api_client.client_side_validation and ('je_lines_query_parameters' not in local_var_params or  # noqa: E501
                                                        local_var_params['je_lines_query_parameters'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `je_lines_query_parameters` when calling `get_je_lines`")  # noqa: E501

        if self.api_client.client_side_validation and ('scope' in local_var_params and  # noqa: E501
                                                        len(local_var_params['scope']) > 64):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `scope` when calling `get_je_lines`, length must be less than or equal to `64`")  # noqa: E501
        if self.api_client.client_side_validation and ('scope' in local_var_params and  # noqa: E501
                                                        len(local_var_params['scope']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `scope` when calling `get_je_lines`, length must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'scope' in local_var_params and not re.search(r'^[a-zA-Z0-9\-_]+$', local_var_params['scope']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `scope` when calling `get_je_lines`, must conform to the pattern `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501
        if self.api_client.client_side_validation and ('code' in local_var_params and  # noqa: E501
                                                        len(local_var_params['code']) > 64):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `code` when calling `get_je_lines`, length must be less than or equal to `64`")  # noqa: E501
        if self.api_client.client_side_validation and ('code' in local_var_params and  # noqa: E501
                                                        len(local_var_params['code']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `code` when calling `get_je_lines`, length must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'code' in local_var_params and not re.search(r'^[a-zA-Z0-9\-_]+$', local_var_params['code']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `code` when calling `get_je_lines`, must conform to the pattern `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501
        if self.api_client.client_side_validation and ('page' in local_var_params and  # noqa: E501
                                                        len(local_var_params['page']) > 500):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `page` when calling `get_je_lines`, length must be less than or equal to `500`")  # noqa: E501
        if self.api_client.client_side_validation and ('page' in local_var_params and  # noqa: E501
                                                        len(local_var_params['page']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `page` when calling `get_je_lines`, length must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'page' in local_var_params and not re.search(r'^[a-zA-Z0-9\+\/]*={0,3}$', local_var_params['page']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `page` when calling `get_je_lines`, must conform to the pattern `/^[a-zA-Z0-9\+\/]*={0,3}$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'scope' in local_var_params:
            path_params['scope'] = local_var_params['scope']  # noqa: E501
        if 'code' in local_var_params:
            path_params['code'] = local_var_params['code']  # noqa: E501

        query_params = []
        if 'as_at' in local_var_params and local_var_params['as_at'] is not None:  # noqa: E501
            query_params.append(('asAt', local_var_params['as_at']))  # noqa: E501
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'page' in local_var_params and local_var_params['page'] is not None:  # noqa: E501
            query_params.append(('page', local_var_params['page']))  # noqa: E501

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        if 'je_lines_query_parameters' in local_var_params:
            body_params = local_var_params['je_lines_query_parameters']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        header_params['Accept-Encoding'] = "gzip, deflate, br"

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # set the LUSID header
        header_params['X-LUSID-SDK-Language'] = 'Python'
        header_params['X-LUSID-SDK-Version'] = '1.0.599'

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        response_types_map = {
            200: "VersionedResourceListOfJournalEntryLine",
            400: "LusidValidationProblemDetails",
        }

        return self.api_client.call_api(
            '/api/abor/{scope}/{code}/JELines/$query/$deprecated', 'POST',
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
