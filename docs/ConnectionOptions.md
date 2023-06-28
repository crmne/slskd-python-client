# ConnectionOptions

Connection options.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timeout** | [**TimeoutOptions**](TimeoutOptions.md) |  | [optional]
**buffer** | [**BufferOptions**](BufferOptions.md) |  | [optional]
**proxy** | [**ProxyOptions**](ProxyOptions.md) |  | [optional]

## Example

```python
from slskd.models.connection_options import ConnectionOptions

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionOptions from a JSON string
connection_options_instance = ConnectionOptions.from_json(json)
# print the JSON string representation of the object
print ConnectionOptions.to_json()

# convert the object into a dict
connection_options_dict = connection_options_instance.to_dict()
# create an instance of ConnectionOptions from a dict
connection_options_form_dict = connection_options.from_dict(connection_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
