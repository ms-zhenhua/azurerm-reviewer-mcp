Use correct spelling for field names and variables.

### good:
```go
type NetworkSecurityRule struct {
    DestinationIps   []string
}
```

### bad:
```go
type NetworkSecurityRule struct {
    DesticationIps   []string  // misspelled "Destination"
}
```
