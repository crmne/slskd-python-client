# slskd.RoomsApi

All URIs are relative to *http://localhost:5030/api/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rooms_available_get**](RoomsApi.md#rooms_available_get) | **GET** /rooms/available | Gets a list of rooms from the server.
[**rooms_joined_get**](RoomsApi.md#rooms_joined_get) | **GET** /rooms/joined | Gets all rooms.
[**rooms_joined_post**](RoomsApi.md#rooms_joined_post) | **POST** /rooms/joined | Joins a room.
[**rooms_joined_room_name_delete**](RoomsApi.md#rooms_joined_room_name_delete) | **DELETE** /rooms/joined/{roomName} | Leaves a room.
[**rooms_joined_room_name_get**](RoomsApi.md#rooms_joined_room_name_get) | **GET** /rooms/joined/{roomName} | Gets the specified room.
[**rooms_joined_room_name_members_post**](RoomsApi.md#rooms_joined_room_name_members_post) | **POST** /rooms/joined/{roomName}/members | Adds a member to a private room.
[**rooms_joined_room_name_messages_get**](RoomsApi.md#rooms_joined_room_name_messages_get) | **GET** /rooms/joined/{roomName}/messages | Gets the current list of messages for the specified room.
[**rooms_joined_room_name_messages_post**](RoomsApi.md#rooms_joined_room_name_messages_post) | **POST** /rooms/joined/{roomName}/messages | Sends a message to the specified room.
[**rooms_joined_room_name_ticker_post**](RoomsApi.md#rooms_joined_room_name_ticker_post) | **POST** /rooms/joined/{roomName}/ticker | Sets a ticker for the specified room.
[**rooms_joined_room_name_users_get**](RoomsApi.md#rooms_joined_room_name_users_get) | **GET** /rooms/joined/{roomName}/users | Gets the current list of users for the specified room.


# **rooms_available_get**
> List[RoomInfo] rooms_available_get()

Gets a list of rooms from the server.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import slskd
from slskd.models.room_info import RoomInfo
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
    api_instance = slskd.RoomsApi(api_client)

    try:
        # Gets a list of rooms from the server.
        api_response = await api_instance.rooms_available_get()
        print("The response of RoomsApi->rooms_available_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomsApi->rooms_available_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**List[RoomInfo]**](RoomInfo.md)

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

# **rooms_joined_get**
> Dict[str, Dict[str, Room]] rooms_joined_get()

Gets all rooms.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import slskd
from slskd.models.room import Room
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
    api_instance = slskd.RoomsApi(api_client)

    try:
        # Gets all rooms.
        api_response = await api_instance.rooms_joined_get()
        print("The response of RoomsApi->rooms_joined_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomsApi->rooms_joined_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**Dict[str, Dict[str, Room]]**

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

# **rooms_joined_post**
> Room rooms_joined_post(body=body)

Joins a room.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import slskd
from slskd.models.room import Room
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
    api_instance = slskd.RoomsApi(api_client)
    body = 'body_example' # str |  (optional)

    try:
        # Joins a room.
        api_response = await api_instance.rooms_joined_post(body=body)
        print("The response of RoomsApi->rooms_joined_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomsApi->rooms_joined_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | [optional]

### Return type

[**Room**](Room.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The request completed successfully. |  -  |
**304** | The room has already been joined. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rooms_joined_room_name_delete**
> rooms_joined_room_name_delete(room_name)

Leaves a room.

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
    api_instance = slskd.RoomsApi(api_client)
    room_name = 'room_name_example' # str |

    try:
        # Leaves a room.
        await api_instance.rooms_joined_room_name_delete(room_name)
    except Exception as e:
        print("Exception when calling RoomsApi->rooms_joined_room_name_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **room_name** | **str**|  |

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
**404** | The room has not been joined. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rooms_joined_room_name_get**
> Room rooms_joined_room_name_get(room_name)

Gets the specified room.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import slskd
from slskd.models.room import Room
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
    api_instance = slskd.RoomsApi(api_client)
    room_name = 'room_name_example' # str |

    try:
        # Gets the specified room.
        api_response = await api_instance.rooms_joined_room_name_get(room_name)
        print("The response of RoomsApi->rooms_joined_room_name_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomsApi->rooms_joined_room_name_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **room_name** | **str**|  |

### Return type

[**Room**](Room.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request completed successfully. |  -  |
**404** | The specified roomName could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rooms_joined_room_name_members_post**
> rooms_joined_room_name_members_post(room_name, body=body)

Adds a member to a private room.

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
    api_instance = slskd.RoomsApi(api_client)
    room_name = 'room_name_example' # str |
    body = 'body_example' # str |  (optional)

    try:
        # Adds a member to a private room.
        await api_instance.rooms_joined_room_name_members_post(room_name, body=body)
    except Exception as e:
        print("Exception when calling RoomsApi->rooms_joined_room_name_members_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **room_name** | **str**|  |
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
**404** | The specified roomName could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rooms_joined_room_name_messages_get**
> List[RoomMessage] rooms_joined_room_name_messages_get(room_name)

Gets the current list of messages for the specified room.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import slskd
from slskd.models.room_message import RoomMessage
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
    api_instance = slskd.RoomsApi(api_client)
    room_name = 'room_name_example' # str |

    try:
        # Gets the current list of messages for the specified room.
        api_response = await api_instance.rooms_joined_room_name_messages_get(room_name)
        print("The response of RoomsApi->rooms_joined_room_name_messages_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomsApi->rooms_joined_room_name_messages_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **room_name** | **str**|  |

### Return type

[**List[RoomMessage]**](RoomMessage.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request completed successfully. |  -  |
**404** | The specified roomName could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rooms_joined_room_name_messages_post**
> rooms_joined_room_name_messages_post(room_name, body=body)

Sends a message to the specified room.

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
    api_instance = slskd.RoomsApi(api_client)
    room_name = 'room_name_example' # str |
    body = 'body_example' # str |  (optional)

    try:
        # Sends a message to the specified room.
        await api_instance.rooms_joined_room_name_messages_post(room_name, body=body)
    except Exception as e:
        print("Exception when calling RoomsApi->rooms_joined_room_name_messages_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **room_name** | **str**|  |
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
**404** | The specified roomName could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rooms_joined_room_name_ticker_post**
> rooms_joined_room_name_ticker_post(room_name, body=body)

Sets a ticker for the specified room.

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
    api_instance = slskd.RoomsApi(api_client)
    room_name = 'room_name_example' # str |
    body = 'body_example' # str |  (optional)

    try:
        # Sets a ticker for the specified room.
        await api_instance.rooms_joined_room_name_ticker_post(room_name, body=body)
    except Exception as e:
        print("Exception when calling RoomsApi->rooms_joined_room_name_ticker_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **room_name** | **str**|  |
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
**404** | The specified roomName could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rooms_joined_room_name_users_get**
> List[UserData] rooms_joined_room_name_users_get(room_name)

Gets the current list of users for the specified room.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import slskd
from slskd.models.user_data import UserData
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
    api_instance = slskd.RoomsApi(api_client)
    room_name = 'room_name_example' # str |

    try:
        # Gets the current list of users for the specified room.
        api_response = await api_instance.rooms_joined_room_name_users_get(room_name)
        print("The response of RoomsApi->rooms_joined_room_name_users_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomsApi->rooms_joined_room_name_users_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **room_name** | **str**|  |

### Return type

[**List[UserData]**](UserData.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request completed successfully. |  -  |
**404** | The specified roomName could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
