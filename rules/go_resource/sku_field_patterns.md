For SKU fields, use a simple `sku` argument when only the SKU name is needed, or a `sku` block when multiple SKU properties are required. Avoid separate `sku_name`, `sku_family` arguments.

### good:
```go
// Simple SKU - single argument
"sku": {
    Type:     pluginsdk.TypeString,
    Optional: true,
    Default:  string(firewallpolicies.FirewallPolicySkuTierStandard),
    ValidateFunc: validation.StringInSlice([]string{
        string(firewallpolicies.FirewallPolicySkuTierPremium),
        string(firewallpolicies.FirewallPolicySkuTierStandard),
        string(firewallpolicies.FirewallPolicySkuTierBasic),
    }, false),
}

// Complex SKU - use block
"sku": {
    Type:     pluginsdk.TypeList,
    Required: true,
    MaxItems: 1,
    Elem: &pluginsdk.Resource{
        Schema: map[string]*pluginsdk.Schema{
            "name": {
                Type:         pluginsdk.TypeString,
                Required:     true,
                ValidateFunc: validation.StringInSlice(helpers.PossibleValuesForSkuName(), false),
            },
            "capacity": {
                Type:     pluginsdk.TypeInt,
                Optional: true,
                Default:  1,
            },
        },
    },
}
```

### bad:
```go
// Don't use separate sku fields
"sku_name": {
    Type:     pluginsdk.TypeString,
    Required: true,
},
"sku_family": {
    Type:     pluginsdk.TypeString,
    Optional: true,
},
"capacity": {
    Type:     pluginsdk.TypeInt,
    Optional: true,
},
```
