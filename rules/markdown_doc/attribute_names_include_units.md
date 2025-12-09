Properties that pertain to sizes, durations, windows, or occurrences should be appended with the appropriate unit of measure to ensure clarity and prevent confusion.

**Note:** Memory units should be in singular form (e.g., `size_in_gb`, not `size_in_gbs`), while time units should be in plural form (e.g., `duration_in_seconds`, `timeout_in_minutes`, `timeout_duration`).

## good

```markdown
* `duration_in_seconds` - (Optional) Specifies the duration of the operation in seconds.
* `size_in_gb` - (Required) Specifies the size of the disk in gigabytes.
* `timeout_in_minutes` - (Optional) Specifies the timeout period in minutes.
* `retention_in_days` - (Required) Specifies the retention period in days.
* `max_occurrences_per_hour` - (Optional) Specifies the maximum number of occurrences per hour.
* `interval_in_milliseconds` - (Optional) Specifies the polling interval in milliseconds.
* `cache_percentage` - (Optional) Specifies the cache size as a percentage.
* `scheduled_event_os_image_timeout_duration` - (Optional) Specifies the length of time a virtual machine being deleted will have to potentially approve the terminate scheduled event before the event is auto approved (timed out). The configuration must be specified in ISO 8601 format.
```

## bad

```markdown
* `duration` - (Optional) Specifies the duration of the operation.
* `size` - (Required) Specifies the size of the disk.
* `size_in_gbs` - (Required) Specifies the size of the disk in gigabytes.
* `timeout` - (Optional) Specifies the timeout period.
* `retention` - (Required) Specifies the retention period.
* `max_occurrences` - (Optional) Specifies the maximum number of occurrences.
* `interval` - (Optional) Specifies the polling interval.
* `cache_in_percent` - (Optional) Specifies the cache size in percent.
* `scheduled_event_os_image_timeout` - (Optional) Specifies the length of time a virtual machine being deleted will have to potentially approve the terminate scheduled event before the event is auto approved (timed out). The configuration must be specified in ISO 8601 format.
```
