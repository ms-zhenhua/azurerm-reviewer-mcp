flatten properties with `MaxItems: 1` that contain only a single nested property.

### good:
```go
"certificate": {
    Type:     pluginsdk.TypeList,
    Optional: true,
    Elem:     &pluginsdk.Schema{
        Type:         pluginsdk.TypeString,
        ValidateFunc: validation.StringIsNotEmpty,
    },
}
```

### bad:
```go
"credentials": {
    Type:     pluginsdk.TypeList,
    Optional: true,
    MaxItems: 1,
    Elem:     &pluginsdk.Resource{
        Schema: map[string]*pluginsdk.Schema{
            "certificate": {
                Type:     pluginsdk.TypeList,
                Optional: true,
                Elem:     &pluginsdk.Schema{
                    Type:         pluginsdk.TypeString,
                    ValidateFunc: validation.StringIsNotEmpty,
                },
            },
        },
    },
}
```
