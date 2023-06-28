# UserData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**average_speed** | **int** |  | [optional]
**country_code** | **str** |  | [optional]
**directory_count** | **int** |  | [optional]
**file_count** | **int** |  | [optional]
**slots_free** | **int** |  | [optional]
**status** | [**UserPresence**](UserPresence.md) |  | [optional]
**upload_count** | **int** |  | [optional]
**username** | **str** |  | [optional]

## Example

```python
from slskd.models.user_data import UserData

# TODO update the JSON string below
json = "{}"
# create an instance of UserData from a JSON string
user_data_instance = UserData.from_json(json)
# print the JSON string representation of the object
print UserData.to_json()

# convert the object into a dict
user_data_dict = user_data_instance.to_dict()
# create an instance of UserData from a dict
user_data_form_dict = user_data.from_dict(user_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
