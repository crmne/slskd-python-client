# slskd.SessionApi

All URIs are relative to *http://localhost:5030/api/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**session_enabled_get**](SessionApi.md#session_enabled_get) | **GET** /session/enabled | Checks whether security is enabled.
[**session_get**](SessionApi.md#session_get) | **GET** /session | Checks whether the provided authentication is valid.
[**session_post**](SessionApi.md#session_post) | **POST** /session | Logs in.


# **session_enabled_get**
> bool session_enabled_get()

Checks whether security is enabled.

### Example

* Bearer (JWT) Authentication (bearerAuth):
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = slskd.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with slskd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slskd.SessionApi(api_client)

    try:
        # Checks whether security is enabled.
        api_response = await api_instance.session_enabled_get()
        print("The response of SessionApi->session_enabled_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionApi->session_enabled_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**bool**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | True if security is enabled, false otherwise. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **session_get**
> session_get()

Checks whether the provided authentication is valid.

This is a no-op provided so that the application can test for an expired token on load.

### Example

* Bearer (JWT) Authentication (bearerAuth):
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = slskd.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with slskd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slskd.SessionApi(api_client)

    try:
        # Checks whether the provided authentication is valid.
        await api_instance.session_get()
    except Exception as e:
        print("Exception when calling SessionApi->session_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The authentication is valid. |  -  |
**401** | Unauthorized |  -  |
**403** | The authentication is is invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **session_post**
> TokenResponse session_post(login_request=login_request)

Logs in.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import os
import slskd
from slskd.models.login_request import LoginRequest
from slskd.models.token_response import TokenResponse
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = slskd.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with slskd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slskd.SessionApi(api_client)
    login_request = slskd.LoginRequest() # LoginRequest |  (optional)

    try:
        # Logs in.
        api_response = await api_instance.session_post(login_request=login_request)
        print("The response of SessionApi->session_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionApi->session_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_request** | [**LoginRequest**](LoginRequest.md)|  | [optional]

### Return type

[**TokenResponse**](TokenResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Login was successful. |  -  |
**400** | Bad request. |  -  |
**401** | Login failed. |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
