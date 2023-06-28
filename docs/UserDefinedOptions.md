# UserDefinedOptions

User defined user group options.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**upload** | [**UploadOptions**](UploadOptions.md) |  | [optional]
**members** | **List[str]** | Gets the list of group member usernames. | [optional]

## Example

```python
from slskd.models.user_defined_options import UserDefinedOptions

# TODO update the JSON string below
json = "{}"
# create an instance of UserDefinedOptions from a JSON string
user_defined_options_instance = UserDefinedOptions.from_json(json)
# print the JSON string representation of the object
print UserDefinedOptions.to_json()

# convert the object into a dict
user_defined_options_dict = user_defined_options_instance.to_dict()
# create an instance of UserDefinedOptions from a dict
user_defined_options_form_dict = user_defined_options.from_dict(user_defined_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
