# SoulseekOptions

Soulseek client options.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | Gets the username for the Soulseek network. | [optional]
**password** | **str** | Gets the password for the Soulseek network. | [optional]
**description** | **str** | Gets the description of the Soulseek user. | [optional]
**listen_port** | **int** | Gets the port on which to listen for incoming connections. | [optional]
**diagnostic_level** | [**DiagnosticLevel**](DiagnosticLevel.md) |  | [optional]
**distributed_network** | [**DistributedNetworkOptions**](DistributedNetworkOptions.md) |  | [optional]
**connection** | [**ConnectionOptions**](ConnectionOptions.md) |  | [optional]

## Example

```python
from slskd.models.soulseek_options import SoulseekOptions

# TODO update the JSON string below
json = "{}"
# create an instance of SoulseekOptions from a JSON string
soulseek_options_instance = SoulseekOptions.from_json(json)
# print the JSON string representation of the object
print SoulseekOptions.to_json()

# convert the object into a dict
soulseek_options_dict = soulseek_options_instance.to_dict()
# create an instance of SoulseekOptions from a dict
soulseek_options_form_dict = soulseek_options.from_dict(soulseek_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
