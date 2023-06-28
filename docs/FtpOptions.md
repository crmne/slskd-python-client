# FtpOptions

FTP options.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Gets a value indicating whether the FTP integration is enabled. | [optional]
**address** | **str** | Gets the FTP address. | [optional]
**port** | **int** | Gets the FTP port. | [optional]
**encryption_mode** | **str** | Gets the FTP encryption mode. | [optional]
**ignore_certificate_errors** | **bool** | Gets a value indicating whether FTP certificate errors should be ignored. | [optional]
**username** | **str** | Gets the FTP username. | [optional]
**password** | **str** | Gets the FTP password. | [optional]
**remote_path** | **str** | Gets the remote path for uploads. | [optional]
**overwrite_existing** | **bool** | Gets a value indicating whether existing files should be overwritten. | [optional]
**connection_timeout** | **int** | Gets the connection timeout value, in milliseconds. | [optional]
**retry_attempts** | **int** | Gets the number of times failing uploads will be retried. | [optional]

## Example

```python
from slskd.models.ftp_options import FtpOptions

# TODO update the JSON string below
json = "{}"
# create an instance of FtpOptions from a JSON string
ftp_options_instance = FtpOptions.from_json(json)
# print the JSON string representation of the object
print FtpOptions.to_json()

# convert the object into a dict
ftp_options_dict = ftp_options_instance.to_dict()
# create an instance of FtpOptions from a dict
ftp_options_form_dict = ftp_options.from_dict(ftp_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
