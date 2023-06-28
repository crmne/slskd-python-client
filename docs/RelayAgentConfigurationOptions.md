# RelayAgentConfigurationOptions

Relay agent configuration options.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance_name** | **str** | Gets the agent instance name. | [optional]
**secret** | **str** | Gets the agent secret. | [optional]
**cidr** | **str** | Gets the comma separated list of CIDRs that are authorized to connect as this agent. | [optional]

## Example

```python
from slskd.models.relay_agent_configuration_options import RelayAgentConfigurationOptions

# TODO update the JSON string below
json = "{}"
# create an instance of RelayAgentConfigurationOptions from a JSON string
relay_agent_configuration_options_instance = RelayAgentConfigurationOptions.from_json(json)
# print the JSON string representation of the object
print RelayAgentConfigurationOptions.to_json()

# convert the object into a dict
relay_agent_configuration_options_dict = relay_agent_configuration_options_instance.to_dict()
# create an instance of RelayAgentConfigurationOptions from a dict
relay_agent_configuration_options_form_dict = relay_agent_configuration_options.from_dict(relay_agent_configuration_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
