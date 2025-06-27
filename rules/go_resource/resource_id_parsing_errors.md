When parsing existing Resource IDs, return the error directly without additional wrapping. The parsing functions already return standardized and descriptive error messages.

### good:
```go
id, err := someResource.ParseResourceID(state.ID)
if err != nil {
    return err
}
```

### bad:
```go
id, err := someResource.ParseResourceID(state.ID)
if err != nil {
    return fmt.Errorf("parsing `resource_id`: %+v", err)
}
```
