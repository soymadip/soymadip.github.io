# pure, impure, lambda/anonymous functions

# pure function, doesnt change global things
def pure_chai(cups):
    return cups


total_chai = 10


# impure, changes global things. not recommended
def impure_chai(cups: int) -> None:
    global total_chai
    total_chai += cups


# Recursive function, calls itself
def pour_chai(n):
    if n == 0:
        return "All cups poured"

    return pour_chai(n - 1)


# ----------------- Lambdas -----------------
# Small one time function
# These keep the namespace clean
chai_types = ["light", "kadak", "ginger", "kadak"]
strong_chai = list(filter(lambda chai: chai == "kadak", chai_types))

# syntax: lambda arguments : expression
double = lambda x: x * 2
print(double(2))

add = lambda x, y: x + y
print(add(10, 12))

# we can also use conditionals
max_value = lambda x, y: x if x > y else y
print(max_value(10, 18))

full_name = lambda fstnm, lstnm: fstnm + " " + lstnm
print(full_name("soymadip", "Das"))

# Also can return bool
age_check = lambda age: True if age >= 18 else False
print(f"Is he adult? {age_check(10)}")
