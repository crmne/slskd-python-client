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

from pydantic import Field, StrictStr, validate_arguments
from typing_extensions import Annotated

from slskd.api_client import ApiClient
from slskd.api_response import ApiResponse
from slskd.exceptions import ApiTypeError, ApiValueError  # noqa: F401


class RelayApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @overload
    async def relay_agent_delete(self, **kwargs) -> None:  # noqa: E501
        ...

    @overload
    def relay_agent_delete(
        self, async_req: Optional[bool] = True, **kwargs
    ) -> None:  # noqa: E501
        ...

    @validate_arguments
    def relay_agent_delete(
        self, async_req: Optional[bool] = None, **kwargs
    ) -> Union[None, Awaitable[None]]:  # noqa: E501
        """Disconnects from the connected controller.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.relay_agent_delete(async_req=True)
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
        :rtype: None
        """
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            raise ValueError(
                "Error! Please call the relay_agent_delete_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            )
        if async_req is not None:
            kwargs["async_req"] = async_req
        return self.relay_agent_delete_with_http_info(**kwargs)  # noqa: E501

    @validate_arguments
    def relay_agent_delete_with_http_info(self, **kwargs) -> ApiResponse:  # noqa: E501
        """Disconnects from the connected controller.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.relay_agent_delete_with_http_info(async_req=True)
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
        :rtype: None
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
                    " to method relay_agent_delete" % _key
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
        # authentication setting
        _auth_settings = ["bearerAuth"]  # noqa: E501

        _response_types_map = {}

        return self.api_client.call_api(
            "/relay/agent",
            "DELETE",
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

    @overload
    async def relay_agent_put(self, **kwargs) -> None:  # noqa: E501
        ...

    @overload
    def relay_agent_put(
        self, async_req: Optional[bool] = True, **kwargs
    ) -> None:  # noqa: E501
        ...

    @validate_arguments
    def relay_agent_put(
        self, async_req: Optional[bool] = None, **kwargs
    ) -> Union[None, Awaitable[None]]:  # noqa: E501
        """Connects to the configured controller.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.relay_agent_put(async_req=True)
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
        :rtype: None
        """
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            raise ValueError(
                "Error! Please call the relay_agent_put_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            )
        if async_req is not None:
            kwargs["async_req"] = async_req
        return self.relay_agent_put_with_http_info(**kwargs)  # noqa: E501

    @validate_arguments
    def relay_agent_put_with_http_info(self, **kwargs) -> ApiResponse:  # noqa: E501
        """Connects to the configured controller.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.relay_agent_put_with_http_info(async_req=True)
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
        :rtype: None
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
                    " to method relay_agent_put" % _key
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
        # authentication setting
        _auth_settings = ["bearerAuth"]  # noqa: E501

        _response_types_map = {}

        return self.api_client.call_api(
            "/relay/agent",
            "PUT",
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

    @overload
    async def relay_controller_downloads_token_get(
        self,
        token: Annotated[
            StrictStr, Field(..., description="The unique identifier for the request.")
        ],
        **kwargs
    ) -> None:  # noqa: E501
        ...

    @overload
    def relay_controller_downloads_token_get(
        self,
        token: Annotated[
            StrictStr, Field(..., description="The unique identifier for the request.")
        ],
        async_req: Optional[bool] = True,
        **kwargs
    ) -> None:  # noqa: E501
        ...

    @validate_arguments
    def relay_controller_downloads_token_get(
        self,
        token: Annotated[
            StrictStr, Field(..., description="The unique identifier for the request.")
        ],
        async_req: Optional[bool] = None,
        **kwargs
    ) -> Union[None, Awaitable[None]]:  # noqa: E501
        """Downloads a file from the connected controller.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.relay_controller_downloads_token_get(token, async_req=True)
        >>> result = thread.get()

        :param token: The unique identifier for the request. (required)
        :type token: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            raise ValueError(
                "Error! Please call the relay_controller_downloads_token_get_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            )
        if async_req is not None:
            kwargs["async_req"] = async_req
        return self.relay_controller_downloads_token_get_with_http_info(
            token, **kwargs
        )  # noqa: E501

    @validate_arguments
    def relay_controller_downloads_token_get_with_http_info(
        self,
        token: Annotated[
            StrictStr, Field(..., description="The unique identifier for the request.")
        ],
        **kwargs
    ) -> ApiResponse:  # noqa: E501
        """Downloads a file from the connected controller.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.relay_controller_downloads_token_get_with_http_info(token, async_req=True)
        >>> result = thread.get()

        :param token: The unique identifier for the request. (required)
        :type token: str
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
        :rtype: None
        """

        _params = locals()

        _all_params = ["token"]
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
                    " to method relay_controller_downloads_token_get" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params["token"]:
            _path_params["token"] = _params["token"]

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get("_headers", {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # authentication setting
        _auth_settings = ["bearerAuth"]  # noqa: E501

        _response_types_map = {}

        return self.api_client.call_api(
            "/relay/controller/downloads/{token}",
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

    @overload
    async def relay_controller_files_token_post(
        self,
        token: Annotated[
            StrictStr, Field(..., description="The unique identifier for the request.")
        ],
        **kwargs
    ) -> None:  # noqa: E501
        ...

    @overload
    def relay_controller_files_token_post(
        self,
        token: Annotated[
            StrictStr, Field(..., description="The unique identifier for the request.")
        ],
        async_req: Optional[bool] = True,
        **kwargs
    ) -> None:  # noqa: E501
        ...

    @validate_arguments
    def relay_controller_files_token_post(
        self,
        token: Annotated[
            StrictStr, Field(..., description="The unique identifier for the request.")
        ],
        async_req: Optional[bool] = None,
        **kwargs
    ) -> Union[None, Awaitable[None]]:  # noqa: E501
        """Uploads a file to the connected controller.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.relay_controller_files_token_post(token, async_req=True)
        >>> result = thread.get()

        :param token: The unique identifier for the request. (required)
        :type token: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            raise ValueError(
                "Error! Please call the relay_controller_files_token_post_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            )
        if async_req is not None:
            kwargs["async_req"] = async_req
        return self.relay_controller_files_token_post_with_http_info(
            token, **kwargs
        )  # noqa: E501

    @validate_arguments
    def relay_controller_files_token_post_with_http_info(
        self,
        token: Annotated[
            StrictStr, Field(..., description="The unique identifier for the request.")
        ],
        **kwargs
    ) -> ApiResponse:  # noqa: E501
        """Uploads a file to the connected controller.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.relay_controller_files_token_post_with_http_info(token, async_req=True)
        >>> result = thread.get()

        :param token: The unique identifier for the request. (required)
        :type token: str
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
        :rtype: None
        """

        _params = locals()

        _all_params = ["token"]
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
                    " to method relay_controller_files_token_post" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params["token"]:
            _path_params["token"] = _params["token"]

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get("_headers", {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # authentication setting
        _auth_settings = ["bearerAuth"]  # noqa: E501

        _response_types_map = {}

        return self.api_client.call_api(
            "/relay/controller/files/{token}",
            "POST",
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

    @overload
    async def relay_controller_shares_token_post(
        self,
        token: Annotated[
            StrictStr, Field(..., description="The unique identifier for the request.")
        ],
        **kwargs
    ) -> None:  # noqa: E501
        ...

    @overload
    def relay_controller_shares_token_post(
        self,
        token: Annotated[
            StrictStr, Field(..., description="The unique identifier for the request.")
        ],
        async_req: Optional[bool] = True,
        **kwargs
    ) -> None:  # noqa: E501
        ...

    @validate_arguments
    def relay_controller_shares_token_post(
        self,
        token: Annotated[
            StrictStr, Field(..., description="The unique identifier for the request.")
        ],
        async_req: Optional[bool] = None,
        **kwargs
    ) -> Union[None, Awaitable[None]]:  # noqa: E501
        """Uploads share information to the connected controller.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.relay_controller_shares_token_post(token, async_req=True)
        >>> result = thread.get()

        :param token: The unique identifier for the request. (required)
        :type token: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            raise ValueError(
                "Error! Please call the relay_controller_shares_token_post_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            )
        if async_req is not None:
            kwargs["async_req"] = async_req
        return self.relay_controller_shares_token_post_with_http_info(
            token, **kwargs
        )  # noqa: E501

    @validate_arguments
    def relay_controller_shares_token_post_with_http_info(
        self,
        token: Annotated[
            StrictStr, Field(..., description="The unique identifier for the request.")
        ],
        **kwargs
    ) -> ApiResponse:  # noqa: E501
        """Uploads share information to the connected controller.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.relay_controller_shares_token_post_with_http_info(token, async_req=True)
        >>> result = thread.get()

        :param token: The unique identifier for the request. (required)
        :type token: str
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
        :rtype: None
        """

        _params = locals()

        _all_params = ["token"]
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
                    " to method relay_controller_shares_token_post" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params["token"]:
            _path_params["token"] = _params["token"]

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get("_headers", {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # authentication setting
        _auth_settings = ["bearerAuth"]  # noqa: E501

        _response_types_map = {}

        return self.api_client.call_api(
            "/relay/controller/shares/{token}",
            "POST",
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
