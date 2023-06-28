# Share

A file share.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional]
**alias** | **str** |  | [optional]
**is_excluded** | **bool** |  | [optional]
**local_path** | **str** |  | [optional]
**raw** | **str** |  | [optional]
**remote_path** | **str** |  | [optional]
**directories** | **int** |  | [optional]
**files** | **int** |  | [optional]

## Example

```python
from slskd.models.share import Share

# TODO update the JSON string below
json = "{}"
# create an instance of Share from a JSON string
share_instance = Share.from_json(json)
# print the JSON string representation of the object
print Share.to_json()

# convert the object into a dict
share_dict = share_instance.to_dict()
# create an instance of Share from a dict
share_form_dict = share.from_dict(share_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
