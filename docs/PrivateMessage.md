# PrivateMessage

A private message.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **datetime** | The UTC timestamp of the message. | [optional]
**id** | **int** | The unique message id, used to acknowledge receipt. | [optional]
**username** | **str** | The username of the remote user. | [optional]
**direction** | [**MessageDirection**](MessageDirection.md) |  | [optional]
**message** | **str** | The message. | [optional]
**is_acknowledged** | **bool** | A value indicating whether the message has been acknowledged. | [optional]

## Example

```python
from slskd.models.private_message import PrivateMessage

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateMessage from a JSON string
private_message_instance = PrivateMessage.from_json(json)
# print the JSON string representation of the object
print PrivateMessage.to_json()

# convert the object into a dict
private_message_dict = private_message_instance.to_dict()
# create an instance of PrivateMessage from a dict
private_message_form_dict = private_message.from_dict(private_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
