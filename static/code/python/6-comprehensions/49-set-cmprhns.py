# Works almost same as list comprehension

fav_chais: list[str] = [
    "Masala Chai",
    "Green tea",
    "Masala ChaiLemon Chai",
    "Green Tea",
    "Elaichi Chai",
]


# We use set for unique values
unq_chai = {chai for chai in fav_chais}

print(unq_chai)


## complex use case

reciepies = {
    "masala Chai": ["ginger", "Cardimum", "clove"],
    "Elaichi Chai": ["Cardimum", "milk"],
    "Spicy Chai": ["ginger", "black paper", "clove"],
}

unq_spices = {spice for ingredients in reciepies.values() for spice in ingredients}
#                       The var     first loop -> returns lists     second loop for iterating
#                      returning     of spices                         over the lists.
