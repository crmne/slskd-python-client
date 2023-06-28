# FiltersOptions

Filter options.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search** | [**SearchOptions**](SearchOptions.md) |  | [optional]

## Example

```python
from slskd.models.filters_options import FiltersOptions

# TODO update the JSON string below
json = "{}"
# create an instance of FiltersOptions from a JSON string
filters_options_instance = FiltersOptions.from_json(json)
# print the JSON string representation of the object
print FiltersOptions.to_json()

# convert the object into a dict
filters_options_dict = filters_options_instance.to_dict()
# create an instance of FiltersOptions from a dict
filters_options_form_dict = filters_options.from_dict(filters_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
