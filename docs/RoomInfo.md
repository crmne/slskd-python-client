# RoomInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional]
**user_count** | **int** |  | [optional]
**users** | **List[str]** |  | [optional] [readonly]

## Example

```python
from slskd.models.room_info import RoomInfo

# TODO update the JSON string below
json = "{}"
# create an instance of RoomInfo from a JSON string
room_info_instance = RoomInfo.from_json(json)
# print the JSON string representation of the object
print RoomInfo.to_json()

# convert the object into a dict
room_info_dict = room_info_instance.to_dict()
# create an instance of RoomInfo from a dict
room_info_form_dict = room_info.from_dict(room_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
