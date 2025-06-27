when `Update(ctx,...)` or `CreateOrUpdate(ctx,...)` fails in `Update()`, use the fixed format `fmt.Errorf("updating %s: %+v", id, err)`.

### good:
```go
func (r ResourceGroupExampleResource) Update() sdk.ResourceFunc {
    return sdk.ResourceFunc{
        ...
        Func: func(ctx context.Context, metadata sdk.ResourceMetaData) error {
            ...

            if _, err := client.CreateOrUpdate(ctx, *id, param); err != nil {
                return fmt.Errorf("updating %s: %+v", id, err)
            }

            ...
        },
    }
}
```

### bad:
```go
func (r ResourceGroupExampleResource) Update() sdk.ResourceFunc {
    return sdk.ResourceFunc{
        ...
        Func: func(ctx context.Context, metadata sdk.ResourceMetaData) error {
            ...

            if _, err := client.CreateOrUpdate(ctx, *id, param); err != nil {
                return fmt.Errorf("creating or updating %s: %+v", id, err)
            }

            ...
        },
    }
}
```
