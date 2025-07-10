Avoid explicit `Key().Exists()` checks in acceptance tests unless the checked field is set `Computed: true`.

### good:
```go
func TestAccExample_complete(t *testing.T) {
	data := acceptance.BuildTestData(t, "azurerm_example", "test")
	r := ExampleTestResource{}

	data.ResourceTest(t, r, []acceptance.TestStep{
		{
			Config: r.complete(data),
			Check: acceptance.ComposeTestCheckFunc(
				check.That(data.ResourceName).ExistsInAzure(r),
			),
		},
		...
	})
}
```

### bad:
```go
func TestAccExample_complete(t *testing.T) {
	data := acceptance.BuildTestData(t, "azurerm_example", "test")
	r := ExampleTestResource{}

	data.ResourceTest(t, r, []acceptance.TestStep{
		{
			Config: r.complete(data),
			Check: acceptance.ComposeTestCheckFunc(
				check.That(data.ResourceName).ExistsInAzure(r),
				check.That(data.ResourceName).Key("total_iops").Exists(),
			),
		},
		...
	})
}
```
