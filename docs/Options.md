# Options

Application options.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**debug** | **bool** | Gets a value indicating whether the application should run in debug mode. | [optional]
**remote_configuration** | **bool** | Gets a value indicating whether remote configuration of options is allowed. | [optional]
**instance_name** | **str** | Gets the unique name for this instance. | [optional]
**flags** | [**FlagsOptions**](FlagsOptions.md) |  | [optional]
**relay** | [**RelayOptions**](RelayOptions.md) |  | [optional]
**directories** | [**DirectoriesOptions**](DirectoriesOptions.md) |  | [optional]
**shares** | [**SharesOptions**](SharesOptions.md) |  | [optional]
**var_global** | [**GlobalOptions**](GlobalOptions.md) |  | [optional]
**groups** | [**GroupsOptions**](GroupsOptions.md) |  | [optional]
**filters** | [**FiltersOptions**](FiltersOptions.md) |  | [optional]
**rooms** | **List[str]** | Gets a list of rooms to automatically join upon connection. | [optional]
**web** | [**WebOptions**](WebOptions.md) |  | [optional]
**logger** | [**LoggerOptions**](LoggerOptions.md) |  | [optional]
**metrics** | [**MetricsOptions**](MetricsOptions.md) |  | [optional]
**feature** | [**FeatureOptions**](FeatureOptions.md) |  | [optional]
**soulseek** | [**SoulseekOptions**](SoulseekOptions.md) |  | [optional]
**integration** | [**IntegrationOptions**](IntegrationOptions.md) |  | [optional]

## Example

```python
from slskd.models.options import Options

# TODO update the JSON string below
json = "{}"
# create an instance of Options from a JSON string
options_instance = Options.from_json(json)
# print the JSON string representation of the object
print Options.to_json()

# convert the object into a dict
options_dict = options_instance.to_dict()
# create an instance of Options from a dict
options_form_dict = options.from_dict(options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
