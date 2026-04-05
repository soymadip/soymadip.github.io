---

id: "19 - sets"
name: "Python Sets"
title: "Python — Sets
"
sidebar_label: "Sets"
sidebar_position: 19
description: "Concise revision notes for Python's built-in `set` type — derived from `19 - sets.py`."
---

# Python — Sets

Short, revision-friendly notes derived from the example `19 - sets.py`. Focus on what you need to remember and quick examples you can run.

:::tip
**Instructor tip:** Sets are great for uniqueness and fast membership checks. Use them when you need O(1) average membership tests.
:::

## Example (source)

```notes/python/code/19 - sets.py#L1-17
essential_spices = {"cardamom", "ginger", "cinemon"}
optional_spices = {"cloves", "ginger", "black paper"}

# union: All items, no repeatation
all_spices = essential_spices | optional_spices
print(f"All spices: {all_spices}")


# Intersection: common