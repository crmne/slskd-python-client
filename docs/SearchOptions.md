# SearchOptions

Search filter options.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | **List[str]** | Gets the list of search request filters. | [optional]

## Example

```python
from slskd.models.search_options import SearchOptions

# TODO update the JSON string below
json = "{}"
# create an instance of SearchOptions from a JSON string
search_options_instance = SearchOptions.from_json(json)
# print the JSON string representation of the object
print SearchOptions.to_json()

# convert the object into a dict
search_options_dict = search_options_instance.to_dict()
# create an instance of SearchOptions from a dict
search_options_form_dict = search_options.from_dict(search_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
