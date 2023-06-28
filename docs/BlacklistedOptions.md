# BlacklistedOptions

Built in blacklisted group options.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**members** | **List[str]** | Gets the list of group member usernames. | [optional]

## Example

```python
from slskd.models.blacklisted_options import BlacklistedOptions

# TODO update the JSON string below
json = "{}"
# create an instance of BlacklistedOptions from a JSON string
blacklisted_options_instance = BlacklistedOptions.from_json(json)
# print the JSON string representation of the object
print BlacklistedOptions.to_json()

# convert the object into a dict
blacklisted_options_dict = blacklisted_options_instance.to_dict()
# create an instance of BlacklistedOptions from a dict
blacklisted_options_form_dict = blacklisted_options.from_dict(blacklisted_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
