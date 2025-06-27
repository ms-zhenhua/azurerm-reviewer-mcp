Required fields should be documented before Optional fields in resource documentation to improve readability and help users quickly identify mandatory parameters.

### good:
```markdown
* `replica_timeout_in_seconds` - (Required) The maximum number of seconds a replica is allowed to run.

* `workload_profile_name` - (Optional) The name of the workload profile to use for the Container App Job.
```

### bad:
```markdown
* `workload_profile_name` - (Optional) The name of the workload profile to use for the Container App Job.

* `replica_timeout_in_seconds` - (Required) The maximum number of seconds a replica is allowed to run.
```
