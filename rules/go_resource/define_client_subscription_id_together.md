Define `client` and `subscriptionId` together at the beginning of the function, rather than scattered throughout the function body.

### good:
```go
func(ctx context.Context, metadata sdk.ResourceMetaData) error {
    client := metadata.Client.Resource.GroupsClient
    subscriptionId := metadata.Client.Account.SubscriptionId

    var config ResourceGroupExampleResourceModel
    if err := metadata.Decode(&config); err != nil {
        return fmt.Errorf("decoding: %+v", err)
    }

    id := resources.NewResourceGroupID(subscriptionId, config.Name)
    // ... rest of function
}
```

### bad:
```go
func(ctx context.Context, metadata sdk.ResourceMetaData) error {
    client := metadata.Client.Resource.GroupsClient

    var config ResourceGroupExampleResourceModel
    if err := metadata.Decode(&config); err != nil {
        return fmt.Errorf("decoding: %+v", err)
    }

    subscriptionId := metadata.Client.Account.SubscriptionId
    id := resources.NewResourceGroupID(subscriptionId, config.Name)
    // ... rest of function
}
```
