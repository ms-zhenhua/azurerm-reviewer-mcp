Examples must be functional and complete. Normally, they should start with an `azurerm_resource_group` resource to ensure the example can be successfully applied by users. This provides all necessary dependencies and follows best practices for Terraform resource definitions.

## good

```hcl
resource "azurerm_resource_group" "example" {
  name     = "example-resources"
  location = "eastus"
}

resource "azurerm_virtual_network" "example" {
  name                = "example-vnet"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
  address_space       = ["10.0.0.0/16"]
}
```

## bad

```hcl
resource "azurerm_virtual_network" "example" {
  name                = "example-vnet"
  location            = "eastus"
  resource_group_name = "example-resources"
  address_space       = ["10.0.0.0/16"]
}
```

