In `Exists` function, directly return error if `Get` fails with error message format `"retrieving %s: %+v", *id, err`. Use `pointer.To` instead of `utils.Bool` for the final return. Do not declare a `client` variable if it's only used once.

### good:
```go
func (r FabricCapacityResource) Exists(ctx context.Context, clients *clients.Client, state *pluginsdk.InstanceState) (*bool, error) {
	id, err := fabriccapacities.ParseCapacityID(state.ID)
	if err != nil {
		return nil, err
	}

	resp, err := clients.Fabric.FabricCapacitiesClient.Get(ctx, *id)
	if err != nil {	
		return nil, fmt.Errorf("retrieving %s: %+v", *id, err)
	}
	
	return pointer.To(resp.Model != nil), nil
}
```

### bad:
```go
func (r FabricFabricCapacityResource) Exists(ctx context.Context, clients *clients.Client, state *pluginsdk.InstanceState) (*bool, error) {
	id, err := fabriccapacities.ParseCapacityID(state.ID)
	if err != nil {
		return nil, err
	}

	client := clients.Fabric.FabricCapacitiesClient
	resp, err := client.Get(ctx, *id)
	if err != nil {
		if response.WasNotFound(resp.HttpResponse) {	
			return pointer.To(false), nil	
		}
		
		return nil, fmt.Errorf("reading %s: %+v", *id, err)
	}
		
	return utils.Bool(resp.Model != nil), nil
}
```
