# LoggerOptions

Logger options.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**loki** | **str** | Gets the URL to a Grafana Loki instance to which to log. | [optional]

## Example

```python
from slskd.models.logger_options import LoggerOptions

# TODO update the JSON string below
json = "{}"
# create an instance of LoggerOptions from a JSON string
logger_options_instance = LoggerOptions.from_json(json)
# print the JSON string representation of the object
print LoggerOptions.to_json()

# convert the object into a dict
logger_options_dict = logger_options_instance.to_dict()
# create an instance of LoggerOptions from a dict
logger_options_form_dict = logger_options.from_dict(logger_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
