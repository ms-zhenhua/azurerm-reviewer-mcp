Use separate Create and Update methods instead of combined CreateOrUpdate. Update methods should use `d.HasChanges()` to only update changed fields and support Terraform's `ignore_changes` feature.

### good:
```go
func (r ExampleResource) Create() sdk.ResourceFunc {
    return sdk.ResourceFunc{
        Func: func(ctx context.Context, metadata sdk.ResourceMetaData) error {
            payload := resources.Group{
                Location: location.Normalize(d.Get("location").(string)),
                Tags: tags.Expand(d.Get("tags").(map[string]interface{})),
            }
            if err := client.CreateThenPoll(ctx, id, payload); err != nil {
                return fmt.Errorf("creating %s: %+v", id, err)
            }
            return nil
        },
    }
}

func (r ExampleResource) Update() sdk.ResourceFunc {
    return sdk.ResourceFunc{
        Func: func(ctx context.Context, metadata sdk.ResourceMetaData) error {
            if d.HasChanges("tags") {
                payload := resources.GroupUpdate{}
                payload.Tags = pointer.To(tags.Expand(d.Get("tags").(map[string]interface{})))
                if err := client.UpdateThenPoll(ctx, id, payload); err != nil {
                    return fmt.Errorf("updating %s: %+v", id, err)
                }
            }
            return nil
        },
    }
}
```

### bad:
```go
func resourceExampleCreateUpdate(d *pluginsdk.ResourceData, meta interface{}) error {
    // Combined create/update method doesn't support ignore_changes properly
    payload := resources.Group{
        Location: location.Normalize(d.Get("location").(string)),
        Tags: tags.Expand(d.Get("tags").(map[string]interface{})),
    }
    if err := client.CreateOrUpdateThenPoll(ctx, id, payload); err != nil {
        return fmt.Errorf("creating/updating %s: %+v", id, err)
    }
    return nil
}
```
