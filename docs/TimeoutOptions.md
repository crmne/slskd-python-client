# TimeoutOptions

Connection timeout options.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connect** | **int** | Gets the connection timeout value, in milliseconds. | [optional]
**inactivity** | **int** | Gets the connection inactivity timeout, in milliseconds. | [optional]

## Example

```python
from slskd.models.timeout_options import TimeoutOptions

# TODO update the JSON string below
json = "{}"
# create an instance of TimeoutOptions from a JSON string
timeout_options_instance = TimeoutOptions.from_json(json)
# print the JSON string representation of the object
print TimeoutOptions.to_json()

# convert the object into a dict
timeout_options_dict = timeout_options_instance.to_dict()
# create an instance of TimeoutOptions from a dict
timeout_options_form_dict = timeout_options.from_dict(timeout_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
