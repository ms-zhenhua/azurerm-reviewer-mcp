Use proper symbols for different types of documentation notes. Use `->` for informational notes, `~>` for warning notes, and `!>` for caution notes to ensure consistent documentation formatting.

### good:
```markdown
-> **Note:** More information on each of the supported types can be found in [type documentation](link-to-additional-info)

~> **Note:** The argument `optional_argument` is required when `optional_argument_enabled` is set to `true`.

!> **Note:** The argument `irreversible_argument_enabled` cannot be disabled after being enabled.
```

### bad:
```markdown
**NOTE:** The `encryption` block can only be set when `encryption_type` is set to `EncryptionAtRestWithCustomerManagedKey`.
```
