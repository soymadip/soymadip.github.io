# Each object posseses is own namespace. likke it's variables that not overlaps with another ones


class Chai:
    origin = "India"


print(Chai.origin)  # access the property of class

Chai.is_hot = True  # this is called dynamic assignment. this is highly discouraged in prod code. more in later lessons
print(Chai.is_hot)


# creating objects from calss chai

masala = Chai()

print("from object")
print(masala.origin)
print(masala.is_hot)


masala.is_hot = False
print(f"Class: {Chai.is_hot}")

print(
    f"Masala: {masala.is_hot}"
)  # changing object property's value doesn't change class property's value

masala.flavour = "Masala"

print(masala.flavour)
