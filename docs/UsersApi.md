# slskd.UsersApi

All URIs are relative to *http://localhost:5030/api/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_username_browse_get**](UsersApi.md#users_username_browse_get) | **GET** /users/{username}/browse | Retrieves the files shared by the specified username.
[**users_username_browse_status_get**](UsersApi.md#users_username_browse_status_get) | **GET** /users/{username}/browse/status | Retrieves the status of the current browse operation for the specified username, if any.
[**users_username_directory_post**](UsersApi.md#users_username_directory_post) | **POST** /users/{username}/directory | Retrieves the files from the specified directory from the specified username.
[**users_username_endpoint_get**](UsersApi.md#users_username_endpoint_get) | **GET** /users/{username}/endpoint | Retrieves the address of the specified username.
[**users_username_info_get**](UsersApi.md#users_username_info_get) | **GET** /users/{username}/info | Retrieves information about the specified username.
[**users_username_status_get**](UsersApi.md#users_username_status_get) | **GET** /users/{username}/status | Retrieves status for the specified username.


# **users_username_browse_get**
> List[Directory] users_username_browse_get(username)

Retrieves the files shared by the specified username.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import slskd
from slskd.models.directory import Directory
from slskd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5030/api/v0
# See configuration.py for a list of all supported configuration parameters.
configuration = slskd.Configuration(
    host = "http://localhost:5030/api/v0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
async with slskd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slskd.UsersApi(api_client)
    username = 'username_example' # str | The username of the user.

    try:
        # Retrieves the files shared by the specified username.
        api_response = await api_instance.users_username_browse_get(username)
        print("The response of UsersApi->users_username_browse_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_username_browse_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username of the user. |

### Return type

[**List[Directory]**](Directory.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_username_browse_status_get**
> float users_username_browse_status_get(username)

Retrieves the status of the current browse operation for the specified username, if any.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import slskd
from slskd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5030/api/v0
# See configuration.py for a list of all supported configuration parameters.
configuration = slskd.Configuration(
    host = "http://localhost:5030/api/v0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
async with slskd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slskd.UsersApi(api_client)
    username = 'username_example' # str | The username of the user.

    try:
        # Retrieves the status of the current browse operation for the specified username, if any.
        api_response = await api_instance.users_username_browse_status_get(username)
        print("The response of UsersApi->users_username_browse_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_username_browse_status_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username of the user. |

### Return type

**float**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_username_directory_post**
> Directory users_username_directory_post(username, directory_contents_request)

Retrieves the files from the specified directory from the specified username.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import slskd
from slskd.models.directory import Directory
from slskd.models.directory_contents_request import DirectoryContentsRequest
from slskd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5030/api/v0
# See configuration.py for a list of all supported configuration parameters.
configuration = slskd.Configuration(
    host = "http://localhost:5030/api/v0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
async with slskd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slskd.UsersApi(api_client)
    username = 'username_example' # str | The username of the user.
    directory_contents_request = slskd.DirectoryContentsRequest() # DirectoryContentsRequest | The directory contents request.

    try:
        # Retrieves the files from the specified directory from the specified username.
        api_response = await api_instance.users_username_directory_post(username, directory_contents_request)
        print("The response of UsersApi->users_username_directory_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_username_directory_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username of the user. |
 **directory_contents_request** | [**DirectoryContentsRequest**](DirectoryContentsRequest.md)| The directory contents request. |

### Return type

[**Directory**](Directory.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_username_endpoint_get**
> IPEndPoint users_username_endpoint_get(username)

Retrieves the address of the specified username.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import slskd
from slskd.models.ip_end_point import IPEndPoint
from slskd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5030/api/v0
# See configuration.py for a list of all supported configuration parameters.
configuration = slskd.Configuration(
    host = "http://localhost:5030/api/v0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
async with slskd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slskd.UsersApi(api_client)
    username = 'username_example' # str | The username of the user.

    try:
        # Retrieves the address of the specified username.
        api_response = await api_instance.users_username_endpoint_get(username)
        print("The response of UsersApi->users_username_endpoint_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_username_endpoint_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username of the user. |

### Return type

[**IPEndPoint**](IPEndPoint.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request completed successfully. |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_username_info_get**
> Info users_username_info_get(username)

Retrieves information about the specified username.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import slskd
from slskd.models.info import Info
from slskd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5030/api/v0
# See configuration.py for a list of all supported configuration parameters.
configuration = slskd.Configuration(
    host = "http://localhost:5030/api/v0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
async with slskd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slskd.UsersApi(api_client)
    username = 'username_example' # str | The username of the user.

    try:
        # Retrieves information about the specified username.
        api_response = await api_instance.users_username_info_get(username)
        print("The response of UsersApi->users_username_info_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_username_info_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username of the user. |

### Return type

[**Info**](Info.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_username_status_get**
> Status users_username_status_get(username)

Retrieves status for the specified username.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import slskd
from slskd.models.status import Status
from slskd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5030/api/v0
# See configuration.py for a list of all supported configuration parameters.
configuration = slskd.Configuration(
    host = "http://localhost:5030/api/v0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
async with slskd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slskd.UsersApi(api_client)
    username = 'username_example' # str | The username of the user.

    try:
        # Retrieves status for the specified username.
        api_response = await api_instance.users_username_status_get(username)
        print("The response of UsersApi->users_username_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_username_status_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username of the user. |

### Return type

[**Status**](Status.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
