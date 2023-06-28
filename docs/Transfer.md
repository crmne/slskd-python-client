# Transfer

A single file transfer.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**average_speed** | **float** | Gets the current average transfer speed. | [optional]
**bytes_remaining** | **int** | Gets the number of remaining bytes to be transferred. | [optional]
**bytes_transferred** | **int** | Gets the total number of bytes transferred. | [optional]
**direction** | [**TransferDirection**](TransferDirection.md) |  | [optional]
**elapsed_time** | **float** | Gets the current duration of the transfer, if it has been started. | [optional]
**end_time** | **datetime** | Gets the UTC time at which the transfer transitioned into the Soulseek.TransferStates.Completed state. | [optional]
**filename** | **str** | Gets the filename of the file to be transferred. | [optional]
**id** | **str** | Gets the transfer id. | [optional] [readonly]
**ip_end_point** | [**IPEndPoint**](IPEndPoint.md) |  | [optional]
**percent_complete** | **float** | Gets the current progress in percent. | [optional]
**place_in_queue** | **int** | Gets the current place in queue, if it has been fetched. | [optional]
**remaining_time** | **float** | Gets the projected remaining duration of the transfer. | [optional]
**remote_token** | **int** | Gets the remote unique token for the transfer. | [optional]
**size** | **int** | Gets the size of the file to be transferred, in bytes. | [optional]
**start_offset** | **int** | Gets the starting offset of the transfer, in bytes. | [optional]
**start_time** | **datetime** | Gets the UTC time at which the transfer transitioned into the Soulseek.TransferStates.InProgress state. | [optional]
**state** | [**TransferStates**](TransferStates.md) |  | [optional]
**token** | **int** | Gets the unique token for the transfer. | [optional]
**username** | **str** | Gets the username of the peer to or from which the file is to be transferred. | [optional]
**exception** | **str** | Gets the Exception that caused the failure of the transfer, if applicable. | [optional]

## Example

```python
from slskd.models.transfer import Transfer

# TODO update the JSON string below
json = "{}"
# create an instance of Transfer from a JSON string
transfer_instance = Transfer.from_json(json)
# print the JSON string representation of the object
print Transfer.to_json()

# convert the object into a dict
transfer_dict = transfer_instance.to_dict()
# create an instance of Transfer from a dict
transfer_form_dict = transfer.from_dict(transfer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
