# ThresholdOptions

Leecher threshold options.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files** | **int** | Gets the minimum number of shared files required to avoid being classified as a leecher. | [optional]
**directories** | **int** | Gets the minimum number of shared directories required to avoid being classified as a leecher. | [optional]

## Example

```python
from slskd.models.threshold_options import ThresholdOptions

# TODO update the JSON string below
json = "{}"
# create an instance of ThresholdOptions from a JSON string
threshold_options_instance = ThresholdOptions.from_json(json)
# print the JSON string representation of the object
print ThresholdOptions.to_json()

# convert the object into a dict
threshold_options_dict = threshold_options_instance.to_dict()
# create an instance of ThresholdOptions from a dict
threshold_options_form_dict = threshold_options.from_dict(threshold_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
