# LeecherOptions

Built in leecher group options.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**thresholds** | [**ThresholdOptions**](ThresholdOptions.md) |  | [optional]
**upload** | [**UploadOptions**](UploadOptions.md) |  | [optional]

## Example

```python
from slskd.models.leecher_options import LeecherOptions

# TODO update the JSON string below
json = "{}"
# create an instance of LeecherOptions from a JSON string
leecher_options_instance = LeecherOptions.from_json(json)
# print the JSON string representation of the object
print LeecherOptions.to_json()

# convert the object into a dict
leecher_options_dict = leecher_options_instance.to_dict()
# create an instance of LeecherOptions from a dict
leecher_options_form_dict = leecher_options.from_dict(leecher_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
