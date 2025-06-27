`pluginsdk.StateChangeConf` is deprecated and should be replaced with custom pollers for handling Long Running Operations (LRO) APIs. Please refer to this [example](https://github.com/hashicorp/terraform-provider-azurerm/blob/main/internal/services/maps/custompollers/maps_account_poller.go).

### good:
```go
func (p mapsAccountPoller) Poll(ctx context.Context) (*pollers.PollResult, error) {
    ...
}
```

### bad:
```go
state := &pluginsdk.StateChangeConf{
    Pending:    []string{...},
    Target:     []string{...},
    Refresh:    ...,
    Timeout:    ...,
}

if _, err := state.WaitForStateContext(ctx); err != nil {
    ...
}
```
