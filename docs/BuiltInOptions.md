# BuiltInOptions

Built in user group options.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**upload** | [**UploadOptions**](UploadOptions.md) |  | [optional]

## Example

```python
from slskd.models.built_in_options import BuiltInOptions

# TODO update the JSON string below
json = "{}"
# create an instance of BuiltInOptions from a JSON string
built_in_options_instance = BuiltInOptions.from_json(json)
# print the JSON string representation of the object
print BuiltInOptions.to_json()

# convert the object into a dict
built_in_options_dict = built_in_options_instance.to_dict()
# create an instance of BuiltInOptions from a dict
built_in_options_form_dict = built_in_options.from_dict(built_in_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
