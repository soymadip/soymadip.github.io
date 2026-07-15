# -- filter() --
# Constructs an iterator of the items from given iterable which given function returns True for.
# syntax: filter(func | lambda, iterable)
# It returns a filter object, an iterator (of type filter).
#    So we need to convert to list/tuple/set... to see all values when printing.

lst = [10, 12, 9, 35, 90]

evens = list(filter(lambda x: x % 2 == 0, lst))
# evens = [x for x in lst if x % 2 == 0] this is pythonic way, list comprehension

print(evens)
