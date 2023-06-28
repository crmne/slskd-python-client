# ProxyOptions

Connection proxy options.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Gets a value indicating whether the proxy is enabled. | [optional]
**address** | **str** | Gets the proxy address. | [optional]
**port** | **int** | Gets the proxy port. | [optional]
**username** | **str** | Gets the proxy username, if applicable. | [optional]
**password** | **str** | Gets the proxy password, if applicable. | [optional]

## Example

```python
from slskd.models.proxy_options import ProxyOptions

# TODO update the JSON string below
json = "{}"
# create an instance of ProxyOptions from a JSON string
proxy_options_instance = ProxyOptions.from_json(json)
# print the JSON string representation of the object
print ProxyOptions.to_json()

# convert the object into a dict
proxy_options_dict = proxy_options_instance.to_dict()
# create an instance of ProxyOptions from a dict
proxy_options_form_dict = proxy_options.from_dict(proxy_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
