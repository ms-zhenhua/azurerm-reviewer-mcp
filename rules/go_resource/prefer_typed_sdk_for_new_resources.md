Use Typed SDK for new resources instead of Untyped SDK. New resources should import and use `"github.com/hashicorp/terraform-provider-azurerm/internal/sdk"` for better validation, error handling, and future framework migration.

### good:
```go
package someservice

import (
    "github.com/hashicorp/terraform-provider-azurerm/internal/sdk"
    pluginsdk "github.com/hashicorp/terraform-plugin-sdk/v2/helper/schema"
)

type SomeResource struct{}

var _ sdk.ResourceWithUpdate = SomeResource{}

type SomeResourceModel struct {
    DisplayName   string            `tfschema:"display_name"`
    ResourceGroup string            `tfschema:"resource_group_name"`
    Tags          map[string]string `tfschema:"tags"`
}

func (r SomeResource) ResourceType() string {
    return "azurerm_some_resource"
}

func (r SomeResource) ModelObject() interface{} {
    return &SomeResourceModel{}
}

func (r SomeResource) IDValidationFunc() pluginsdk.SchemaValidateFunc {
    return someService.ValidateSomeResourceID
}
```

### bad:
```go
package someservice

import (
    pluginsdk "github.com/hashicorp/terraform-plugin-sdk/v2/helper/schema"
)

func someResource() *pluginsdk.Resource {
    return &pluginsdk.Resource{
        Create: someResourceCreate,
        Read:   someResourceRead,
        Update: someResourceUpdate,
        Delete: someResourceDelete,
        // No built-in ID validation, encoding/decoding, etc.
    }
}
```
