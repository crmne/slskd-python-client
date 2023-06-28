# ApiKeyOptions

API key options.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Gets the API key value. | [optional]
**role** | **str** | Gets the role for the key. | [optional]
**cidr** | **str** | Gets the comma separated list of CIDRs that are authorized to use the key. | [optional]

## Example

```python
from slskd.models.api_key_options import ApiKeyOptions

# TODO update the JSON string below
json = "{}"
# create an instance of ApiKeyOptions from a JSON string
api_key_options_instance = ApiKeyOptions.from_json(json)
# print the JSON string representation of the object
print ApiKeyOptions.to_json()

# convert the object into a dict
api_key_options_dict = api_key_options_instance.to_dict()
# create an instance of ApiKeyOptions from a dict
api_key_options_form_dict = api_key_options.from_dict(api_key_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
