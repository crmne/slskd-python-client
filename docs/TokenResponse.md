# TokenResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expires** | **int** | Gets the time at which the Access Token expires. | [optional] [readonly]
**issued** | **int** | Gets the time at which the Access Token was issued. | [optional] [readonly]
**name** | **str** | Gets the value of the Name claim from the Access Token. | [optional] [readonly]
**not_before** | **int** | Gets the value of the Not Before claim from the Access Token. | [optional] [readonly]
**token** | **str** | Gets the Access Token string. | [optional] [readonly]
**token_type** | **str** | Gets the Token type. | [optional] [readonly]

## Example

```python
from slskd.models.token_response import TokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TokenResponse from a JSON string
token_response_instance = TokenResponse.from_json(json)
# print the JSON string representation of the object
print TokenResponse.to_json()

# convert the object into a dict
token_response_dict = token_response_instance.to_dict()
# create an instance of TokenResponse from a dict
token_response_form_dict = token_response.from_dict(token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
