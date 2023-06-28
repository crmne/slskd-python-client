# slskd.TransfersApi

All URIs are relative to *https://localhost:5031/api/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**transfers_downloads_all_completed_delete**](TransfersApi.md#transfers_downloads_all_completed_delete) | **DELETE** /transfers/downloads/all/completed | Removes all completed downloads, regardless of whether they failed or succeeded.
[**transfers_downloads_get**](TransfersApi.md#transfers_downloads_get) | **GET** /transfers/downloads | Gets all downloads.
[**transfers_downloads_username_get**](TransfersApi.md#transfers_downloads_username_get) | **GET** /transfers/downloads/{username} | Gets all downloads for the specified username.
[**transfers_downloads_username_id_delete**](TransfersApi.md#transfers_downloads_username_id_delete) | **DELETE** /transfers/downloads/{username}/{id} | Cancels the specified download.
[**transfers_downloads_username_id_get**](TransfersApi.md#transfers_downloads_username_id_get) | **GET** /transfers/downloads/{username}/{id} |
[**transfers_downloads_username_id_position_get**](TransfersApi.md#transfers_downloads_username_id_position_get) | **GET** /transfers/downloads/{username}/{id}/position | Gets the downlaod for the specified username matching the specified filename, and requests  the current place in the remote queue of the specified download.
[**transfers_downloads_username_post**](TransfersApi.md#transfers_downloads_username_post) | **POST** /transfers/downloads/{username} | Enqueues the specified download.
[**transfers_uploads_all_completed_delete**](TransfersApi.md#transfers_uploads_all_completed_delete) | **DELETE** /transfers/uploads/all/completed | Removes all completed uploads, regardless of whether they failed or succeeded.
[**transfers_uploads_get**](TransfersApi.md#transfers_uploads_get) | **GET** /transfers/uploads | Gets all uploads.
[**transfers_uploads_username_get**](TransfersApi.md#transfers_uploads_username_get) | **GET** /transfers/uploads/{username} | Gets all uploads for the specified username.
[**transfers_uploads_username_id_delete**](TransfersApi.md#transfers_uploads_username_id_delete) | **DELETE** /transfers/uploads/{username}/{id} | Cancels the specified upload.
[**transfers_uploads_username_id_get**](TransfersApi.md#transfers_uploads_username_id_get) | **GET** /transfers/uploads/{username}/{id} | Gets the upload for the specified username matching the specified filename.


# **transfers_downloads_all_completed_delete**
> transfers_downloads_all_completed_delete()

Removes all completed downloads, regardless of whether they failed or succeeded.

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
    api_instance = slskd.TransfersApi(api_client)

    try:
        # Removes all completed downloads, regardless of whether they failed or succeeded.
        await api_instance.transfers_downloads_all_completed_delete()
    except Exception as e:
        print("Exception when calling TransfersApi->transfers_downloads_all_completed_delete: %s\n" % e)
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
**204** | The downloads were removed successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfers_downloads_get**
> transfers_downloads_get(include_removed=include_removed)

Gets all downloads.

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
    api_instance = slskd.TransfersApi(api_client)
    include_removed = False # bool |  (optional) (default to False)

    try:
        # Gets all downloads.
        await api_instance.transfers_downloads_get(include_removed=include_removed)
    except Exception as e:
        print("Exception when calling TransfersApi->transfers_downloads_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_removed** | **bool**|  | [optional] [default to False]

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfers_downloads_username_get**
> transfers_downloads_username_get(username)

Gets all downloads for the specified username.

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
    api_instance = slskd.TransfersApi(api_client)
    username = 'username_example' # str |

    try:
        # Gets all downloads for the specified username.
        await api_instance.transfers_downloads_username_get(username)
    except Exception as e:
        print("Exception when calling TransfersApi->transfers_downloads_username_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  |

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfers_downloads_username_id_delete**
> transfers_downloads_username_id_delete(username, id, remove=remove)

Cancels the specified download.

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
    api_instance = slskd.TransfersApi(api_client)
    username = 'username_example' # str | The username of the download source.
    id = 'id_example' # str | The id of the download.
    remove = False # bool | A value indicating whether the tracked download should be removed after cancellation. (optional) (default to False)

    try:
        # Cancels the specified download.
        await api_instance.transfers_downloads_username_id_delete(username, id, remove=remove)
    except Exception as e:
        print("Exception when calling TransfersApi->transfers_downloads_username_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username of the download source. |
 **id** | **str**| The id of the download. |
 **remove** | **bool**| A value indicating whether the tracked download should be removed after cancellation. | [optional] [default to False]

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
**204** | The download was cancelled successfully. |  -  |
**404** | The specified download was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfers_downloads_username_id_get**
> Transfer transfers_downloads_username_id_get(username, id)



### Example

```python
import time
import os
import slskd
from slskd.models.transfer import Transfer
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
    api_instance = slskd.TransfersApi(api_client)
    username = 'username_example' # str |
    id = 'id_example' # str |

    try:
        api_response = await api_instance.transfers_downloads_username_id_get(username, id)
        print("The response of TransfersApi->transfers_downloads_username_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransfersApi->transfers_downloads_username_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  |
 **id** | **str**|  |

### Return type

[**Transfer**](Transfer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfers_downloads_username_id_position_get**
> Transfer transfers_downloads_username_id_position_get(username, id)

Gets the downlaod for the specified username matching the specified filename, and requests  the current place in the remote queue of the specified download.

### Example

```python
import time
import os
import slskd
from slskd.models.transfer import Transfer
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
    api_instance = slskd.TransfersApi(api_client)
    username = 'username_example' # str | The username of the download source.
    id = 'id_example' # str | The id of the download.

    try:
        # Gets the downlaod for the specified username matching the specified filename, and requests  the current place in the remote queue of the specified download.
        api_response = await api_instance.transfers_downloads_username_id_position_get(username, id)
        print("The response of TransfersApi->transfers_downloads_username_id_position_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransfersApi->transfers_downloads_username_id_position_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username of the download source. |
 **id** | **str**| The id of the download. |

### Return type

[**Transfer**](Transfer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request completed successfully. |  -  |
**404** | The specified download was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfers_downloads_username_post**
> transfers_downloads_username_post(username, queue_download_request=queue_download_request)

Enqueues the specified download.

### Example

```python
import time
import os
import slskd
from slskd.models.queue_download_request import QueueDownloadRequest
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
    api_instance = slskd.TransfersApi(api_client)
    username = 'username_example' # str | The username of the download source.
    queue_download_request = [slskd.QueueDownloadRequest()] # List[QueueDownloadRequest] | The list of download requests. (optional)

    try:
        # Enqueues the specified download.
        await api_instance.transfers_downloads_username_post(username, queue_download_request=queue_download_request)
    except Exception as e:
        print("Exception when calling TransfersApi->transfers_downloads_username_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username of the download source. |
 **queue_download_request** | [**List[QueueDownloadRequest]**](QueueDownloadRequest.md)| The list of download requests. | [optional]

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
**201** | The download was successfully enqueued. |  -  |
**403** | The download was rejected. |  -  |
**500** | An unexpected error was encountered. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfers_uploads_all_completed_delete**
> transfers_uploads_all_completed_delete()

Removes all completed uploads, regardless of whether they failed or succeeded.

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
    api_instance = slskd.TransfersApi(api_client)

    try:
        # Removes all completed uploads, regardless of whether they failed or succeeded.
        await api_instance.transfers_uploads_all_completed_delete()
    except Exception as e:
        print("Exception when calling TransfersApi->transfers_uploads_all_completed_delete: %s\n" % e)
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
**204** | The uploads were removed successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfers_uploads_get**
> transfers_uploads_get(include_removed=include_removed)

Gets all uploads.

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
    api_instance = slskd.TransfersApi(api_client)
    include_removed = False # bool |  (optional) (default to False)

    try:
        # Gets all uploads.
        await api_instance.transfers_uploads_get(include_removed=include_removed)
    except Exception as e:
        print("Exception when calling TransfersApi->transfers_uploads_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_removed** | **bool**|  | [optional] [default to False]

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfers_uploads_username_get**
> transfers_uploads_username_get(username)

Gets all uploads for the specified username.

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
    api_instance = slskd.TransfersApi(api_client)
    username = 'username_example' # str |

    try:
        # Gets all uploads for the specified username.
        await api_instance.transfers_uploads_username_get(username)
    except Exception as e:
        print("Exception when calling TransfersApi->transfers_uploads_username_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  |

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfers_uploads_username_id_delete**
> transfers_uploads_username_id_delete(username, id, remove=remove)

Cancels the specified upload.

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
    api_instance = slskd.TransfersApi(api_client)
    username = 'username_example' # str | The username of the upload destination.
    id = 'id_example' # str | The id of the upload.
    remove = False # bool | A value indicating whether the tracked upload should be removed after cancellation. (optional) (default to False)

    try:
        # Cancels the specified upload.
        await api_instance.transfers_uploads_username_id_delete(username, id, remove=remove)
    except Exception as e:
        print("Exception when calling TransfersApi->transfers_uploads_username_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username of the upload destination. |
 **id** | **str**| The id of the upload. |
 **remove** | **bool**| A value indicating whether the tracked upload should be removed after cancellation. | [optional] [default to False]

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
**204** | The upload was cancelled successfully. |  -  |
**404** | The specified upload was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfers_uploads_username_id_get**
> transfers_uploads_username_id_get(username, id)

Gets the upload for the specified username matching the specified filename.

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
    api_instance = slskd.TransfersApi(api_client)
    username = 'username_example' # str | The username of the upload destination.
    id = 'id_example' # str | The id of the upload.

    try:
        # Gets the upload for the specified username matching the specified filename.
        await api_instance.transfers_uploads_username_id_get(username, id)
    except Exception as e:
        print("Exception when calling TransfersApi->transfers_uploads_username_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username of the upload destination. |
 **id** | **str**| The id of the upload. |

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
