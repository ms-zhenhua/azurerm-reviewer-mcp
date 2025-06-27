Define `expand...` and `flatten...` functions as global methods rather than member methods of resource structs.

### good:
```go
func expandComplexResource(input []ComplexResource) *resource.ComplexResource {
    ...
}

func flattenComplexResource(input *resource.ComplexResource) []ComplexResource {
    ...
}
```

### bad:
```go
func (r ResourceGroupExampleResource) expandComplexResource(input []ComplexResource) *resource.ComplexResource {
    ...
}

func (r ResourceGroupExampleResource) flattenComplexResource(input *resource.ComplexResource) []ComplexResource {
    ...
}
```
