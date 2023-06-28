# RoomMessage

A message sent to a room.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **datetime** | The timestamp of the message. | [optional]
**username** | **str** | The username of the user who sent the message. | [optional]
**message** | **str** | The message. | [optional]
**room_name** | **str** | The room to which the message pertains. | [optional]
**direction** | [**MessageDirection**](MessageDirection.md) |  | [optional]

## Example

```python
from slskd.models.room_message import RoomMessage

# TODO update the JSON string below
json = "{}"
# create an instance of RoomMessage from a JSON string
room_message_instance = RoomMessage.from_json(json)
# print the JSON string representation of the object
print RoomMessage.to_json()

# convert the object into a dict
room_message_dict = room_message_instance.to_dict()
# create an instance of RoomMessage from a dict
room_message_form_dict = room_message.from_dict(room_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
