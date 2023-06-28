# Conversation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | [optional]
**is_active** | **bool** |  | [optional]
**un_acknowledged_message_count** | **int** |  | [optional]
**has_un_acknowledged_messages** | **bool** |  | [optional] [readonly]
**messages** | [**List[PrivateMessage]**](PrivateMessage.md) |  | [optional]

## Example

```python
from slskd.models.conversation import Conversation

# TODO update the JSON string below
json = "{}"
# create an instance of Conversation from a JSON string
conversation_instance = Conversation.from_json(json)
# print the JSON string representation of the object
print Conversation.to_json()

# convert the object into a dict
conversation_dict = conversation_instance.to_dict()
# create an instance of Conversation from a dict
conversation_form_dict = conversation.from_dict(conversation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
