"""
A classmethod is similar to a @staticmethod. However:
  - Receives the class (cls) as its first argument.
  - Can access and modify class-level attributes.
  - Is often used as an alternative constructor.

# Quick comparison
 
| Method Type     | First Parameter | Access Instance Data?  | Access Class Data?  |
| --------------- | --------------- | ---------------------  | ------------------  |
| Instance Method | `self`          | ✅ Yes                 | ✅ Yes              |
| Class Method    | `cls`           | ❌ No                  | ✅ Yes              |
| Static Method   | None            | ❌ No                  | ❌ No               |
"""


# accessing class variables
class Person:
    species = "Human"

    def __init__(self, species) -> None:
        self.species = species

    @classmethod
    def show_species(cls):
        print(cls.species)


Person.show_species()  # Human
pobj = Person("Cat")

print(pobj.species)  # Cat
pobj.show_species()  # Human (not cat)


#
# We can use classmethods to create alternative constructors too!
class ChaiOrder:
    def __init__(self, tea_type, sweetness, size) -> None:
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size = size

    # TAke dictionary
    @classmethod
    def from_dict(cls, order: dict[str, str]) -> ChaiOrder:
        return cls(order["tea_type"], order["sweetness"], order["size"])

    # take string
    @classmethod
    def from_str(cls, order: str):
        tea_type, sweetness, size = order.split("-")
        return cls(tea_type, sweetness, size)

    def show_order(self):
        print(self.tea_type, self.sweetness, self.size)


order1 = ChaiOrder(tea_type="masala", sweetness="mid", size="jambo")
order2 = ChaiOrder.from_dict(
    {"tea_type": "masala", "sweetness": "mid", "size": "jumbo"}
)
order3 = ChaiOrder.from_str("masala-mid-jambo")


print("\n")
order1.show_order()
order2.show_order()
order3.show_order()

# btw, we can just use the dict dunder var..
print("\n", order1.__dict__)
print(order2.__dict__)
print(order3.__dict__)
