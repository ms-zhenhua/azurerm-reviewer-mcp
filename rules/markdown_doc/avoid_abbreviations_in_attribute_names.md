Avoid using abbreviations in attribute names. Use full, descriptive words to ensure clarity and consistency across the provider.

### good:
```markdown
* `resource_group_name` - (Required) Specifies the resource group where the resource exists.
* `virtual_machine_id` - (Optional) Specifies the ID of the virtual machine.
* `storage_account_name` - (Required) Specifies the name of the storage account.
* `network_interface_id` - (Optional) Specifies the ID of the network interface.
```

### bad:
```markdown
* `rg_name` - (Required) Specifies the resource group where the resource exists.
* `vm_id` - (Optional) Specifies the ID of the virtual machine.
* `sa_name` - (Required) Specifies the name of the storage account.
* `nic_id` - (Optional) Specifies the ID of the network interface.
```
