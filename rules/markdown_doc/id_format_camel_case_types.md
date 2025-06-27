Use lowerCamelCase format for resource type segments and lowercase format for name segments in Azure resource IDs.

### good:
```terraform
terraform import azurerm_dev_center_environment_type.example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.DevCenter/devCenters/dc1/environmentTypes/et1
```

### bad:
```terraform
terraform import azurerm_dev_center_environment_type.example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.DevCenter/devcenters/dc1/environmentTypes/et1
```
