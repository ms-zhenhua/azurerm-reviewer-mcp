`location.Normalize` converts Azure location names to their canonical form. Use it to ensure consistent location formatting.

### good:
```go
Location: location.Normalize(model.Location),
```

### bad:
```go
Location: model.Location,
```
