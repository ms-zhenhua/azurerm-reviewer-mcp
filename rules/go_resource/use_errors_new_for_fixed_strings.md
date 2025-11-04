use `errors.New()` for error messages that are fixed strings without variable interpolation. Use `fmt.Errorf()` only when the error message contains dynamic values that need to be interpolated.

### good:
```go
func (r ResourceGroupExampleResource) Create() sdk.ResourceFunc {
    return sdk.ResourceFunc{
        ...
        Func: func(ctx context.Context, metadata sdk.ResourceMetaData) error {
            ...
            // good: use fmt.Errorf when interpolating variables into the error message
            return fmt.Errorf("the `network_acls.bypass` does not support Trusted Services when `kind` is set to `%s`", kind)

            // good: use errors.New for static error messages without any variables
            return errors.New("`project_management_enabled` can only be enabled when kind is set to `AIServices`")

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
            // bad: using fmt.Errorf for a static string wastes formatting capability
            return fmt.Errorf("`project_management_enabled` can only be enabled when kind is set to `AIServices`")
            ...
        },
    }
}
```
