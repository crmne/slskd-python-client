# slskd.SearchesApi

All URIs are relative to *http://localhost:5030/api/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**searches_get**](SearchesApi.md#searches_get) | **GET** /searches | Gets the list of active and completed searches.
[**searches_id_delete**](SearchesApi.md#searches_id_delete) | **DELETE** /searches/{id} | Deletes the search corresponding to the specified id.
[**searches_id_get**](SearchesApi.md#searches_id_get) | **GET** /searches/{id} | Gets the state of the search corresponding to the specified id.
[**searches_id_put**](SearchesApi.md#searches_id_put) | **PUT** /searches/{id} | Stops the search corresponding to the specified id.
[**searches_id_responses_get**](SearchesApi.md#searches_id_responses_get) | **GET** /searches/{id}/responses | Gets the state of the search corresponding to the specified id.
[**searches_post**](SearchesApi.md#searches_post) | **POST** /searches | Performs a search for the specified request.


# **searches_get**
> object searches_get()

Gets the list of active and completed searches.

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
    api_instance = slskd.SearchesApi(api_client)

    try:
        # Gets the list of active and completed searches.
        api_response = await api_instance.searches_get()
        print("The response of SearchesApi->searches_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchesApi->searches_get: %s\n" % e)
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

# **searches_id_delete**
> searches_id_delete(id)

Deletes the search corresponding to the specified id.

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
    api_instance = slskd.SearchesApi(api_client)
    id = 'id_example' # str | The unique id of the search.

    try:
        # Deletes the search corresponding to the specified id.
        await api_instance.searches_id_delete(id)
    except Exception as e:
        print("Exception when calling SearchesApi->searches_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique id of the search. |

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
**204** | The search was deleted. |  -  |
**404** | A search with the specified id could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **searches_id_get**
> object searches_id_get(id, include_responses=include_responses)

Gets the state of the search corresponding to the specified id.

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
    api_instance = slskd.SearchesApi(api_client)
    id = 'id_example' # str | The unique id of the search.
    include_responses = False # bool | A value indicating whether to include search responses in the response. (optional) (default to False)

    try:
        # Gets the state of the search corresponding to the specified id.
        api_response = await api_instance.searches_id_get(id, include_responses=include_responses)
        print("The response of SearchesApi->searches_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchesApi->searches_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique id of the search. |
 **include_responses** | **bool**| A value indicating whether to include search responses in the response. | [optional] [default to False]

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
**404** | A matching search was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **searches_id_put**
> object searches_id_put(id)

Stops the search corresponding to the specified id.

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
    api_instance = slskd.SearchesApi(api_client)
    id = 'id_example' # str | The unique id of the search.

    try:
        # Stops the search corresponding to the specified id.
        api_response = await api_instance.searches_id_put(id)
        print("The response of SearchesApi->searches_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchesApi->searches_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique id of the search. |

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
**200** | The search was stopped. |  -  |
**304** | The search was not in progress. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **searches_id_responses_get**
> object searches_id_responses_get(id)

Gets the state of the search corresponding to the specified id.

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
    api_instance = slskd.SearchesApi(api_client)
    id = 'id_example' # str | The unique id of the search.

    try:
        # Gets the state of the search corresponding to the specified id.
        api_response = await api_instance.searches_id_responses_get(id)
        print("The response of SearchesApi->searches_id_responses_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchesApi->searches_id_responses_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique id of the search. |

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
**404** | A matching search was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **searches_post**
> object searches_post(search_request=search_request)

Performs a search for the specified request.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import slskd
from slskd.models.search_request import SearchRequest
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
    api_instance = slskd.SearchesApi(api_client)
    search_request = slskd.SearchRequest() # SearchRequest | The search request. (optional)

    try:
        # Performs a search for the specified request.
        api_response = await api_instance.searches_post(search_request=search_request)
        print("The response of SearchesApi->searches_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchesApi->searches_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_request** | [**SearchRequest**](SearchRequest.md)| The search request. | [optional]

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The search completed successfully. |  -  |
**400** | The specified request was malformed. |  -  |
**500** | The search terminated abnormally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
