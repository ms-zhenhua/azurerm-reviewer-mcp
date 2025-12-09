Do not use `ignore_changes` for properties in Terraform test configurations. Define them as `Optional`+`Computed` in the schema instead.

### good:
```go
resource "example_resource" "example" {
  name                    = "acctestappinsightswebtests-%d"
  location                = azurerm_resource_group.test.location
  resource_group_name     = azurerm_resource_group.test.name
  ...
}
```

### bad:
```go
resource "example_resource" "example" {
  name                    = "acctestappinsightswebtests-%d"
  location                = azurerm_resource_group.test.location
  resource_group_name     = azurerm_resource_group.test.name
  ...

  lifecycle {
    ignore_changes = ["etag"]
  }
}
```
