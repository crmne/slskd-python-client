# FlagsOptions

Optional flags.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**no_logo** | **bool** | Gets a value indicating whether the logo should be suppressed on startup. | [optional]
**no_start** | **bool** | Gets a value indicating whether the application should quit after initialization. | [optional]
**no_connect** | **bool** | Gets a value indicating whether the application should connect to the Soulseek network on startup. | [optional]
**no_share_scan** | **bool** | Gets a value indicating whether the application should scan shared directories on startup. | [optional]
**force_share_scan** | **bool** | Gets a value indicating whether shares should be forcibly re-scanned on startup. | [optional]
**no_version_check** | **bool** | Gets a value indicating whether the application should check for a newer version on startup. | [optional]
**log_sql** | **bool** | Gets a value indicating whether Entity Framework queries should be logged. | [optional]
**experimental** | **bool** | Gets a value indicating whether the application should run in experimental mode. | [optional]
**volatile** | **bool** | Gets a value indicating whether the application should run in volatile mode. | [optional]
**case_sensitive_reg_ex** | **bool** | Gets a value indicating whether user-defined regular expressions are case sensitive. | [optional]

## Example

```python
from slskd.models.flags_options import FlagsOptions

# TODO update the JSON string below
json = "{}"
# create an instance of FlagsOptions from a JSON string
flags_options_instance = FlagsOptions.from_json(json)
# print the JSON string representation of the object
print FlagsOptions.to_json()

# convert the object into a dict
flags_options_dict = flags_options_instance.to_dict()
# create an instance of FlagsOptions from a dict
flags_options_form_dict = flags_options.from_dict(flags_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
