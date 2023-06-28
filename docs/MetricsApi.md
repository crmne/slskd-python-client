# slskd.MetricsApi

All URIs are relative to *https://localhost:5031/api/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**metrics_get**](MetricsApi.md#metrics_get) | **GET** /metrics | Gets application metrics.


# **metrics_get**
> metrics_get()

Gets application metrics.

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
    api_instance = slskd.MetricsApi(api_client)

    try:
        # Gets application metrics.
        await api_instance.metrics_get()
    except Exception as e:
        print("Exception when calling MetricsApi->metrics_get: %s\n" % e)
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
