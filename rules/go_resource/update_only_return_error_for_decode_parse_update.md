in `Update()` function, only return error for decode, parse or update operations, use `ForceNew` in `CustomizeDiff()` for validation errors.

### good:
```go
func (r ResourceGroupExampleResource) Update() sdk.ResourceFunc {
    return sdk.ResourceFunc{
        ...
        Func: func(ctx context.Context, metadata sdk.ResourceMetaData) error {

            id, err := resources.ParseResourceGroupID(metadata.ResourceData.Id())
            if err != nil {
                return err
            }

            ...
            if err := metadata.Decode(&config); err != nil {
                return fmt.Errorf("decoding: %+v", err)
            }

            ...
            if _, err := client.CreateOrUpdate(ctx, *id, param); err != nil {
                return fmt.Errorf("updating %s: %+v", id, err)
            }

            ...
            return nil
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
            if d.HasChange("property_a") && len(d.Get("property_a").([]interface{})) == 0 {
                return errors.New("...")
            }

            ...
            if d.HasChange("property_b") && len(d.Get("property_b").([]interface{})) == 0 {
                return fmt.Errorf("...")
            }

            ...
            return nil
        },
    }
}
```
