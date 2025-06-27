Do not define a local variable if it's only used once in a function. Return the expression directly instead of storing it in an intermediate variable.

### good:
```go
func (r ManagerVerifierWorkspaceResource) complete(data acceptance.TestData) string {
	return fmt.Sprintf(`
%[1]s
provider "azurerm" {
  features {}
}
resource "azurerm_network_manager_verifier_workspace" "test" {
  ...
}
`, r.template(data), ...)
}
```

### bad:
```go
func (r ManagerVerifierWorkspaceResource) complete(data acceptance.TestData) string {
	template := r.template(data)
	return fmt.Sprintf(`
%[1]s
provider "azurerm" {
  features {}
}
resource "azurerm_network_manager_verifier_workspace" "test" {
  ...
}
`, template, ...)
}
```
