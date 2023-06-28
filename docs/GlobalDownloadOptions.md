# GlobalDownloadOptions

Gets global download options.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slots** | **int** | Gets the limit for the total number of download slots. | [optional]
**speed_limit** | **int** | Gets the total download speed limit. | [optional]

## Example

```python
from slskd.models.global_download_options import GlobalDownloadOptions

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalDownloadOptions from a JSON string
global_download_options_instance = GlobalDownloadOptions.from_json(json)
# print the JSON string representation of the object
print GlobalDownloadOptions.to_json()

# convert the object into a dict
global_download_options_dict = global_download_options_instance.to_dict()
# create an instance of GlobalDownloadOptions from a dict
global_download_options_form_dict = global_download_options.from_dict(global_download_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
