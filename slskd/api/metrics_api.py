# coding: utf-8

"""
    slskd

    A python client for slskd  # noqa: E501

    The version of the OpenAPI document: 0.17.8.0
    Contact: carmine@paolino.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import re  # noqa: F401
from typing import Awaitable, Optional, Union, overload

from pydantic import validate_arguments

from slskd.api_client import ApiClient
from slskd.api_response import ApiResponse
from slskd.exceptions import ApiTypeError, ApiValueError  # noqa: F401


class MetricsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @overload
    async def metrics_get(self, **kwargs) -> object:  # noqa: E501
        ...

    @overload
    def metrics_get(
        self, async_req: Optional[bool] = True, **kwargs
    ) -> object:  # noqa: E501
        ...

    @validate_arguments
    def metrics_get(
        self, async_req: Optional[bool] = None, **kwargs
    ) -> Union[object, Awaitable[object]]:  # noqa: E501
        """Gets application metrics.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.metrics_get(async_req=True)
        >>> result = thread.get()

        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: object
        """
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            raise ValueError(
                "Error! Please call the metrics_get_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            )
        if async_req is not None:
            kwargs["async_req"] = async_req
        return self.metrics_get_with_http_info(**kwargs)  # noqa: E501

    @validate_arguments
    def metrics_get_with_http_info(self, **kwargs) -> ApiResponse:  # noqa: E501
        """Gets application metrics.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.metrics_get_with_http_info(async_req=True)
        >>> result = thread.get()

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
        :rtype: tuple(object, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = []
        _all_params.extend(
            [
                "async_req",
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
                "_request_auth",
                "_content_type",
                "_headers",
            ]
        )

        # validate the arguments
        for _key, _val in _params["kwargs"].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method metrics_get" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get("_headers", {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # authentication setting
        _auth_settings = ["ApiKeyAuth"]  # noqa: E501

        _response_types_map = {
            "200": "object",
        }

        return self.api_client.call_api(
            "/metrics",
            "GET",
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get("async_req"),
            _return_http_data_only=_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=_params.get("_preload_content", True),
            _request_timeout=_params.get("_request_timeout"),
            collection_formats=_collection_formats,
            _request_auth=_params.get("_request_auth"),
        )
