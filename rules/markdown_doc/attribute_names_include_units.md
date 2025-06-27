Properties that pertain to sizes, durations, windows, or occurrences should be appended with the appropriate unit of measure to ensure clarity and prevent confusion.

## good

```markdown
* `duration_in_seconds` - (Optional) Specifies the duration of the operation in seconds.
* `size_in_gb` - (Required) Specifies the size of the disk in gigabytes.
* `timeout_in_minutes` - (Optional) Specifies the timeout period in minutes.
* `retention_in_days` - (Required) Specifies the retention period in days.
* `max_occurrences_per_hour` - (Optional) Specifies the maximum number of occurrences per hour.
* `interval_in_milliseconds` - (Optional) Specifies the polling interval in milliseconds.
```

## bad

```markdown
* `duration` - (Optional) Specifies the duration of the operation.
* `size` - (Required) Specifies the size of the disk.
* `timeout` - (Optional) Specifies the timeout period.
* `retention` - (Required) Specifies the retention period.
* `max_occurrences` - (Optional) Specifies the maximum number of occurrences.
* `interval` - (Optional) Specifies the polling interval.
```
