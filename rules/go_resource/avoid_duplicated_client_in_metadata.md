Avoid duplicated `Client` when accessing service clients from metadata. Use the direct service client path instead of including an extra `Client` component.

### good:
```go
func(ctx context.Context, metadata sdk.ResourceMetaData) error {
    client := metadata.Client.ElasticSan.ElasticSans
}
```

### bad:
```go
func(ctx context.Context, metadata sdk.ResourceMetaData) error {
    client := metadata.Client.ElasticSan.Client.ElasticSans
}
```
