# JwtOptions

JWT options.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Gets the key with which to sign JWTs. | [optional]
**ttl** | **int** | Gets the TTL for JWTs, in milliseconds. | [optional]

## Example

```python
from slskd.models.jwt_options import JwtOptions

# TODO update the JSON string below
json = "{}"
# create an instance of JwtOptions from a JSON string
jwt_options_instance = JwtOptions.from_json(json)
# print the JSON string representation of the object
print JwtOptions.to_json()

# convert the object into a dict
jwt_options_dict = jwt_options_instance.to_dict()
# create an instance of JwtOptions from a dict
jwt_options_form_dict = jwt_options.from_dict(jwt_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
