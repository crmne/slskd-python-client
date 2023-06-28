# BufferOptions

Connection buffer options.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**read** | **int** | Gets the connection read buffer size, in bytes. | [optional]
**write** | **int** | Gets the connection write buffer size, in bytes. | [optional]
**transfer** | **int** | Gets the read/write buffer size for transfers, in bytes. | [optional]
**write_queue** | **int** | Gets the size of the queue for double buffered writes. | [optional]

## Example

```python
from slskd.models.buffer_options import BufferOptions

# TODO update the JSON string below
json = "{}"
# create an instance of BufferOptions from a JSON string
buffer_options_instance = BufferOptions.from_json(json)
# print the JSON string representation of the object
print BufferOptions.to_json()

# convert the object into a dict
buffer_options_dict = buffer_options_instance.to_dict()
# create an instance of BufferOptions from a dict
buffer_options_form_dict = buffer_options.from_dict(buffer_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
