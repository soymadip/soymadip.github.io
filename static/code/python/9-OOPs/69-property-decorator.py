"""
Here we gonna talk about getters and setters in python

"""


class Person:
    def __init__(self, age):
        self._age = age  # this is a internal prop/attribute. we dnt want users to change/access this.

    # so give users to access we give methods.

    # to get value
    def get_age(self):
        return self._age

    # to set value
    def set_age(self, age):
        self._age = age


me = Person(12)

print(me.get_age())  # 12

me.set_age(14)
print(me.get_age())  # 14


# But this is considered non pythonic.
# There is a better way to declare getter and setter. with property decorator


class Gay:
    def __init__(self, age) -> None:
        self._age = age  # btw about this, this doesnt protect from initiating with negative value

    @property  # getter
    def age(
        self,
    ):  # Name the method same as the prop to be exposed. in this case we want users to use 'age'
        return self._age

    @age.setter  # setter
    def age(self, age):

        if age > 0:
            self._age = age
        else:
            raise ValueError("Age cant be negative")


me = Gay(-21)

print()
print(me.age)

me.age = 69
print(me.age)
