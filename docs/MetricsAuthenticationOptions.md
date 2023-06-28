# MetricsAuthenticationOptions

Metrics endpoint authentication options.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disabled** | **bool** | Gets a value indicating whether authentication should be disabled. | [optional]
**username** | **str** | Gets the username for the metrics endpoint. | [optional]
**password** | **str** | Gets the password for the metrics endpoint. | [optional]

## Example

```python
from slskd.models.metrics_authentication_options import MetricsAuthenticationOptions

# TODO update the JSON string below
json = "{}"
# create an instance of MetricsAuthenticationOptions from a JSON string
metrics_authentication_options_instance = MetricsAuthenticationOptions.from_json(json)
# print the JSON string representation of the object
print MetricsAuthenticationOptions.to_json()

# convert the object into a dict
metrics_authentication_options_dict = metrics_authentication_options_instance.to_dict()
# create an instance of MetricsAuthenticationOptions from a dict
metrics_authentication_options_form_dict = metrics_authentication_options.from_dict(metrics_authentication_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
