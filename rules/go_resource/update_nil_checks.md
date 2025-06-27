Perform nil checks for both `Model` and `Properties` in `Update` functions before accessing nested fields to prevent runtime panics.

### good:
```go
func (r DevCenterProjectEnvironmentTypeResource) Update() sdk.ResourceFunc {
	return sdk.ResourceFunc{
		Timeout: 30 * time.Minute,
		Func: func(ctx context.Context, metadata sdk.ResourceMetaData) error {
			// ...
			resp, err := client.Get(ctx, *id)
			// ...

			if resp.Model == nil {
				return fmt.Errorf("retrieving %s: `model` was nil", id)
			}
			if resp.Model.Properties == nil {
				return fmt.Errorf("retrieving %s: `properties` was nil", id)
			}

			updatedOn := resp.Model.Properties.UpdatedOn
			// ...
		}
	}
}
```

### bad:
```go
func (r DevCenterProjectEnvironmentTypeResource) Update() sdk.ResourceFunc {
	return sdk.ResourceFunc{
		Timeout: 30 * time.Minute,
		Func: func(ctx context.Context, metadata sdk.ResourceMetaData) error {
			// ...
			resp, err := client.Get(ctx, *id)
			// ...

			updatedOn := resp.Model.Properties.UpdatedOn
			// ...
		}
	}
}
```
