# UploadOptions

User group upload options.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**priority** | **int** | Gets the priority of the group. | [optional]
**strategy** | **str** | Gets the queue strategy for the group. | [optional]
**slots** | **int** | Gets the limit for the total number of upload slots for the group. | [optional]
**speed_limit** | **int** | Gets the total upload speed limit for the group. | [optional]

## Example

```python
from slskd.models.upload_options import UploadOptions

# TODO update the JSON string below
json = "{}"
# create an instance of UploadOptions from a JSON string
upload_options_instance = UploadOptions.from_json(json)
# print the JSON string representation of the object
print UploadOptions.to_json()

# convert the object into a dict
upload_options_dict = upload_options_instance.to_dict()
# create an instance of UploadOptions from a dict
upload_options_form_dict = upload_options.from_dict(upload_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
