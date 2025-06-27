Do not return `nil` from `expand...` functions in `Update` operations as `nil` values are ignored by PATCH requests. Instead, return an empty struct or appropriate zero value to ensure the field is properly cleared.

### good:
```go
func ExpandVolumeGroupEncryption(input []ElasticSANVolumeGroupResourceEncryptionModel) (*volumegroups.EncryptionProperties, error) {
	if len(input) == 0 {
		return &volumegroups.EncryptionProperties{}, nil
	}
	
	// ... expansion logic
}
```

### bad:
```go
func ExpandVolumeGroupEncryption(input []ElasticSANVolumeGroupResourceEncryptionModel) (*volumegroups.EncryptionProperties, error) {
	if len(input) == 0 {
		return nil, nil
	}
	
	// ... expansion logic
}
```
