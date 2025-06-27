when `Create(ctx,...)` or `CreateOrUpdate(ctx,...)` fails in `Create()`, use the fixed format `fmt.Errorf("creating %s: %+v", id, err)`.

### good:
```go
func (r ResourceGroupExampleResource) Create() sdk.ResourceFunc {
    return sdk.ResourceFunc{
        ...
        Func: func(ctx context.Context, metadata sdk.ResourceMetaData) error {
            ...
            if _, err := client.CreateOrUpdate(ctx, id, param); err != nil {
                return fmt.Errorf("creating %s: %+v", id, err)
            }

            ...
        },
    }
}
```

### bad:
```go
func (r ResourceGroupExampleResource) Create() sdk.ResourceFunc {
    return sdk.ResourceFunc{
        ...
        Func: func(ctx context.Context, metadata sdk.ResourceMetaData) error {
            ...
            if _, err := client.CreateOrUpdate(ctx, id, param); err != nil {
                return fmt.Errorf("creating or updating %s: %+v", id, err)
            }

            ...
        },
    }
}
```
