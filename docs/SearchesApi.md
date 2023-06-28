# slskd.SearchesApi

All URIs are relative to *https://localhost:5031/api/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**searches_get**](SearchesApi.md#searches_get) | **GET** /searches | Gets the list of active and completed searches.
[**searches_id_delete**](SearchesApi.md#searches_id_delete) | **DELETE** /searches/{id} | Deletes the search corresponding to the specified id.
[**searches_id_get**](SearchesApi.md#searches_id_get) | **GET** /searches/{id} | Gets the state of the search corresponding to the specified id.
[**searches_id_put**](SearchesApi.md#searches_id_put) | **PUT** /searches/{id} | Stops the search corresponding to the specified id.
[**searches_id_responses_get**](SearchesApi.md#searches_id_responses_get) | **GET** /searches/{id}/responses | Gets the state of the search corresponding to the specified id.
[**searches_post**](SearchesApi.md#searches_post) | **POST** /searches | Performs a search for the specified request.


# **searches_get**
> searches_get()

Gets the list of active and completed searches.

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
    api_instance = slskd.SearchesApi(api_client)

    try:
        # Gets the list of active and completed searches.
        await api_instance.searches_get()
    except Exception as e:
        print("Exception when calling SearchesApi->searches_get: %s\n" % e)
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

# **searches_id_delete**
> searches_id_delete(id)

Deletes the search corresponding to the specified id.

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

No authorization required

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
> searches_id_get(id, include_responses=include_responses)

Gets the state of the search corresponding to the specified id.

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
    api_instance = slskd.SearchesApi(api_client)
    id = 'id_example' # str | The unique id of the search.
    include_responses = False # bool | A value indicating whether to include search responses in the response. (optional) (default to False)

    try:
        # Gets the state of the search corresponding to the specified id.
        await api_instance.searches_id_get(id, include_responses=include_responses)
    except Exception as e:
        print("Exception when calling SearchesApi->searches_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique id of the search. |
 **include_responses** | **bool**| A value indicating whether to include search responses in the response. | [optional] [default to False]

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
**200** | The request completed successfully. |  -  |
**404** | A matching search was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **searches_id_put**
> searches_id_put(id)

Stops the search corresponding to the specified id.

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
    api_instance = slskd.SearchesApi(api_client)
    id = 'id_example' # str | The unique id of the search.

    try:
        # Stops the search corresponding to the specified id.
        await api_instance.searches_id_put(id)
    except Exception as e:
        print("Exception when calling SearchesApi->searches_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique id of the search. |

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
**200** | The search was stopped. |  -  |
**304** | The search was not in progress. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **searches_id_responses_get**
> searches_id_responses_get(id)

Gets the state of the search corresponding to the specified id.

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
    api_instance = slskd.SearchesApi(api_client)
    id = 'id_example' # str | The unique id of the search.

    try:
        # Gets the state of the search corresponding to the specified id.
        await api_instance.searches_id_responses_get(id)
    except Exception as e:
        print("Exception when calling SearchesApi->searches_id_responses_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique id of the search. |

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
**200** | The request completed successfully. |  -  |
**404** | A matching search was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **searches_post**
> searches_post(search_request=search_request)

Performs a search for the specified request.

### Example

```python
import time
import os
import slskd
from slskd.models.search_request import SearchRequest
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
    api_instance = slskd.SearchesApi(api_client)
    search_request = slskd.SearchRequest() # SearchRequest | The search request. (optional)

    try:
        # Performs a search for the specified request.
        await api_instance.searches_post(search_request=search_request)
    except Exception as e:
        print("Exception when calling SearchesApi->searches_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_request** | [**SearchRequest**](SearchRequest.md)| The search request. | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The search completed successfully. |  -  |
**400** | The specified request was malformed. |  -  |
**500** | The search terminated abnormally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)