# IntegrationOptions

Options for external integrations.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ftp** | [**FtpOptions**](FtpOptions.md) |  | [optional]
**pushbullet** | [**PushbulletOptions**](PushbulletOptions.md) |  | [optional]

## Example

```python
from slskd.models.integration_options import IntegrationOptions

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationOptions from a JSON string
integration_options_instance = IntegrationOptions.from_json(json)
# print the JSON string representation of the object
print IntegrationOptions.to_json()

# convert the object into a dict
integration_options_dict = integration_options_instance.to_dict()
# create an instance of IntegrationOptions from a dict
integration_options_form_dict = integration_options.from_dict(integration_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
