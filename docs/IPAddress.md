# IPAddress


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_family** | [**AddressFamily**](AddressFamily.md) |  | [optional]
**scope_id** | **int** |  | [optional]
**is_ipv6_multicast** | **bool** |  | [optional] [readonly]
**is_ipv6_link_local** | **bool** |  | [optional] [readonly]
**is_ipv6_site_local** | **bool** |  | [optional] [readonly]
**is_ipv6_teredo** | **bool** |  | [optional] [readonly]
**is_ipv6_unique_local** | **bool** |  | [optional] [readonly]
**is_ipv4_mapped_to_ipv6** | **bool** |  | [optional] [readonly]
**address** | **int** |  | [optional]

## Example

```python
from slskd.models.ip_address import IPAddress

# TODO update the JSON string below
json = "{}"
# create an instance of IPAddress from a JSON string
ip_address_instance = IPAddress.from_json(json)
# print the JSON string representation of the object
print IPAddress.to_json()

# convert the object into a dict
ip_address_dict = ip_address_instance.to_dict()
# create an instance of IPAddress from a dict
ip_address_form_dict = ip_address.from_dict(ip_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
