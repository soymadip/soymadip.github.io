# pure, impure, lambda/anonymous functions

# pure function, doesnt change global things
def pure_chai(cups):
    return cups


total_chai = 10


# impure, changes global things. not recommended
def impure_chai(cups):
    global total_chai
    total_chai += 10


# Recursive function, calls itself
def pour_chai(n):
    if n == 0:
        return "All cups poured"

    return pour_chai(n - 1)


# ----------------- Lambdas -----------------
#
# These keep the namespace clean
chai_types = ["light", "kadak", "ginger", "kadak"]
strong_chai = list(filter(lambda chai: chai == "kadak", chai_types))

# syntax: lambda arguments : expression
x = lambda a: a + 10
print(x(5))
