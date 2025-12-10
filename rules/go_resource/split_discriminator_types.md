When APIs use discriminator types (indicated by `type` or `kind` fields), split them into separate resources rather than exposing a generic resource with all possible fields.

### good:
```go
// Split into separate resources
azurerm_data_factory_linked_service_azure_blob_storage
azurerm_data_factory_linked_service_azure_databricks  
azurerm_data_factory_linked_service_azure_file_storage
azurerm_data_factory_linked_service_azure_function
azurerm_data_factory_linked_service_azure_search
```

### bad:
```go
// Don't create generic resource with type field
"type": {
    Type:     pluginsdk.TypeString,
    Required: true,
    ValidateFunc: validation.StringInSlice([]string{
        string(datafactory.TypeBasicLinkedServiceTypeAzureBlobStorage),
        string(datafactory.TypeBasicLinkedServiceTypeAzureDatabricks),
        string(datafactory.TypeBasicLinkedServiceTypeAzureFileStorage),
        string(datafactory.TypeBasicLinkedServiceTypeAzureFunction),
        string(datafactory.TypeBasicLinkedServiceTypeAzureSearch),
        // ... many more types with different required fields
    }, false),
}
// Plus all possible fields for all types mixed together
```
