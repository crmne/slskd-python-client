# ServerState


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | [optional]
**ip_end_point** | [**IPEndPoint**](IPEndPoint.md) |  | [optional]
**state** | [**SoulseekClientStates**](SoulseekClientStates.md) |  | [optional]
**username** | **str** |  | [optional]
**is_connected** | **bool** |  | [optional] [readonly]
**is_logged_in** | **bool** |  | [optional] [readonly]
**is_transitioning** | **bool** |  | [optional] [readonly]

## Example

```python
from slskd.models.server_state import ServerState

# TODO update the JSON string below
json = "{}"
# create an instance of ServerState from a JSON string
server_state_instance = ServerState.from_json(json)
# print the JSON string representation of the object
print ServerState.to_json()

# convert the object into a dict
server_state_dict = server_state_instance.to_dict()
# create an instance of ServerState from a dict
server_state_form_dict = server_state.from_dict(server_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
