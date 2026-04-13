'''

In Python, an Iterator is an object that allows you to traverse through all the elements of a collection, regardless of its specific implementation. It is the engine behind for loops, map(), filter(), and list comprehensions.

1. The Core Concept: Iterable vs. Iterator

It is easy to confuse these two, but they serve different roles in the Iterator Protocol.

Term

Definition

Examples

Iterable

Any object you can loop over. It can produce an iterator.

list, str, tuple, dict

Iterator

The stateful object that actually performs the traversal.

map object, zip object, generator

:::tip The Vending Machine Analogy

The Iterable is the Vending Machine. It holds all the items.

The Iterator is the Mechanical Arm. It knows which item is next and hands it to you one by one.
:::

2. The Iterator Protocol

For an object to be considered an iterator in Python, it must implement two methods:

__iter__(): Returns the iterator object itself. This allows an iterator to be used where an iterable is expected.

__next__(): Returns the next item in the sequence. If there are no items left, it must raise StopIteration.

Manual Interaction

You can manually interact with this protocol using the built-in iter() and next() functions:

data = [10, 20]
it = iter(data)  # Calls data.__iter__()

print(next(it))  # Calls it.__next__() -> 10
print(next(it))  # Calls it.__next__() -> 20
# print(next(it)) # Raises StopIteration


3. Key Characteristics

⚡ Lazy Evaluation

Iterators use Lazy Evaluation. They don't calculate or store all their values upfront. They only compute the "next" value when you explicitly ask for it.

Benefit: Massive memory savings. You can iterate over a 10GB file or even an infinite sequence without crashing your RAM.

⚠️ Exhaustion (One-Way Street)

Iterators are consumable. Once you have traversed to the end, the iterator is "exhausted."

:::warning Exhaustion Trap
Calling list(my_iterator) or sum(my_iterator) consumes the entire stream. Any subsequent loops over that specific iterator object will be empty.
:::

nums = [1, 2, 3]
mp = map(lambda x: x*x, nums)

print(list(mp)) # [1, 4, 9] -> This "consumed" the iterator.

# This loop will NOT run because mp is empty now:
for i in mp:
    print(i)


4. Custom Iterator Example

Here is how you build an iterator from scratch by following the protocol.

class PowerOfTwo:
    """Iterator that yields powers of 2 up to a limit."""
    def __init__(self, max_exponent):
        self.max = max_exponent
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.max:
            result = 2 ** self.current
            self.current += 1
            return result
        else:
            raise StopIteration

# Usage
powers = PowerOfTwo(3)
for p in powers:
    print(p) # 1, 2, 4, 8


5. Summary

Iterables are containers (list, set).

Iterators are streams (map, zip, generator).

next() pulls the next value.

StopIteration signals the end.

Memory Efficiency is the primary reason to use them.
'''
