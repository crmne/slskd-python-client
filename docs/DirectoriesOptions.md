# DirectoriesOptions

Directory options.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**incomplete** | **str** | Gets the path where incomplete downloads are saved. | [optional]
**downloads** | **str** | Gets the path where downloaded files are saved. | [optional]

## Example

```python
from slskd.models.directories_options import DirectoriesOptions

# TODO update the JSON string below
json = "{}"
# create an instance of DirectoriesOptions from a JSON string
directories_options_instance = DirectoriesOptions.from_json(json)
# print the JSON string representation of the object
print DirectoriesOptions.to_json()

# convert the object into a dict
directories_options_dict = directories_options_instance.to_dict()
# create an instance of DirectoriesOptions from a dict
directories_options_form_dict = directories_options.from_dict(directories_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
