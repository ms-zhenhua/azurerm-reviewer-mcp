Field names in validation error messages should be wrapped in backticks for proper formatting and clarity.

### good:
```go
"name": {
	Type:     pluginsdk.TypeString,
	Required: true,
	ForceNew: true,
	ValidateFunc: validation.StringMatch(
		regexp.MustCompile(`^[a-zA-Z0-9\_\.\-]{1,64}$`),
		"`name` must be ...",
	),
},
```

### bad:
```go
"name": {
	Type:     pluginsdk.TypeString,
	Required: true,
	ForceNew: true,
	ValidateFunc: validation.StringMatch(
		regexp.MustCompile(`^[a-zA-Z0-9\_\.\-]{1,64}$`),
		"name must be ...",
	),
},
```
