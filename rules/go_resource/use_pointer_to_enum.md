use `pointer.ToEnum` to convert Enum type instead of explicitly type conversion.

### good:
```go
return &managedclusters.ManagedClusterBootstrapProfile{
    ArtifactSource: pointer.ToEnum[managedclusters.ArtifactSource](config["artifact_source"].(string)),
}
```

### bad:
```go
return &managedclusters.ManagedClusterBootstrapProfile{
    ArtifactSource: pointer.To(managedclusters.ArtifactSource(config["artifact_source"].(string))),
}
```
