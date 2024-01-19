# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    Contact: info@finbourne.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError
from typing import overload, Optional, Union, Awaitable

from typing_extensions import Annotated
from pydantic import Field

from lusid.models.get_recipe_response import GetRecipeResponse
from lusid.models.upsert_recipe_composer_request import UpsertRecipeComposerRequest

from lusid.api_client import ApiClient
from lusid.api_response import ApiResponse
from lusid.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class RecipeComposerApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @overload
    async def get_recipe_composer_resolved_inline(self, upsert_recipe_composer_request : Annotated[UpsertRecipeComposerRequest, Field(..., description="Recipe composer used to resolve into the Configuration Recipe.")], **kwargs) -> GetRecipeResponse:  # noqa: E501
        ...

    @overload
    def get_recipe_composer_resolved_inline(self, upsert_recipe_composer_request : Annotated[UpsertRecipeComposerRequest, Field(..., description="Recipe composer used to resolve into the Configuration Recipe.")], async_req: Optional[bool]=True, **kwargs) -> GetRecipeResponse:  # noqa: E501
        ...

    @validate_arguments
    def get_recipe_composer_resolved_inline(self, upsert_recipe_composer_request : Annotated[UpsertRecipeComposerRequest, Field(..., description="Recipe composer used to resolve into the Configuration Recipe.")], async_req: Optional[bool]=None, **kwargs) -> Union[GetRecipeResponse, Awaitable[GetRecipeResponse]]:  # noqa: E501
        """[EXPERIMENTAL] GetRecipeComposerResolvedInline: Given a Recipe Composer, this endpoint shows what configuration recipe it would resolve to, able to access the already upserted configuration recipes as well as plain inline string inputs.  # noqa: E501

        Resolves an inline recipe composer into a ConfigurationRecipe.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_recipe_composer_resolved_inline(upsert_recipe_composer_request, async_req=True)
        >>> result = thread.get()

        :param upsert_recipe_composer_request: Recipe composer used to resolve into the Configuration Recipe. (required)
        :type upsert_recipe_composer_request: UpsertRecipeComposerRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GetRecipeResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_recipe_composer_resolved_inline_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        if async_req is not None:
            kwargs['async_req'] = async_req
        return self.get_recipe_composer_resolved_inline_with_http_info(upsert_recipe_composer_request, **kwargs)  # noqa: E501

    @validate_arguments
    def get_recipe_composer_resolved_inline_with_http_info(self, upsert_recipe_composer_request : Annotated[UpsertRecipeComposerRequest, Field(..., description="Recipe composer used to resolve into the Configuration Recipe.")], **kwargs) -> ApiResponse:  # noqa: E501
        """[EXPERIMENTAL] GetRecipeComposerResolvedInline: Given a Recipe Composer, this endpoint shows what configuration recipe it would resolve to, able to access the already upserted configuration recipes as well as plain inline string inputs.  # noqa: E501

        Resolves an inline recipe composer into a ConfigurationRecipe.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_recipe_composer_resolved_inline_with_http_info(upsert_recipe_composer_request, async_req=True)
        >>> result = thread.get()

        :param upsert_recipe_composer_request: Recipe composer used to resolve into the Configuration Recipe. (required)
        :type upsert_recipe_composer_request: UpsertRecipeComposerRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(GetRecipeResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'upsert_recipe_composer_request'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_recipe_composer_resolved_inline" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['upsert_recipe_composer_request'] is not None:
            _body_params = _params['upsert_recipe_composer_request']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['oauth2']  # noqa: E501

        _response_types_map = {
            '200': "GetRecipeResponse",
            '400': "LusidValidationProblemDetails",
        }

        return self.api_client.call_api(
            '/api/recipecomposers/inline', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))