# ============================================================
# Python Comprehension Exercises
# List | Set | Dict
# ============================================================

from typing import Optional, TypedDict

# ── LIST COMPREHENSIONS ──────────────────────────────────────

# 1. Square all numbers from 1–20.
ex01: list[int] = [num**2 for num in range(1, 21)]

# 2. From a list of words, keep only those longer than 4 characters.
words_ex02: list[str] = ["cat", "elephant", "dog", "python", "owl", "snake"]
ex02: list[str] = [word for word in words_ex02 if len(word) > 4]

# 3. Flatten this nested list into a single list.
nested_ex03: list[list[int]] = [[1, 2], [3, 4], [5, 6]]
ex03: list[int] = [num for lst in nested_ex03 for num in lst]

# 4. From a list of strings, return each string reversed —
#    but only if it is a palindrome.
strings_ex04: list[str] = ["racecar", "hello", "level", "world", "madam", "python"]
ex04: list[str] = [string[::-1] for string in strings_ex04 if string[::-1] == string]

# 5. Generate all (x, y) pairs where x ∈ [1,5], y ∈ [1,5], and x != y.
ex05: list[tuple[int, int]] = [
    (x, y) for x in range(1, 6) for y in range(1, 6) if x != y
]

# NOTE: if we had to give if to 1st comprehension: [(x, y) for x in range(1, 6) if x != 3 for y in range(1, 6)]


# ── SET COMPREHENSIONS ───────────────────────────────────────

# 6. From a sentence string, collect all unique vowels present.
sentence_ex06: str = "the quick brown fox jumps over the lazy dog"
ex06: set[str] = {letter for letter in sentence_ex06 if letter in "aeiou"}

# 7. Given two lists, build a set of values that appear in BOTH
#    — without using & or .intersection().
list_a_ex07: list[int] = [1, 2, 3, 4, 5]
list_b_ex07: list[int] = [3, 4, 5, 6, 7]
ex07: set[int] = {num for num in list_a_ex07 if num in list_b_ex07}

# 8. From a list of words, build a set of their lengths.
words_ex08: list[str] = ["cat", "elephant", "dog", "python", "owl", "snake", "rat"]
ex08: set[int] = {len(word) for word in words_ex08}

# 9. From a list of numbers, build a set of only the prime ones.
# A prime number has exactly two factors — 1 and itself.
# Means nothing between 2 and num-1 can divide it.
numbers_ex09: list[int] = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
ex09: set[int] = {
    num for num in numbers_ex09 if num > 1 and all(num % i != 0 for i in range(2, num))
}


# ── DICT COMPREHENSIONS ──────────────────────────────────────

# 10. From a list of words, map each word → its length.
words_ex10: list[str] = ["cat", "elephant", "dog", "python"]
ex10: dict[str, int] = {word: len(word) for word in words_ex10}

# 11. Invert a dictionary: {'a': 1, 'b': 2} → {1: 'a', 2: 'b'}.
original_ex11: dict[str, int] = {"a": 1, "b": 2, "c": 3}
ex11: dict[int, str] = {val: key for key, val in original_ex11.items()}

# 12. From two lists (keys, values), zip into a dict —
#     but only include pairs where the value is truthy.
keys_ex12: list[str] = ["a", "b", "c", "d"]
values_ex12: list[Optional[int]] = [1, 0, 3, None]
ex12: dict[str, int] = {
    letter: value for letter, value in zip(keys_ex12, values_ex12) if value
}

# 13. Given a dict of name → score, keep only scores above 70
#     and scale each by 1.1.
scores_ex13: dict[str, int] = {
    "alice": 85,
    "bob": 60,
    "charlie": 72,
    "diana": 55,
    "eve": 90,
}
ex13: dict[str, float] = {
    name: score * 1.1 for name, score in scores_ex13.items() if score > 70
}

# 14. Group characters of a string by vowel / consonant.
#     Expected shape: {'vowel': {...}, 'consonant': {...}}
text_ex14: str = "comprehension"
vowels_ex14: set[str] = set("aeiou")
ex14: dict[str, set[str]] = {
    "vowel": {letter for letter in text_ex14 if letter in vowels_ex14},
    "consonant": {letter for letter in text_ex14 if letter not in vowels_ex14},
}


# ── MIXED / HARDER ───────────────────────────────────────────


# 15. Given a list of dicts, build a dict of name → age.
class Person(TypedDict):
    name: str
    age: int


people_ex15: list[Person] = [
    {"name": "alice", "age": 25},
    {"name": "bob", "age": 30},
    {"name": "carol", "age": 22},
]
ex15: dict[str, int] = {person["name"]: person["age"] for person in people_ex15}

# 16. Build a dict where keys are numbers 1–10 and values are
#     their factor lists  →  {1: [1], 2: [1,2], 6: [1,2,3,6], ...}
ex16: dict[int, list[int]] = {
    num: [i for i in range(1, num + 1) if num % i == 0] for num in range(1, 11)
}

# 17. Flatten a nested list of numbers, keep only unique evens —
#     produce a set, in one expression.
nested_ex17: list[list[int]] = [[1, 2, 3], [4, 5, 6], [2, 4, 8], [7, 9, 10]]
ex17: set[int] = {num for lst in nested_ex17 for num in lst if num % 2 == 0}
