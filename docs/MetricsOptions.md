# MetricsOptions

Metrics options.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Gets a value indicating whether the metrics endpoint should be enabled. | [optional]
**url** | **str** | Gets the url for the metrics endpoint. | [optional]
**authentication** | [**MetricsAuthenticationOptions**](MetricsAuthenticationOptions.md) |  | [optional]

## Example

```python
from slskd.models.metrics_options import MetricsOptions

# TODO update the JSON string below
json = "{}"
# create an instance of MetricsOptions from a JSON string
metrics_options_instance = MetricsOptions.from_json(json)
# print the JSON string representation of the object
print MetricsOptions.to_json()

# convert the object into a dict
metrics_options_dict = metrics_options_instance.to_dict()
# create an instance of MetricsOptions from a dict
metrics_options_form_dict = metrics_options.from_dict(metrics_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
