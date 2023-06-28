# SharesOptions

Share options.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**directories** | **List[str]** | Gets the list of paths to shared files. | [optional]
**filters** | **List[str]** | Gets the list of shared file filters. | [optional]
**cache** | [**ShareCacheOptions**](ShareCacheOptions.md) |  | [optional]

## Example

```python
from slskd.models.shares_options import SharesOptions

# TODO update the JSON string below
json = "{}"
# create an instance of SharesOptions from a JSON string
shares_options_instance = SharesOptions.from_json(json)
# print the JSON string representation of the object
print SharesOptions.to_json()

# convert the object into a dict
shares_options_dict = shares_options_instance.to_dict()
# create an instance of SharesOptions from a dict
shares_options_form_dict = shares_options.from_dict(shares_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
