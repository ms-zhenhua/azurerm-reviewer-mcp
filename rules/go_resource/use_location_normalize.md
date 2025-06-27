`azure.NormalizeLocation` is deprecated, use `location.Normalize` instead.

### good:
```go
Location: location.Normalize(state.Location),
```

### bad:
```go
Location: azure.NormalizeLocation(state.Location),
```
