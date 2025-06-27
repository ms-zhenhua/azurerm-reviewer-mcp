# Property Format Naming

Append format specifications to property names to clarify the expected data type and encoding. For UTC timestamps, use `_in_utc` suffix.

## good:
```markdown
* `certificate_base64` - (Required) The certificate content encoded in Base64 format.
* `policy_json` - (Optional) The policy document in JSON format.
* `content_base64` - (Required) The file content encoded in Base64 format.
* `data_url` - (Optional) The data in URL format.
* `timestamp_in_utc` - (Optional) The timestamp in UTC format.
```

## bad:
```markdown
* `certificate` - (Required) The certificate content encoded in Base64 format.
* `policy` - (Optional) The policy document in JSON format.
* `content` - (Required) The file content encoded in Base64 format.
* `data` - (Optional) The data in URL format.
* `timestamp` - (Optional) The timestamp in UTC format.
```
