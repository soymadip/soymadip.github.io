class Chai:
    def __init__(self, type_, strength) -> None:
        self.type = type_  # this creates instance attribute
        self.strength = strength

    def prepare(self):
        print(f"Preparing {self.type} chai with strength: {self.strength}....")


## When we inherit a child class, python automatically calls parent's constructor.
class MasalaChai(Chai):
    type = "ginger"
    # Class attribute: does NOT become self.type automatically.
    # It is used only if the instance does not define "type".
    # Accessible as MasalaChai.type or via an instance only as a fallback.


chai = MasalaChai("Masala", 150)  # parent's constructor is called.
chai.prepare()  # Preparing Masala chai with strength: 150....
print(chai.type)  #  will be `masala` as the instance has a type attribute too

# So in oneline, If an instance attribute and a class attribute have the same name,
# the instance attribute overrides (shadows) the class attribute.


# But if we wanna customise the constructor, we have to define child's
class GreenChai(Chai):
    def __init__(self, strength, extra_attr) -> None:
        super().__init__("Green", strength)
        self.extra_attr = extra_attr  # any extra child class's attribute needs to be mapped


green_chai = GreenChai(200, "some_extra_arg")
green_chai.prepare()  # Preparing Green chai with strength: 200....
print(green_chai.type) # Green
