# WebOptions

Web server options.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**port** | **int** | Gets the HTTP listen port. | [optional]
**https** | [**HttpsOptions**](HttpsOptions.md) |  | [optional]
**url_base** | **str** | Gets the base url for web requests. | [optional]
**content_path** | **str** | Gets the path to static web content. | [optional]
**logging** | **bool** | Gets a value indicating whether HTTP request logging should be enabled. | [optional]
**authentication** | [**WebAuthenticationOptions**](WebAuthenticationOptions.md) |  | [optional]

## Example

```python
from slskd.models.web_options import WebOptions

# TODO update the JSON string below
json = "{}"
# create an instance of WebOptions from a JSON string
web_options_instance = WebOptions.from_json(json)
# print the JSON string representation of the object
print WebOptions.to_json()

# convert the object into a dict
web_options_dict = web_options_instance.to_dict()
# create an instance of WebOptions from a dict
web_options_form_dict = web_options.from_dict(web_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
