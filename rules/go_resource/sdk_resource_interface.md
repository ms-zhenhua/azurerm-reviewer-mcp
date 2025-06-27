`sdk.ResourceWithUpdate` must be defined with `Update()`; `sdk.ResourceWithCustomizeDiff` must be defined with `CustomizeDiff()`; `sdk.ResourceWithStateMigration` must be defined with `StateUpgraders()`; if `sdk.ResourceWith...` is defined, do not define `sdk.Resource` because `sdk.Resource` has already been defined in each `sdk.ResourceWith...`.

### good:
```go
var _ sdk.ResourceWithUpdate 		= ExampleResource{}
var _ sdk.ResourceWithCustomizeDiff = ExampleResource{}
var _ sdk.ResourceWithStateMigration = ExampleResource{}

...
func (k KeyResource) Update() sdk.ResourceFunc {
    // ... implementation ...
}

...
func (k KeyResource) CustomizeDiff() sdk.ResourceFunc {
    // ... implementation ...
}

...
func (k KeyResource) StateUpgraders() sdk.StateUpgradeData {
    // ... implementation ...
}
```

### bad:
```go
var _ sdk.Resource           		= ExampleResource{}
var _ sdk.ResourceWithUpdate 		= ExampleResource{}
var _ sdk.ResourceWithCustomizeDiff = ExampleResource{}
var _ sdk.ResourceWithStateMigration = ExampleResource{}

...
func (k KeyResource) Update() sdk.ResourceFunc {
    // ... implementation ...
}

...
func (k KeyResource) CustomizeDiff() sdk.ResourceFunc {
    // ... implementation ...
}

...
func (k KeyResource) StateUpgraders() sdk.StateUpgradeData {
    // ... implementation ...
}
```
