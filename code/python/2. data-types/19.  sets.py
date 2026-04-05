essential_spices = {"cardamom", "ginger", "cinemon"}
optional_spices = {"cloves", "ginger", "black paper"}

# union: All items, no repeatation
all_spices = essential_spices | optional_spices
print(f"All spices: {all_spices}")


# Intersection: common  items
common_spices: set[str] = essential_spices & optional_spices
print(common_spices)


only_in_essentials = essential_spices - optional_spices
print(f"Only in essential: {only_in_essentials}")

print(f"Is clove in optional_spices: {'cloves' in optional_spices}")
