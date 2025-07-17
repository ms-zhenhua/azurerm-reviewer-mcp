when `Delete(ctx,...)` fails in `Delete()`, use the fixed format `fmt.Errorf("deleting %s: %+v", *id, err)`.

### good:
```go
func (f ExampleResource) Delete() sdk.ResourceFunc {
	return sdk.ResourceFunc{
		...
		Func: func(ctx context.Context, metadata sdk.ResourceMetaData) error {
			...
			if err = client.DeleteThenPoll(ctx, *id); err != nil {
				return fmt.Errorf("deleting %s: %+v", *id, err)
			}
			...
		},
	}
}
```

### bad:
```go
func (f ExampleResource) Delete() sdk.ResourceFunc {
	return sdk.ResourceFunc{
		...
		Func: func(ctx context.Context, metadata sdk.ResourceMetaData) error {
			...
			if err = client.DeleteThenPoll(ctx, *id); err != nil {
				return fmt.Errorf("deleting %q: %+v", id.ID(), err)
			}
			...
		},
	}
}
```
