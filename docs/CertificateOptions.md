# CertificateOptions

Certificate options.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pfx** | **str** | Gets the path to the the X509 certificate .pfx file. | [optional]
**password** | **str** | Gets the password for the X509 certificate. | [optional]

## Example

```python
from slskd.models.certificate_options import CertificateOptions

# TODO update the JSON string below
json = "{}"
# create an instance of CertificateOptions from a JSON string
certificate_options_instance = CertificateOptions.from_json(json)
# print the JSON string representation of the object
print CertificateOptions.to_json()

# convert the object into a dict
certificate_options_dict = certificate_options_instance.to_dict()
# create an instance of CertificateOptions from a dict
certificate_options_form_dict = certificate_options.from_dict(certificate_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
