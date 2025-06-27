Put `model` and `properties` in backticks when checking for `nil` values in error messages.

### good:
```go
if existing.Model == nil {
	return fmt.Errorf("retrieving %s: `model` was nil", id)
}
if existing.Model.Properties == nil {
	return fmt.Errorf("retrieving %s: `properties` was nil", id)
}
```

### bad:
```go
if existing.Model == nil {
	return fmt.Errorf("retrieving %s: model was nil", id)
}
if existing.Model.Properties == nil {
	return fmt.Errorf("retrieving %s: properties was nil", id)
}
```
