Each property in the documentation should be explicitly marked as `Required` or `Optional` to ensure clarity for users about which fields are mandatory and which are optional when configuring the resource.

## good

```markdown
* `name` - (Required) The name of the resource.
* `resource_group_name` - (Required) The name of the Resource Group where the Cross Region Disaster Recovery Autonomous Database should exist.
* `location` - (Required) The Azure Region where the resource should exist.
* `tags` - (Optional) A mapping of tags to assign to the resource.
```

## bad

```markdown
* `name` - The name of the resource.
* `resource_group_name` - The name of the Resource Group where the Cross Region Disaster Recovery Autonomous Database should exist.
* `location` - The Azure Region where the resource should exist.
* `tags` - A mapping of tags to assign to the resource.
```
