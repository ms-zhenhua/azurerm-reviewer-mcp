Use the fixed format `fmt.Errorf("decoding: %+v", err)` when `metadata.Decode` fails.

### good:
```go
if err := metadata.Decode(&state); err != nil {
	return fmt.Errorf("decoding: %+v", err)
}
```

### bad:
```go
if err := metadata.Decode(&state); err != nil {
	return err
}
```
