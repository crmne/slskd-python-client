# FileAttribute


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**FileAttributeType**](FileAttributeType.md) |  | [optional]
**value** | **int** |  | [optional]

## Example

```python
from slskd.models.file_attribute import FileAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of FileAttribute from a JSON string
file_attribute_instance = FileAttribute.from_json(json)
# print the JSON string representation of the object
print FileAttribute.to_json()

# convert the object into a dict
file_attribute_dict = file_attribute_instance.to_dict()
# create an instance of FileAttribute from a dict
file_attribute_form_dict = file_attribute.from_dict(file_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
