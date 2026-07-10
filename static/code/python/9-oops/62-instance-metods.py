class Chaicup:
    size = 150  # ml

    def describe(self):  # refers to the instance
        return f"A {self.size}ml chai cup."


cup1 = Chaicup()

print(cup1.describe())  # internally python translates to Chaicup.describe(cup1)


# print(Chaicup.describe())
# gives error: `missing 1 required pos: self`.
# Calling a method on the class does not automatically pass an instance.
# Python only supplies `self` automatically when the method is called on an instance.

print(Chaicup.describe(cup1))  # this works as we pass the object when calling.
