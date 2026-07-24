class Person:
    def __init__(self, name: str, age: int, address: str) -> None:
        self.name = name
        self.age = age
        self.address = address

    def print_info(self) -> None:
        print(
            f"HI, my name is {self.name}, i am {self.age} years old and live in {self.address}"
        )


me = Person("Soumadip", 15, "Naihati")

me.print_info()


# lets say we want to access a attribute what users says.
# We use getattr() for this job

choice = input("What attribute do you wanna access:  ")

#             obj  attr   fallback (optional)
print(getattr(me, choice, None))
print(getattr(me, choice))  # raises AttributeError if fallback is not given


# We can also set dynamically too:
# we use setattr() to do this

choice = input("What attribute do you wanna change: ")
value = input("Enter the value: ")


#      obj   attr    value
setattr(me, choice, value)  # Creates  the attribute if doesn't exist

print(getattr(me, choice))  # use getattr to print the new value


# we can check if a object has an attribute
print(hasattr(me, "name"))


# we can delete a attribute too
delattr(me, "name")

me.print_info()  # Throws error now as the self.name doesn't exists
