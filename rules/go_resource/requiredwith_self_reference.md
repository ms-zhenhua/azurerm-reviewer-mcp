Avoid including a field in its own `RequiredWith` list as it's redundant.

### good:
```go
"administrator_username": {
    Type:         schema.TypeString,
    Optional:     true,
    RequiredWith: []string{"administrator_password"},
},
```

### bad:
```go
"administrator_username": {
    Type:         schema.TypeString,
    Optional:     true,
    RequiredWith: []string{"administrator_username", "administrator_password"},
},
```
