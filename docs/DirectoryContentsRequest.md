# DirectoryContentsRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**directory** | **str** |  | [optional]

## Example

```python
from slskd.models.directory_contents_request import DirectoryContentsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DirectoryContentsRequest from a JSON string
directory_contents_request_instance = DirectoryContentsRequest.from_json(json)
# print the JSON string representation of the object
print DirectoryContentsRequest.to_json()

# convert the object into a dict
directory_contents_request_dict = directory_contents_request_instance.to_dict()
# create an instance of DirectoryContentsRequest from a dict
directory_contents_request_form_dict = directory_contents_request.from_dict(directory_contents_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
