# File


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_count** | **int** |  | [optional] [readonly]
**attributes** | [**List[FileAttribute]**](FileAttribute.md) |  | [optional] [readonly]
**bit_depth** | **int** |  | [optional] [readonly]
**bit_rate** | **int** |  | [optional] [readonly]
**code** | **int** |  | [optional]
**extension** | **str** |  | [optional]
**filename** | **str** |  | [optional]
**is_variable_bit_rate** | **bool** |  | [optional] [readonly]
**length** | **int** |  | [optional] [readonly]
**sample_rate** | **int** |  | [optional] [readonly]
**size** | **int** |  | [optional]

## Example

```python
from slskd.models.file import File

# TODO update the JSON string below
json = "{}"
# create an instance of File from a JSON string
file_instance = File.from_json(json)
# print the JSON string representation of the object
print File.to_json()

# convert the object into a dict
file_dict = file_instance.to_dict()
# create an instance of File from a dict
file_form_dict = file.from_dict(file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
