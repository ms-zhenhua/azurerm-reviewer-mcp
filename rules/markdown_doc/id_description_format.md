Property descriptions for `id` or properties ending with `_id` must start with `The ID of`.

## good

```markdown
* `id` - The ID of the Cross Region Disaster Recovery Autonomous Database.
* `subnet_id` - The ID of the subnet where the resource is deployed.
* `network_security_group_id` - The ID of the Network Security Group.
* `key_vault_id` - The ID of the Key Vault.
```

## bad

```markdown
* `id` - The Immutable Azure Resource ID of the Cross Region Disaster Recovery Autonomous Database.
* `subnet_id` - A subnet identifier for deployment.
* `network_security_group_id` - Network Security Group resource identifier.
* `key_vault_id` - Key Vault resource ID.
```
