# slskd.RelayApi

All URIs are relative to *https://localhost:5031/api/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**relay_agent_delete**](RelayApi.md#relay_agent_delete) | **DELETE** /relay/agent | Disconnects from the connected controller.
[**relay_agent_put**](RelayApi.md#relay_agent_put) | **PUT** /relay/agent | Connects to the configured controller.
[**relay_controller_downloads_token_get**](RelayApi.md#relay_controller_downloads_token_get) | **GET** /relay/controller/downloads/{token} | Downloads a file from the connected controller.
[**relay_controller_files_token_post**](RelayApi.md#relay_controller_files_token_post) | **POST** /relay/controller/files/{token} | Uploads a file to the connected controller.
[**relay_controller_shares_token_post**](RelayApi.md#relay_controller_shares_token_post) | **POST** /relay/controller/shares/{token} | Uploads share information to the connected controller.


# **relay_agent_delete**
> relay_agent_delete()

Disconnects from the connected controller.

### Example

```python
import time
import os
import slskd
from slskd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:5031/api/v0
# See configuration.py for a list of all supported configuration parameters.
configuration = slskd.Configuration(
    host = "https://localhost:5031/api/v0"
)


# Enter a context with an instance of the API client
async with slskd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slskd.RelayApi(api_client)

    try:
        # Disconnects from the connected controller.
        await api_instance.relay_agent_delete()
    except Exception as e:
        print("Exception when calling RelayApi->relay_agent_delete: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **relay_agent_put**
> relay_agent_put()

Connects to the configured controller.

### Example

```python
import time
import os
import slskd
from slskd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:5031/api/v0
# See configuration.py for a list of all supported configuration parameters.
configuration = slskd.Configuration(
    host = "https://localhost:5031/api/v0"
)


# Enter a context with an instance of the API client
async with slskd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slskd.RelayApi(api_client)

    try:
        # Connects to the configured controller.
        await api_instance.relay_agent_put()
    except Exception as e:
        print("Exception when calling RelayApi->relay_agent_put: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **relay_controller_downloads_token_get**
> relay_controller_downloads_token_get(token)

Downloads a file from the connected controller.

### Example

```python
import time
import os
import slskd
from slskd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:5031/api/v0
# See configuration.py for a list of all supported configuration parameters.
configuration = slskd.Configuration(
    host = "https://localhost:5031/api/v0"
)


# Enter a context with an instance of the API client
async with slskd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slskd.RelayApi(api_client)
    token = 'token_example' # str | The unique identifier for the request.

    try:
        # Downloads a file from the connected controller.
        await api_instance.relay_controller_downloads_token_get(token)
    except Exception as e:
        print("Exception when calling RelayApi->relay_controller_downloads_token_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| The unique identifier for the request. |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **relay_controller_files_token_post**
> relay_controller_files_token_post(token)

Uploads a file to the connected controller.

### Example

```python
import time
import os
import slskd
from slskd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:5031/api/v0
# See configuration.py for a list of all supported configuration parameters.
configuration = slskd.Configuration(
    host = "https://localhost:5031/api/v0"
)


# Enter a context with an instance of the API client
async with slskd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slskd.RelayApi(api_client)
    token = 'token_example' # str | The unique identifier for the request.

    try:
        # Uploads a file to the connected controller.
        await api_instance.relay_controller_files_token_post(token)
    except Exception as e:
        print("Exception when calling RelayApi->relay_controller_files_token_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| The unique identifier for the request. |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **relay_controller_shares_token_post**
> relay_controller_shares_token_post(token)

Uploads share information to the connected controller.

### Example

```python
import time
import os
import slskd
from slskd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:5031/api/v0
# See configuration.py for a list of all supported configuration parameters.
configuration = slskd.Configuration(
    host = "https://localhost:5031/api/v0"
)


# Enter a context with an instance of the API client
async with slskd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slskd.RelayApi(api_client)
    token = 'token_example' # str | The unique identifier for the request.

    try:
        # Uploads share information to the connected controller.
        await api_instance.relay_controller_shares_token_post(token)
    except Exception as e:
        print("Exception when calling RelayApi->relay_controller_shares_token_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| The unique identifier for the request. |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
