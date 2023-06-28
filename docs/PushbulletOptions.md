# PushbulletOptions

Pushbullet options.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Gets a value indicating whether the Pushbullet integration is enabled. | [optional]
**access_token** | **str** | Gets the Pushbullet API access token. | [optional]
**notification_prefix** | **str** | Gets the prefix for Pushbullet notification titles. | [optional]
**notify_on_private_message** | **bool** | Gets a value indicating whether a Pushbullet notification should be sent when a private message is received. | [optional]
**notify_on_room_mention** | **bool** | Gets a value indicating whether a Pushbullet notification should be sent when the currently logged  in user&#39;s username is mentioned in a room. | [optional]
**retry_attempts** | **int** | Gets the number of times failing Pushbullet notifications will be retried. | [optional]
**cooldown_time** | **int** | Gets the cooldown time for Pushbullet notifications, in milliseconds. | [optional]

## Example

```python
from slskd.models.pushbullet_options import PushbulletOptions

# TODO update the JSON string below
json = "{}"
# create an instance of PushbulletOptions from a JSON string
pushbullet_options_instance = PushbulletOptions.from_json(json)
# print the JSON string representation of the object
print PushbulletOptions.to_json()

# convert the object into a dict
pushbullet_options_dict = pushbullet_options_instance.to_dict()
# create an instance of PushbulletOptions from a dict
pushbullet_options_form_dict = pushbullet_options.from_dict(pushbullet_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
