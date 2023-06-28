# FeatureOptions

Feature options.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**swagger** | **bool** | Gets a value indicating whether swagger documentation and UI should be enabled. | [optional]

## Example

```python
from slskd.models.feature_options import FeatureOptions

# TODO update the JSON string below
json = "{}"
# create an instance of FeatureOptions from a JSON string
feature_options_instance = FeatureOptions.from_json(json)
# print the JSON string representation of the object
print FeatureOptions.to_json()

# convert the object into a dict
feature_options_dict = feature_options_instance.to_dict()
# create an instance of FeatureOptions from a dict
feature_options_form_dict = feature_options.from_dict(feature_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
