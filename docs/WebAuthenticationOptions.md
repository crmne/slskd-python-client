# WebAuthenticationOptions

Authentication options.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disabled** | **bool** | Gets a value indicating whether authentication should be disabled. | [optional]
**username** | **str** | Gets the username for the web UI. | [optional]
**password** | **str** | Gets the password for the web UI. | [optional]
**jwt** | [**JwtOptions**](JwtOptions.md) |  | [optional]
**api_keys** | [**Dict[str, ApiKeyOptions]**](ApiKeyOptions.md) | Gets API keys. | [optional]

## Example

```python
from slskd.models.web_authentication_options import WebAuthenticationOptions

# TODO update the JSON string below
json = "{}"
# create an instance of WebAuthenticationOptions from a JSON string
web_authentication_options_instance = WebAuthenticationOptions.from_json(json)
# print the JSON string representation of the object
print WebAuthenticationOptions.to_json()

# convert the object into a dict
web_authentication_options_dict = web_authentication_options_instance.to_dict()
# create an instance of WebAuthenticationOptions from a dict
web_authentication_options_form_dict = web_authentication_options.from_dict(web_authentication_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
