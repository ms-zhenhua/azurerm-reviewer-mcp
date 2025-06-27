Initialize slices with `make()` in `flatten` functions instead of declaring `nil` slices. Setting `nil` into the state for Lists/Sets means that users can't interpolate these values.

### good:
```go
func flattenFilteringTagModelArray(input *[]tagrules.FilteringTag) []FilteringTagModel {
    output := make([]FilteringTagModel, 0)
    // ... rest of the function
}
```

### bad:
```go
func flattenFilteringTagModelArray(input *[]tagrules.FilteringTag) []FilteringTagModel {
    var outputList []FilteringTagModel
    // ... rest of the function
}
```
