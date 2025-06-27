`pointer.From` returns the dereferenced value or zero if the pointer is `nil`. Use it instead of manual `nil` checks.

### good:
```go
output.Name = pointer.From(input.Name)
```

### bad:
```go
if input.Name != nil {
    output.Name = *input.Name
}
```
