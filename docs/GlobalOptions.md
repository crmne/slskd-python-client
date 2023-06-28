# GlobalOptions

Global options.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**upload** | [**GlobalUploadOptions**](GlobalUploadOptions.md) |  | [optional]
**download** | [**GlobalDownloadOptions**](GlobalDownloadOptions.md) |  | [optional]

## Example

```python
from slskd.models.global_options import GlobalOptions

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalOptions from a JSON string
global_options_instance = GlobalOptions.from_json(json)
# print the JSON string representation of the object
print GlobalOptions.to_json()

# convert the object into a dict
global_options_dict = global_options_instance.to_dict()
# create an instance of GlobalOptions from a dict
global_options_form_dict = global_options.from_dict(global_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
