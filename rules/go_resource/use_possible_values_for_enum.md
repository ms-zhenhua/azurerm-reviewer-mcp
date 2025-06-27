When defining enum attributes, use the `PossibleValuesFor` function instead of manually listing individual enum values. This ensures all possible values are included and maintains consistency with the SDK patterns.

### good:
```go
"example_field": {
    Type:         pluginsdk.TypeString,
    Required:     true,
    ValidateFunc: validation.StringInSlice(example.PossibleValuesForExampleFieldEnum(), false),
},
```

### bad:
```go
"example_field": {
    Type:     pluginsdk.TypeString,
    Optional: true,
    ValidateFunc: validation.StringInSlice([]string{
        string(example.ExampleFieldValue1),
        string(example.ExampleFieldValue2),
        // ...
    }, false),
},
```
