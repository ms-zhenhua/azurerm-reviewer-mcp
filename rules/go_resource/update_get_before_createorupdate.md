If `Update()` function uses `CreateOrUpdate`, use `client.Get()` to retrieve existing resource state before calling `CreateOrUpdate` in update functions. Only modify properties that have changed using `HasChange()` checks.

### good:

```go
func (r ResourceExampleResource) Update() sdk.ResourceFunc {
    return sdk.ResourceFunc{
        Func: func(ctx context.Context, metadata sdk.ResourceMetaData) error {
            client := metadata.Client.Resource.GroupsClient
            
            existing, err := client.Get(ctx, *id)
            if err != nil {
                return fmt.Errorf("retrieving %s: %+v", id, err)
            }
            
            if metadata.ResourceData.HasChange("tags") {
                existing.Model.Properties.Tags = tags.Expand(config.Tags)
            }
            
            if _, err := client.CreateOrUpdate(ctx, *id, existing.Model); err != nil {
                return fmt.Errorf("updating %s: %+v", id, err)
            }
            
            return nil
        },
    }
}
```

### bad:

```go
func (r ResourceExampleResource) Update() sdk.ResourceFunc {
    return sdk.ResourceFunc{
        Func: func(ctx context.Context, metadata sdk.ResourceMetaData) error {
            // Error: Creates new model, overwrites existing properties
            param := resources.Group{
                Tags: pointer.To(config.Tags),
            }
            
            if _, err := client.CreateOrUpdate(ctx, *id, param); err != nil {
                return fmt.Errorf("updating %s: %+v", id, err)
            }
            
            return nil
        },
    }
}
