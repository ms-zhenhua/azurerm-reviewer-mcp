Use the correct note formatting in documentation: `->` for informational notes, `~>` for warnings, and `!>` for caution/critical information.

### good:
```markdown
* `type` - (Required) The type. Possible values include `This`, `That`, and `Other`.

-> **Note:** More information on each of the supported types can be found in [type documentation](link-to-additional-info)

* `optional_argument` - (Optional) An optional argument.

~> **Note:** The argument `optional_argument` is required when `optional_argument_enabled` is set to `true`.

* `irreversible_argument_enabled` - (Optional) Is irreversible argument enabled? Defaults to `false`.

!> **Note:** The argument `irreversible_argument_enabled` cannot be disabled after being enabled.
```

### bad:
```markdown
**Info:** More information on each of the supported types...
**Important:** The argument `optional_argument` is required...
**Be Aware:** The argument `irreversible_argument_enabled`...
**NOTE:** This cannot be changed...
Note: This is important information...
```
