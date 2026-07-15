# -- map() --
# Applies a specific function to every item in an iterable and returns an iterator.
# map() returns a map object, an iterator (of type map). Why? because of efficiency. Iterator calculates next value when asked. ALSO, THIS IS ONE TIME USE
# We need to convert to list to see all values when printing.

lists = [1, 2, 3]
mapobj = map(lambda x: x**3, lists)
mlist = list(mapobj)

print(mlist)

# Remember that an iterator (like your mpobj) is a one-way stream. Once you "consume" it, it's empty.
# What happened in your code:
#     print(list(mpobj)): When you wrapped mpobj in list(), you told Python to pull every single value out of the iterator to build that list.
#     The Exhaustion: By the time that line finished, the mpobj iterator had reached the end of the data. It "remembered" that it had no more items left.
#     The Loop: When the for loop started, it asked mpobj for the next value. mpobj essentially replied, "I'm already finished," so the loop body never executed.
