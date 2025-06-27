Boolean attributes named `disableSomething` in the API should be flipped and exposed as `something_enabled` in the provider to provide a more intuitive user experience. This approach aligns with Terraform's convention of using positive boolean attributes.

### good:
```markdown
* `file_copy_enabled` - (Optional) Whether to enable the File Copy feature for the Bastion Host. Defaults to `false`.
* `ip_forwarding_enabled` - (Optional) Whether to enable IP Forwarding on the Network Interface. Defaults to `false`.
* `accelerated_networking_enabled` - (Optional) Whether to enable Accelerated Networking on the Network Interface. Defaults to `false`.
```

### bad:
```markdown
* `disable_file_copy` - (Optional) Whether to disable the File Copy feature for the Bastion Host. Defaults to `true`.
* `disable_ip_forwarding` - (Optional) Whether to disable IP Forwarding on the Network Interface. Defaults to `true`.
* `disable_accelerated_networking` - (Optional) Whether to disable Accelerated Networking on the Network Interface. Defaults to `true`.
```
