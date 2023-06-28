# ShareCacheOptions

Share caching options.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**storage_mode** | **str** | Gets the type of storage to use for the share cache. | [optional]
**workers** | **int** | Gets the number of workers to use while scanning shares. | [optional]

## Example

```python
from slskd.models.share_cache_options import ShareCacheOptions

# TODO update the JSON string below
json = "{}"
# create an instance of ShareCacheOptions from a JSON string
share_cache_options_instance = ShareCacheOptions.from_json(json)
# print the JSON string representation of the object
print ShareCacheOptions.to_json()

# convert the object into a dict
share_cache_options_dict = share_cache_options_instance.to_dict()
# create an instance of ShareCacheOptions from a dict
share_cache_options_form_dict = share_cache_options.from_dict(share_cache_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
