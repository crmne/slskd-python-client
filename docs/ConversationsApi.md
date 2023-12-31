# slskd.ConversationsApi

All URIs are relative to *http://localhost:5030/api/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**conversations_get**](ConversationsApi.md#conversations_get) | **GET** /conversations | Gets all active conversations.
[**conversations_username_delete**](ConversationsApi.md#conversations_username_delete) | **DELETE** /conversations/{username} | Closes the conversation associated with the given username.
[**conversations_username_get**](ConversationsApi.md#conversations_username_get) | **GET** /conversations/{username} | Gets the conversation associated with the specified username.
[**conversations_username_id_put**](ConversationsApi.md#conversations_username_id_put) | **PUT** /conversations/{username}/{id} | Acknowledges the given message id for the given username.
[**conversations_username_messages_get**](ConversationsApi.md#conversations_username_messages_get) | **GET** /conversations/{username}/messages |
[**conversations_username_post**](ConversationsApi.md#conversations_username_post) | **POST** /conversations/{username} | Sends a private message to the specified username.
[**conversations_username_put**](ConversationsApi.md#conversations_username_put) | **PUT** /conversations/{username} | Acknowledges all messages from the given username.


# **conversations_get**
> List[Conversation] conversations_get(include_inactive=include_inactive, un_acknowledged_only=un_acknowledged_only)

Gets all active conversations.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import slskd
from slskd.models.conversation import Conversation
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
    api_instance = slskd.ConversationsApi(api_client)
    include_inactive = False # bool |  (optional) (default to False)
    un_acknowledged_only = False # bool |  (optional) (default to False)

    try:
        # Gets all active conversations.
        api_response = await api_instance.conversations_get(include_inactive=include_inactive, un_acknowledged_only=un_acknowledged_only)
        print("The response of ConversationsApi->conversations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConversationsApi->conversations_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_inactive** | **bool**|  | [optional] [default to False]
 **un_acknowledged_only** | **bool**|  | [optional] [default to False]

### Return type

[**List[Conversation]**](Conversation.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request completed successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **conversations_username_delete**
> conversations_username_delete(username)

Closes the conversation associated with the given username.

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
    api_instance = slskd.ConversationsApi(api_client)
    username = 'username_example' # str |

    try:
        # Closes the conversation associated with the given username.
        await api_instance.conversations_username_delete(username)
    except Exception as e:
        print("Exception when calling ConversationsApi->conversations_username_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  |

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The request completed successfully. |  -  |
**404** | A conversation with the specified username could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **conversations_username_get**
> Conversation conversations_username_get(username, include_messages=include_messages)

Gets the conversation associated with the specified username.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import slskd
from slskd.models.conversation import Conversation
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
    api_instance = slskd.ConversationsApi(api_client)
    username = 'username_example' # str | The username associated with the desired conversation.
    include_messages = True # bool |  (optional) (default to True)

    try:
        # Gets the conversation associated with the specified username.
        api_response = await api_instance.conversations_username_get(username, include_messages=include_messages)
        print("The response of ConversationsApi->conversations_username_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConversationsApi->conversations_username_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username associated with the desired conversation. |
 **include_messages** | **bool**|  | [optional] [default to True]

### Return type

[**Conversation**](Conversation.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request completed successfully. |  -  |
**404** | A matching search was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **conversations_username_id_put**
> object conversations_username_id_put(username, id)

Acknowledges the given message id for the given username.

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
    api_instance = slskd.ConversationsApi(api_client)
    username = 'username_example' # str |
    id = 56 # int |

    try:
        # Acknowledges the given message id for the given username.
        api_response = await api_instance.conversations_username_id_put(username, id)
        print("The response of ConversationsApi->conversations_username_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConversationsApi->conversations_username_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  |
 **id** | **int**|  |

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
**200** | The request completed successfully. |  -  |
**404** | A conversation with the specified username, or a message matching the specified id could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **conversations_username_messages_get**
> List[PrivateMessage] conversations_username_messages_get(username, un_acknowledged_only=un_acknowledged_only)



### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import slskd
from slskd.models.private_message import PrivateMessage
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
    api_instance = slskd.ConversationsApi(api_client)
    username = 'username_example' # str |
    un_acknowledged_only = False # bool |  (optional) (default to False)

    try:
        api_response = await api_instance.conversations_username_messages_get(username, un_acknowledged_only=un_acknowledged_only)
        print("The response of ConversationsApi->conversations_username_messages_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConversationsApi->conversations_username_messages_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  |
 **un_acknowledged_only** | **bool**|  | [optional] [default to False]

### Return type

[**List[PrivateMessage]**](PrivateMessage.md)

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

# **conversations_username_post**
> conversations_username_post(username, body=body)

Sends a private message to the specified username.

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
    api_instance = slskd.ConversationsApi(api_client)
    username = 'username_example' # str |
    body = 'body_example' # str |  (optional)

    try:
        # Sends a private message to the specified username.
        await api_instance.conversations_username_post(username, body=body)
    except Exception as e:
        print("Exception when calling ConversationsApi->conversations_username_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  |
 **body** | **str**|  | [optional]

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The request completed successfully. |  -  |
**400** | The specified message is null or empty. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **conversations_username_put**
> object conversations_username_put(username)

Acknowledges all messages from the given username.

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
    api_instance = slskd.ConversationsApi(api_client)
    username = 'username_example' # str |

    try:
        # Acknowledges all messages from the given username.
        api_response = await api_instance.conversations_username_put(username)
        print("The response of ConversationsApi->conversations_username_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConversationsApi->conversations_username_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  |

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
**200** | The request completed successfully. |  -  |
**404** | A conversation with the specified username could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
