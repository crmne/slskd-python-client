# SearchRequest

A search request.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Gets or sets the unique search identifier. | [optional]
**file_limit** | **int** | Gets or sets the maximum number of file results to accept before the search is considered complete. (Default &#x3D; 10,000). | [optional]
**filter_responses** | **bool** | Gets or sets a value indicating whether responses are to be filtered. (Default &#x3D; true). | [optional]
**maximum_peer_queue_length** | **int** | Gets or sets the maximum queue depth a peer may have in order for a response to be processed. (Default &#x3D; 1000000). | [optional]
**minimum_peer_upload_speed** | **int** | Gets or sets the minimum upload speed a peer must have in order for a response to be processed. (Default &#x3D; 0). | [optional]
**minimum_response_file_count** | **int** | Gets or sets the minimum number of files a response must contain in order to be processed. (Default &#x3D; 1). | [optional]
**response_limit** | **int** | Gets or sets the maximum number of search results to accept before the search is considered complete. (Default &#x3D; 100). | [optional]
**search_text** | **str** | Gets or sets the search text. | [optional]
**search_timeout** | **int** | Gets or sets the search timeout value, in seconds, used to determine when the search is complete. (Default &#x3D; 15). | [optional]
**token** | **int** | Gets or sets the search token. | [optional]

## Example

```python
from slskd.models.search_request import SearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SearchRequest from a JSON string
search_request_instance = SearchRequest.from_json(json)
# print the JSON string representation of the object
print SearchRequest.to_json()

# convert the object into a dict
search_request_dict = search_request_instance.to_dict()
# create an instance of SearchRequest from a dict
search_request_form_dict = search_request.from_dict(search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
