when a `pluginsdk.TypeList` property has multiple nested properties that are all optional, use `AtLeastOneOf` to ensure at least one property is specified.

### good:
```go
"setting": {
    Type:     pluginsdk.TypeList,
    Optional: true,
    MaxItems: 1,
    Elem: &pluginsdk.Resource{
        Schema: map[string]*pluginsdk.Schema{
            "linux": {
                Type:         pluginsdk.TypeList,
                Optional:     true,
                Elem:         osSchema(),
                AtLeastOneOf: []string{"setting.0.linux", "setting.0.windows"},
            },
            "windows": {
                Type:         pluginsdk.TypeList,
                Optional:     true,
                Elem:         osSchema(),
                AtLeastOneOf: []string{"setting.0.linux", "setting.0.windows"},
            },
        },
    },
}
```

### bad:
```go
"setting": {
    Type:     pluginsdk.TypeList,
    Optional: true,
    MaxItems: 1,
    Elem: &pluginsdk.Resource{
        Schema: map[string]*pluginsdk.Schema{
            "linux": {
                Type:     pluginsdk.TypeList,
                Optional: true,
                Elem:     osSchema(),
            },
            "windows": {
                Type:     pluginsdk.TypeList,
                Optional: true,
                Elem:     osSchema(),
            },
        },
    },
}
```
