# An Attribute is a variable inside a Class/method. the behavior remains same


class Chai:
    temperature = "hot"
    strength = "strong"


cutting_chai = Chai()


print(cutting_chai.temperature)


cutting_chai.temperature = "mild"
cutting_chai.cup = "small"

print(f"After change: {cutting_chai.temperature}")
print(f"Cup size: {cutting_chai.cup}")
print(f"Direct Class: {Chai.temperature}")

del cutting_chai.temperature  # deleting the attribute
del cutting_chai.cup  # deleting the attribute

print(
    f"After delete: {cutting_chai.temperature}"
)  # if a attribute of an object is not available anymore, it fallbacks to class's attribute (here Chai)

print(
    f"Chai after delete: {cutting_chai.cup}"
)  # This gives error. because we dynamically assigned it so no class fallback.
