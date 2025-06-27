Avoid using redundant words in attribute names that don't add informational value. Use concise, meaningful names that convey the essential information without unnecessary suffixes or descriptors.

### good:
```markdown
* `firewall` - (Required) Specifies the firewall configuration.
* `email` - (Optional) Specifies the email for notifications.
* `subnet` - (Required) Specifies the subnet configuration.
* `endpoint` - (Optional) Specifies the service endpoint.
```

### bad:
```markdown
* `firewall_properties` - (Required) Specifies the firewall configuration.
* `email_address` - (Optional) Specifies the email for notifications.
* `subnet_details` - (Required) Specifies the subnet configuration.
* `endpoint_configuration` - (Optional) Specifies the service endpoint.
```
