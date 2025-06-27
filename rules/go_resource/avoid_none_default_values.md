Don't expose default enum values of `None`, `Off`, or `Default` in Terraform schemas. Use Terraform's null type instead and handle conversion in Create/Read functions.

### good:
```go
// Schema - omit None/Default values
"shutdown_on_idle": {
    Type:     pluginsdk.TypeString,
    Optional: true,
    ValidateFunc: validation.StringInSlice([]string{
        string(labplan.ShutdownOnIdleModeUserAbsence),
    }, false),
},

// Create - convert null to None
shutdownOnIdle := string(labplan.ShutdownOnIdleModeNone)
if v := model.ShutdownOnIdle; v != "" {
    shutdownOnIdle = v
}
```

### bad:
```go
// Schema - exposing None/Default values
"shutdown_on_idle": {
    Type:     pluginsdk.TypeString,
    Optional: true,
    ValidateFunc: validation.StringInSlice([]string{
        string(labplan.ShutdownOnIdleModeNone), // Don't expose
        string(labplan.ShutdownOnIdleModeUserAbsence),
    }, false),
},
```
