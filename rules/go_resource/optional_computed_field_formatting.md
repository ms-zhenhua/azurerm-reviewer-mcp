when a field must be both `Optional` and `Computed`, follow these conventions:

1. Properties are in this sequence: `Optional`, Explanatory Comment, `Computed`
2. The comment should start with `// NOTE: O+C` and then explain the reason for the field being Optional and Computed

### good:
```go
"etag": {
    Type: pluginsdk.TypeString,
    Optional: true,
    // NOTE: O+C Azure generates a new value every time this resource is updated
    Computed: true,
},
```

### bad:
```go
"etag": {
    Type: pluginsdk.TypeString,
    Optional: true,
    // `Computed: O+C Azure generates a new value every time this resource is updated
    Computed: true,
},
```
