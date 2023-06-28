# QueueDownloadRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **str** | Gets or sets the filename to download. | [optional]
**size** | **int** | Gets or sets the size of the file. | [optional]

## Example

```python
from slskd.models.queue_download_request import QueueDownloadRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QueueDownloadRequest from a JSON string
queue_download_request_instance = QueueDownloadRequest.from_json(json)
# print the JSON string representation of the object
print QueueDownloadRequest.to_json()

# convert the object into a dict
queue_download_request_dict = queue_download_request_instance.to_dict()
# create an instance of QueueDownloadRequest from a dict
queue_download_request_form_dict = queue_download_request.from_dict(queue_download_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
