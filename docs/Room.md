# Room


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The room name. | [optional]
**is_private** | **bool** | A value indicating whether the room is private. | [optional]
**operator_count** | **int** | The number of operators in the room, if private. | [optional]
**operators** | **List[str]** | The operators in the room, if private. | [optional]
**owner** | **str** | The owner of the room, if private. | [optional]
**users** | [**List[UserData]**](UserData.md) | The list of users in the room. | [optional]
**messages** | [**List[RoomMessage]**](RoomMessage.md) | The list of messages. | [optional]

## Example

```python
from slskd.models.room import Room

# TODO update the JSON string below
json = "{}"
# create an instance of Room from a JSON string
room_instance = Room.from_json(json)
# print the JSON string representation of the object
print Room.to_json()

# convert the object into a dict
room_dict = room_instance.to_dict()
# create an instance of Room from a dict
room_form_dict = room.from_dict(room_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
