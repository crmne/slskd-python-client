# slskd.PublicChatApi

All URIs are relative to *https://localhost:5031/api/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**publicchat_delete**](PublicChatApi.md#publicchat_delete) | **DELETE** /publicchat | Stops public chat.
[**publicchat_post**](PublicChatApi.md#publicchat_post) | **POST** /publicchat | Starts public chat.


# **publicchat_delete**
> publicchat_delete()

Stops public chat.

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
    api_instance = slskd.PublicChatApi(api_client)

    try:
        # Stops public chat.
        await api_instance.publicchat_delete()
    except Exception as e:
        print("Exception when calling PublicChatApi->publicchat_delete: %s\n" % e)
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

# **publicchat_post**
> publicchat_post()

Starts public chat.

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
    api_instance = slskd.PublicChatApi(api_client)

    try:
        # Starts public chat.
        await api_instance.publicchat_post()
    except Exception as e:
        print("Exception when calling PublicChatApi->publicchat_post: %s\n" % e)
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
