# GroupsOptions

User groups.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | [**BuiltInOptions**](BuiltInOptions.md) |  | [optional]
**leechers** | [**LeecherOptions**](LeecherOptions.md) |  | [optional]
**blacklisted** | [**BlacklistedOptions**](BlacklistedOptions.md) |  | [optional]
**user_defined** | [**Dict[str, UserDefinedOptions]**](UserDefinedOptions.md) | Gets user defined groups and options. | [optional]

## Example

```python
from slskd.models.groups_options import GroupsOptions

# TODO update the JSON string below
json = "{}"
# create an instance of GroupsOptions from a JSON string
groups_options_instance = GroupsOptions.from_json(json)
# print the JSON string representation of the object
print GroupsOptions.to_json()

# convert the object into a dict
groups_options_dict = groups_options_instance.to_dict()
# create an instance of GroupsOptions from a dict
groups_options_form_dict = groups_options.from_dict(groups_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
