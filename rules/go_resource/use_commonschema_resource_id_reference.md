Use `commonschema.ResourceIDReference...` methods instead of explicitly defining `ValidateFunc` for resource ID field definitions. This provides consistent validation patterns and reduces code duplication.

### good:
```go
"application_load_balancer_id": commonschema.ResourceIDReferenceForceNew(associationsinterface.TrafficControllerId{}),
```

### bad:
```go
"application_load_balancer_id": {
    Type:         pluginsdk.TypeString,
    Required:     true,
    ForceNew:     true,
    ValidateFunc: associationsinterface.ValidateTrafficControllerID,
},
```
