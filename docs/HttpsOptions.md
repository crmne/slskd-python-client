# HttpsOptions

HTTPS options.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disabled** | **bool** | Gets a value indicating whether HTTPS should be disabled. | [optional]
**port** | **int** | Gets the HTTPS listen port. | [optional]
**force** | **bool** | Gets a value indicating whether HTTP requests should be redirected to HTTPS. | [optional]
**certificate** | [**CertificateOptions**](CertificateOptions.md) |  | [optional]

## Example

```python
from slskd.models.https_options import HttpsOptions

# TODO update the JSON string below
json = "{}"
# create an instance of HttpsOptions from a JSON string
https_options_instance = HttpsOptions.from_json(json)
# print the JSON string representation of the object
print HttpsOptions.to_json()

# convert the object into a dict
https_options_dict = https_options_instance.to_dict()
# create an instance of HttpsOptions from a dict
https_options_form_dict = https_options.from_dict(https_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
