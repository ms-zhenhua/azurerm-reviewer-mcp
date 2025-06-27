Do not explicitly set `model.SystemData = nil` when working with `model`.

### good:
```go
func(ctx context.Context, metadata sdk.ResourceMetaData) error {
	...
	existing, err := client.Get(ctx, *id)
	...
	model := existing.Model
	...
}
```

### bad:
```go
func(ctx context.Context, metadata sdk.ResourceMetaData) error {
	...
	existing, err := client.Get(ctx, *id)
	...
	model := existing.Model
	...
	model.SystemData = nil
}
```
