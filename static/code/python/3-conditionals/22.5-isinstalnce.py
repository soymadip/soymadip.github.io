"""
What is isinstance()?

It answers one question:

    "Is this object an instance of this type (or class)?"

    Returns True or False
"""

x = 10

# Check if x is of type int
print(isinstance(x, int))


y = "google is shit"

print(isinstance(y, int))  # False

# Match OneOf multiple type
print(isinstance(y, (int, str)))  # True


# We can also check if an instance is of a class


class Animal: ...


class Dog(Animal): ...


dog = Dog()

print(isinstance(dog, Dog))  # True

print(isinstance(dog, Animal))  # True. Why? Because Dog is subclass of Animal.


# subtypes are types that are inherited from a type. python internally coverts them
# boolean is subclass of int. so python implicit type converts it
#
print(True + True)  # 2


#
# If you need exact type
print(type(dog) == Animal)  # False
