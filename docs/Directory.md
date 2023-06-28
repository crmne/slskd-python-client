# Directory


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional]
**file_count** | **int** |  | [optional] [readonly]
**files** | [**List[File]**](File.md) |  | [optional] [readonly]

## Example

```python
from slskd.models.directory import Directory

# TODO update the JSON string below
json = "{}"
# create an instance of Directory from a JSON string
directory_instance = Directory.from_json(json)
# print the JSON string representation of the object
print Directory.to_json()

# convert the object into a dict
directory_dict = directory_instance.to_dict()
# create an instance of Directory from a dict
directory_form_dict = directory.from_dict(directory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
