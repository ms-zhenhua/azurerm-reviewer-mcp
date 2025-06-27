Use resource-specific ID validation functions instead of generic string validation for `xxx_id` fields. This ensures the ID format matches the expected Azure resource ID pattern and provides better error messages.

### good:
```go
"source_server_id": {
    Type:         schema.TypeString,
    Optional:     true,
    ForceNew:     true,
    ValidateFunc: mongoclusters.ValidateMongoClusterID,
},
```

### bad:
```go
"source_server_id": {
    Type:         schema.TypeString,
    Optional:     true,
    ForceNew:     true,
    ValidateFunc: validation.StringIsNotEmpty,
},
```
