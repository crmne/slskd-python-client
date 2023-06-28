# slskd.ServerApi

All URIs are relative to *https://localhost:5031/api/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**server_delete**](ServerApi.md#server_delete) | **DELETE** /server | Disconnects the client.
[**server_get**](ServerApi.md#server_get) | **GET** /server | Retrieves the current state of the server.
[**server_put**](ServerApi.md#server_put) | **PUT** /server | Connects the client.


# **server_delete**
> server_delete(body=body)

Disconnects the client.

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
    api_instance = slskd.ServerApi(api_client)
    body = 'body_example' # str |  (optional)

    try:
        # Disconnects the client.
        await api_instance.server_delete(body=body)
    except Exception as e:
        print("Exception when calling ServerApi->server_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **server_get**
> ServerState server_get()

Retrieves the current state of the server.

### Example

```python
import time
import os
import slskd
from slskd.models.server_state import ServerState
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
    api_instance = slskd.ServerApi(api_client)

    try:
        # Retrieves the current state of the server.
        api_response = await api_instance.server_get()
        print("The response of ServerApi->server_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServerApi->server_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ServerState**](ServerState.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **server_put**
> server_put()

Connects the client.

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
    api_instance = slskd.ServerApi(api_client)

    try:
        # Connects the client.
        await api_instance.server_put()
    except Exception as e:
        print("Exception when calling ServerApi->server_put: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)