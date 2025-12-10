Avoid marking fields as both `Optional` and `Computed`. For new fields, use only `Optional` and rely on `ignore_changes` for default values. If `Optional + Computed` is required, add a comment starting with `// NOTE: O+C` explaining why.

### good:
```go
// Use only Optional, let users handle defaults with ignore_changes
"storage_type": {
    Type:     pluginsdk.TypeString,
    Optional: true,
    ValidateFunc: validation.StringInSlice([]string{
        "Standard",
        "Premium",
    }, false),
},

// If O+C is absolutely required, document why
"etag": {
    Type:     pluginsdk.TypeString,
    Optional: true,
    // NOTE: O+C Azure generates a new value every time this resource is updated
    Computed: true,
},
```

### bad:
```go
// Don't use Optional + Computed without explanation
"storage_type": {
    Type:     pluginsdk.TypeString,
    Optional: true,
    Computed: true, // This makes it hard for users to reset to default
    ValidateFunc: validation.StringInSlice([]string{
        "Standard",
        "Premium", 
    }, false),
},
```
