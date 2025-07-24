Always validate resource IDs using the appropriate parsing functions and return meaningful error messages when validation fails.

### good:
```go
func (r ResourceExample) ValidateFunc() pluginsdk.SchemaValidateFunc {
    return func(input interface{}, key string) (warnings []string, errors []error) {
        v, ok := input.(string)
        if !ok {
            errors = append(errors, fmt.Errorf("expected %q to be a string", key))
            return
        }

        if _, err := parse.ExampleID(v); err != nil {
            errors = append(errors, fmt.Errorf("parsing %q as Example ID: %+v", v, err))
        }

        return
    }
}
```

### bad:
```go
func (r ResourceExample) ValidateFunc() pluginsdk.SchemaValidateFunc {
    return validation.StringIsNotEmpty
}
```

### additional context:
Resource ID validation should use the specific parsing functions from the parse package to ensure the ID format is correct and provide clear error messages when validation fails.
