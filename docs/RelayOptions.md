# RelayOptions

Relay options.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Gets a value indicating whether the relay is enabled. | [optional]
**mode** | **str** | Gets the relay mode. | [optional]
**controller** | [**RelayControllerConfigurationOptions**](RelayControllerConfigurationOptions.md) |  | [optional]
**agents** | [**Dict[str, RelayAgentConfigurationOptions]**](RelayAgentConfigurationOptions.md) | Gets the agent configuration. | [optional]

## Example

```python
from slskd.models.relay_options import RelayOptions

# TODO update the JSON string below
json = "{}"
# create an instance of RelayOptions from a JSON string
relay_options_instance = RelayOptions.from_json(json)
# print the JSON string representation of the object
print RelayOptions.to_json()

# convert the object into a dict
relay_options_dict = relay_options_instance.to_dict()
# create an instance of RelayOptions from a dict
relay_options_form_dict = relay_options.from_dict(relay_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
