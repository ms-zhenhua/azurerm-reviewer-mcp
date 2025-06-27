Schema fields should be ordered consistently to improve code readability and maintainability. Follow the specific ordering rules for resource schema definitions.

**Ordering Rules:**
1. Any fields that make up the resource's ID, with the last user specified segment (usually the resource's name) first. (e.g. `name` then `resource_group_name`, or `name` then `parent_resource_id`)
2. The `location` field.
3. Required fields, sorted alphabetically.
4. Optional fields, sorted alphabetically.
5. Computed fields, sorted alphabetically.

### good:
```go
return map[string]*pluginsdk.Schema{
    "name": {
        Type:         pluginsdk.TypeString,
        Required:     true,
        ValidateFunc: validation.StringIsNotEmpty,
    },

    "resource_group_name": commonschema.ResourceGroupName(),

    "location": commonschema.Location(),

    "description": {
        Type:     pluginsdk.TypeString,
        Required: true,
    },

    "enabled": {
        Type:     pluginsdk.TypeBool,
        Optional: true,
        Default:  true,
    },

    "tags": tags.Schema(),

    "fqdn": {
        Type:     pluginsdk.TypeString,
        Computed: true,
    },
}
```

### bad:
```go
return map[string]*pluginsdk.Schema{
    "location": commonschema.Location(),

    "tags": tags.Schema(),

    "name": {
        Type:         pluginsdk.TypeString,
        Required:     true,
        ValidateFunc: validation.StringIsNotEmpty,
    },

    "enabled": {
        Type:     pluginsdk.TypeBool,
        Optional: true,
        Default:  true,
    },

    "resource_group_name": commonschema.ResourceGroupName(),

    "description": {
        Type:     pluginsdk.TypeString,
        Required: true,
    },

    "fqdn": {
        Type:     pluginsdk.TypeString,
        Computed: true,
    },
}
```
