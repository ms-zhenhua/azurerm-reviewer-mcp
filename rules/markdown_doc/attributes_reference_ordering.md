Attributes in the documentation are expected to be ordered as follows:

1. The `id` attribute.
2. The remaining attributes, sorted alphabetically.

Block attributes must have two entries in the documentation:

1. The initial entry, e.g., `* block_attribute - A block_attribute as defined below.`
2. A subsection, added after all top-level attributes. If multiple blocks are present in the resource, these subsections should be ordered alphabetically.

## good

```markdown
## Attributes Reference

`id` - The ID of this resource.

`block_attribute` - A `block_attribute` as defined below.

`some_other_attribute` - This attribute returns something magical.

---

A `block_attribute` exports the following:

* `nested_attribute_1` - A very whimsical attribute.

* `nested_attribute_2` - A much more monotonous attribute.

## Timeouts

...
```

## bad

```markdown
## Attributes Reference

`block_attribute` - A `block_attribute` as defined below.

`some_other_attribute` - This attribute returns something magical.

---

A `block_attribute` exports the following:

* `nested_attribute_1` - A very whimsical attribute.

* `nested_attribute_2` - A much more monotonous attribute.

## Timeouts

...
```
