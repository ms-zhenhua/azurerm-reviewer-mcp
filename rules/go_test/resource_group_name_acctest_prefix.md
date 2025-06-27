Resource group names must start with `acctest` prefix to ensure proper cleanup during testing.

### good:
```hcl
resource "azurerm_resource_group" "test" {
  name     = "acctestRG-sapvis-%d"
  location = "%s"
}

resource "azurerm_workloads_sap_discovery_virtual_instance" "test" {
  # ...
  managed_resource_group_name = "acctestmanagedRG%d"
  # ...
}
```

### bad:
```hcl
resource "azurerm_resource_group" "test" {
  name     = "rg-sapvis-%d"
  location = "%s"
}

resource "azurerm_workloads_sap_discovery_virtual_instance" "test" {
  # ...
  managed_resource_group_name = "managedRG%d"
  # ...
}
```
