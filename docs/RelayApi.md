# slskd.RelayApi

All URIs are relative to *http://localhost:5030/api/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**relay_agent_delete**](RelayApi.md#relay_agent_delete) | **DELETE** /relay/agent | Disconnects from the connected controller.
[**relay_agent_put**](RelayApi.md#relay_agent_put) | **PUT** /relay/agent | Connects to the configured controller.
[**relay_controller_downloads_token_get**](RelayApi.md#relay_controller_downloads_token_get) | **GET** /relay/controller/downloads/{token} | Downloads a file from the connected controller.
[**relay_controller_files_token_post**](RelayApi.md#relay_controller_files_token_post) | **POST** /relay/controller/files/{token} | Uploads a file to the connected controller.
[**relay_controller_shares_token_post**](RelayApi.md#relay_controller_shares_token_post) | **POST** /relay/controller/shares/{token} | Uploads share information to the connected controller.


# **relay_agent_delete**
> object relay_agent_delete()

Disconnects from the connected controller.

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
    api_instance = slskd.RelayApi(api_client)

    try:
        # Disconnects from the connected controller.
        api_response = await api_instance.relay_agent_delete()
        print("The response of RelayApi->relay_agent_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RelayApi->relay_agent_delete: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **relay_agent_put**
> object relay_agent_put()

Connects to the configured controller.

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
    api_instance = slskd.RelayApi(api_client)

    try:
        # Connects to the configured controller.
        api_response = await api_instance.relay_agent_put()
        print("The response of RelayApi->relay_agent_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RelayApi->relay_agent_put: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **relay_controller_downloads_token_get**
> object relay_controller_downloads_token_get(token)

Downloads a file from the connected controller.

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
    api_instance = slskd.RelayApi(api_client)
    token = 'token_example' # str | The unique identifier for the request.

    try:
        # Downloads a file from the connected controller.
        api_response = await api_instance.relay_controller_downloads_token_get(token)
        print("The response of RelayApi->relay_controller_downloads_token_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RelayApi->relay_controller_downloads_token_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| The unique identifier for the request. |

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **relay_controller_files_token_post**
> object relay_controller_files_token_post(token)

Uploads a file to the connected controller.

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
    api_instance = slskd.RelayApi(api_client)
    token = 'token_example' # str | The unique identifier for the request.

    try:
        # Uploads a file to the connected controller.
        api_response = await api_instance.relay_controller_files_token_post(token)
        print("The response of RelayApi->relay_controller_files_token_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RelayApi->relay_controller_files_token_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| The unique identifier for the request. |

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **relay_controller_shares_token_post**
> object relay_controller_shares_token_post(token)

Uploads share information to the connected controller.

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
    api_instance = slskd.RelayApi(api_client)
    token = 'token_example' # str | The unique identifier for the request.

    try:
        # Uploads share information to the connected controller.
        api_response = await api_instance.relay_controller_shares_token_post(token)
        print("The response of RelayApi->relay_controller_shares_token_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RelayApi->relay_controller_shares_token_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| The unique identifier for the request. |

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
