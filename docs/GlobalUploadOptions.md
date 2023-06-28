# GlobalUploadOptions

Global upload options.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slots** | **int** | Gets the limit for the total number of upload slots. | [optional]
**speed_limit** | **int** | Gets the total upload speed limit. | [optional]

## Example

```python
from slskd.models.global_upload_options import GlobalUploadOptions

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalUploadOptions from a JSON string
global_upload_options_instance = GlobalUploadOptions.from_json(json)
# print the JSON string representation of the object
print GlobalUploadOptions.to_json()

# convert the object into a dict
global_upload_options_dict = global_upload_options_instance.to_dict()
# create an instance of GlobalUploadOptions from a dict
global_upload_options_form_dict = global_upload_options.from_dict(global_upload_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
