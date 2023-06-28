# DistributedNetworkOptions

Distributed network options.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disabled** | **bool** | Gets a value indicating whether the distributed network should be disabled. | [optional]
**disable_children** | **bool** | Gets a value indicating whether to accept distributed child connections. | [optional]
**child_limit** | **int** | Gets the distributed child connection limit. | [optional]
**logging** | **bool** | Gets a value indicating whether distributed network logging should be enabled. | [optional]

## Example

```python
from slskd.models.distributed_network_options import DistributedNetworkOptions

# TODO update the JSON string below
json = "{}"
# create an instance of DistributedNetworkOptions from a JSON string
distributed_network_options_instance = DistributedNetworkOptions.from_json(json)
# print the JSON string representation of the object
print DistributedNetworkOptions.to_json()

# convert the object into a dict
distributed_network_options_dict = distributed_network_options_instance.to_dict()
# create an instance of DistributedNetworkOptions from a dict
distributed_network_options_form_dict = distributed_network_options.from_dict(distributed_network_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
