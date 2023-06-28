# IPEndPoint


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_family** | [**AddressFamily**](AddressFamily.md) |  | [optional]
**address** | [**IPAddress**](IPAddress.md) |  | [optional]
**port** | **int** |  | [optional]

## Example

```python
from slskd.models.ip_end_point import IPEndPoint

# TODO update the JSON string below
json = "{}"
# create an instance of IPEndPoint from a JSON string
ip_end_point_instance = IPEndPoint.from_json(json)
# print the JSON string representation of the object
print IPEndPoint.to_json()

# convert the object into a dict
ip_end_point_dict = ip_end_point_instance.to_dict()
# create an instance of IPEndPoint from a dict
ip_end_point_form_dict = ip_end_point.from_dict(ip_end_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
