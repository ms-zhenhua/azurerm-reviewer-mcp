`Tags` fields must be defined as `map[string]string` for type safety. Avoid `map[string]interface{}`.

### good:
```go
Tags             map[string]string `tfschema:"tags"`
```

### bad:
```go
Tags             map[string]interface{} `tfschema:"tags"`
```
