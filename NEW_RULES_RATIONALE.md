# New Code Review Rules Added to AzureRM Reviewer MCP

## Overview

This document explains the rationale behind adding 6 new code review rules to the AzureRM Reviewer MCP tool. These rules were identified as critical gaps when comparing the existing rule set with the official [AzureRM Provider Contributor Guidelines](https://github.com/hashicorp/terraform-provider-azurerm/tree/main/contributing).

## Analysis Summary

### Coverage Assessment
- **Before**: The MCP tool had approximately 50 rules covering basic patterns
- **Gap Identified**: Missing several high-priority best practices from the official guidelines
- **After**: Added 6 critical rules addressing the most important missing patterns

### Priority Classification
The new rules address **Tier 1 (Critical)** gaps that directly impact:
- Terraform functionality (`ignore_changes` support)
- Code maintainability (typed vs untyped patterns)
- User experience (schema design consistency)
- Documentation quality (standardized formatting)

## New Rules Added

### 1. `separate_create_update_methods.md`

**File**: `rules/go_resource/separate_create_update_methods.md`

**Why Added**: 
- **Official Guideline**: [Best Practices - Separate Create and Update Methods](https://github.com/hashicorp/terraform-provider-azurerm/blob/main/contributing/topics/best-practices.md#separate-create-and-update-methods)
- **Critical Issue**: Combined CreateOrUpdate methods break Terraform's `ignore_changes` feature
- **Impact**: Without this pattern, users cannot properly ignore fields they want Azure to manage with defaults

**What It Catches**:
- Resources using combined create/update functions
- Missing `d.HasChanges()` checks in update methods
- Improper handling of partial updates

**Business Value**:
- Enables proper Terraform state management
- Supports advanced Terraform features users expect
- Prevents configuration drift issues

### 2. `prefer_typed_sdk_for_new_resources.md`

**File**: `rules/go_resource/prefer_typed_sdk_for_new_resources.md`

**Why Added**:
- **Official Guideline**: [Best Practices - Typed vs. Untyped Resources](https://github.com/hashicorp/terraform-provider-azurerm/blob/main/contributing/topics/best-practices.md#typed-vs-untyped-resources)
- **Strategic Direction**: AzureRM is migrating from plugin-sdk to internal SDK
- **Code Quality**: Typed SDK provides better validation, error handling, and future-proofing

**What It Catches**:
- New resources not using the internal SDK package
- Missing ID validation functions
- Lack of type safety in resource definitions

**Business Value**:
- Reduces runtime errors through compile-time validation
- Enables future migration to terraform-plugin-framework
- Improves developer experience with better tooling

### 3. `avoid_optional_computed_pattern.md`

**File**: `rules/go_resource/avoid_optional_computed_pattern.md`

**Why Added**:
- **Official Guideline**: [Best Practices - Setting Properties to Optional + Computed](https://github.com/hashicorp/terraform-provider-azurerm/blob/main/contributing/topics/best-practices.md#setting-properties-to-optional--computed)
- **User Experience Issue**: O+C fields are difficult for users to reset to defaults
- **Future Compatibility**: Will cause errors in terraform-plugin-framework v6

**What It Catches**:
- Fields marked as both Optional and Computed without justification
- Missing explanatory comments when O+C is necessary
- Patterns that will break in future Terraform versions

**Business Value**:
- Improves user experience with configuration management
- Prevents future breaking changes
- Provides clearer configuration semantics

### 4. `sku_field_patterns.md`

**File**: `rules/go_resource/sku_field_patterns.md`

**Why Added**:
- **Official Guideline**: [Schema Design Considerations - SKU fields](https://github.com/hashicorp/terraform-provider-azurerm/blob/main/contributing/topics/schema-design-considerations.md#sku-fields)
- **Consistency Issue**: Inconsistent SKU implementations across resources
- **User Experience**: Standardized patterns improve usability

**What It Catches**:
- Inconsistent SKU field naming (`sku_name`, `sku_family` vs. standardized patterns)
- Incorrect choice between single argument vs. block design
- Missing validation for SKU values

**Business Value**:
- Provides consistent user experience across all Azure resources
- Reduces learning curve for users working with multiple resources
- Improves configuration predictability

### 5. `split_discriminator_types.md`

**File**: `rules/go_resource/split_discriminator_types.md`

**Why Added**:
- **Official Guideline**: [Schema Design Considerations - The `type` field](https://github.com/hashicorp/terraform-provider-azurerm/blob/main/contributing/topics/schema-design-considerations.md#the-type-field)
- **Complexity Issue**: Generic resources with type discriminators are hard to use and maintain
- **Validation Benefits**: Specific resources provide better field validation

**What It Catches**:
- Resources using generic `type` fields with many possible values
- Mixed schema with fields that only apply to certain types
- Missing type-specific validation

**Business Value**:
- Simplifies resource usage with only relevant fields exposed
- Enables better validation and error messages
- Reduces configuration complexity and errors

### 6. `standardized_note_formatting.md`

**File**: `rules/markdown_doc/standardized_note_formatting.md`

**Why Added**:
- **Official Guideline**: [Provider Documentation Standards - Notes](https://github.com/hashicorp/terraform-provider-azurerm/blob/main/contributing/topics/reference-documentation-standards.md#notes)
- **Documentation Quality**: Inconsistent note formatting across documentation
- **User Experience**: Standardized formatting improves information hierarchy

**What It Catches**:
- Incorrect note formatting symbols (using `**Info:**` instead of `-> **Note:**`)
- Missing severity indicators (info vs. warning vs. caution)
- Inconsistent capitalization and punctuation

**Business Value**:
- Improves documentation readability and consistency
- Helps users quickly identify important vs. critical information
- Maintains professional documentation standards

## Implementation Impact

### For Code Reviews
These rules will now automatically detect and flag:
- Architectural anti-patterns that break Terraform functionality
- Inconsistent schema designs that confuse users
- Documentation formatting that doesn't meet project standards

### For Developers
- **Immediate**: Clear guidance on current best practices
- **Future**: Protection against deprecated patterns
- **Consistency**: Standardized approaches across the entire provider

### For Users
- **Better Experience**: More consistent and predictable resource behavior
- **Fewer Bugs**: Reduced configuration drift and state management issues
- **Clear Documentation**: Standardized information presentation

## Validation

These rules were derived directly from:
1. **Official AzureRM Provider Guidelines** - All rules map to specific sections
2. **Current Best Practices** - Reflect the project's current direction
3. **Real-World Issues** - Address common problems seen in pull requests

## Next Steps

### Immediate
1. Review and approve these new rules
2. Test against existing codebase to validate accuracy
3. Update team documentation with new standards

### Future Considerations
The analysis identified additional gaps that could be addressed in future iterations:
- Internal error prefixing patterns
- Comprehensive property naming rules
- State migration requirements
- Acceptance testing patterns

## Conclusion

These 6 rules address the most critical gaps in our automated code review coverage, ensuring that new code follows the latest AzureRM Provider standards and best practices. They focus on areas that directly impact user experience, code maintainability, and Terraform functionality.
