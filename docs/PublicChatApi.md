# slskd.PublicChatApi

All URIs are relative to *http://localhost:5030/api/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**publicchat_delete**](PublicChatApi.md#publicchat_delete) | **DELETE** /publicchat | Stops public chat.
[**publicchat_post**](PublicChatApi.md#publicchat_post) | **POST** /publicchat | Starts public chat.


# **publicchat_delete**
> object publicchat_delete()

Stops public chat.

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
    api_instance = slskd.PublicChatApi(api_client)

    try:
        # Stops public chat.
        api_response = await api_instance.publicchat_delete()
        print("The response of PublicChatApi->publicchat_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicChatApi->publicchat_delete: %s\n" % e)
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

# **publicchat_post**
> object publicchat_post()

Starts public chat.

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
    api_instance = slskd.PublicChatApi(api_client)

    try:
        # Starts public chat.
        api_response = await api_instance.publicchat_post()
        print("The response of PublicChatApi->publicchat_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicChatApi->publicchat_post: %s\n" % e)
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
