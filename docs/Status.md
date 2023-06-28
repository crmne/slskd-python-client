# Status

User status.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_privileged** | **bool** | Gets a value indicating whether the user is privileged. | [optional]
**presence** | [**UserPresence**](UserPresence.md) |  | [optional]

## Example

```python
from slskd.models.status import Status

# TODO update the JSON string below
json = "{}"
# create an instance of Status from a JSON string
status_instance = Status.from_json(json)
# print the JSON string representation of the object
print Status.to_json()

# convert the object into a dict
status_dict = status_instance.to_dict()
# create an instance of Status from a dict
status_form_dict = status.from_dict(status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
