Boolean attributes should use the `_enabled` suffix for clarity and consistency.

### good:
```markdown
* `compression_enabled` - (Optional) Enables compression for the resource.
* `encryption_enabled` - (Required) Enables encryption.
* `monitoring_enabled` - (Optional) Enables monitoring for the service.
```

### bad:
```markdown
* `need_compression` - (Optional) Enables compression for the resource.
* `has_encryption` - (Required) Enables encryption.
* `monitoring` - (Optional) Enables monitoring for the service.
```
