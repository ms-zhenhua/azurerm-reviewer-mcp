Fields containing sensitive information like secrets, passwords, keys, connection strings, or certificates should be marked with `Sensitive: true` to prevent their values from being displayed in logs or CLI output.

### good:
```go
"client_secret": {
    Type:      pluginsdk.TypeString,
    Optional:  true,
    Sensitive: true,
},
```

### bad:
```go
"client_secret": {
    Type:      pluginsdk.TypeString,
    Optional:  true,
},
```
