# RelayControllerConfigurationOptions

Relay controller configuration options.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Gets the controller address. | [optional]
**ignore_certificate_errors** | **bool** | Gets a value indicating whether controller certificate errors should be ignored. | [optional]
**api_key** | **str** | Gets the controller API key. | [optional]
**secret** | **str** | Gets the controller secret. | [optional]
**downloads** | **bool** | Gets a value indicating whether to receive completed downloads from the controller. | [optional]

## Example

```python
from slskd.models.relay_controller_configuration_options import RelayControllerConfigurationOptions

# TODO update the JSON string below
json = "{}"
# create an instance of RelayControllerConfigurationOptions from a JSON string
relay_controller_configuration_options_instance = RelayControllerConfigurationOptions.from_json(json)
# print the JSON string representation of the object
print RelayControllerConfigurationOptions.to_json()

# convert the object into a dict
relay_controller_configuration_options_dict = relay_controller_configuration_options_instance.to_dict()
# create an instance of RelayControllerConfigurationOptions from a dict
relay_controller_configuration_options_form_dict = relay_controller_configuration_options.from_dict(relay_controller_configuration_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
