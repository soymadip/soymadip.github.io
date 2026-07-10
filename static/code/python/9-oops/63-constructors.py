class ChaiOrder:
    def __init__(self, type_, size) -> None: # this is constructor. We have to pass type_ and size when creating an object/instance of this class (initiating a object)
        self.type = type_  # why the _? type() is a builtin method. so the _ to distinguish
        self.size = size

    def summmary(self):
        return f"{self.size}ml of {self.type} chai"


order1 = ChaiOrder(type_="masalala", size=150)  # instance of a class
order2 = ChaiOrder("ginger", 220)

print(order1.summmary())
print(order2.summmary())
