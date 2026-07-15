# Strings


# Reeverse a string
string = "Hello"
rstr = string[::-1]


# String concatenation


name: str = "Soumadip"
title: str = "Das"

full_name = name + title  # there is no space added

print(full_name)  # SoumadipDas


# Inplicit Concatination
# Whenever Python sees string literals enclosed in parentheses without commas between them, it automatically glues them together.

msg = (
    "Hello "
    "World"
)  # note that there are no commas between the entries, unless they will become tuple

# What Python sees
msg = "Hello World"


# MultiLine strings
multi: str = """Hi i am google
I am a total shit

Just do some fucking
"""

print("-------")
print(multi)


# ------- Unpacking -------------

x, y = ("googpe", "shit")

# we can use any iterable
x, y = ["googpe", "shit"]

# ----------------- String Methods -----------------

# center()
# It takes a string and pads it with a character of your choice on both sides so that the total text block reaches a specific width

string = "google"

# by default only length is given, it pads with whitespace
print(
    string.center(50)  # output: '                      google                      '
)

# we can give custom character:
print(string.center(20, "-"))  # output: '-------google-------'


# Comparing String

str1 = "google"
str2 = "Google"


print(str1.__str__, str2.__str__)

# has same content string?
if str2.lower() == str1:  # comparison is case-sensitive so needs to be lowered
    print("same but neeeds to be lowered")


# which one is bigger?
print(str1 > str2)  # True

# Why? Python compares each letter in a string from left to right.
# And it uses unicode values.
# In unicode, UpperCase letters have LOWER numbers than lowercase. So...
# 'N' (71) is actually smaller than 'a' (103).


# ----------------------------------------------------

# split()
# This method returns a list of substrings split with given delimitatior

print("Google shit".split())  # by default uses space to dplit

print("i_am".split("_"))  # splits using _ now

# we can directly assign with unpacking
x, y = "i_am_2".split("_", 1)  # max 1 split, default all.


# rplit()
# same as split() but starts spliting from right side.
# Use for cases like extension extraction.


# --------------------------------------------------

# strip()
# this method strips leading & trailing whitespaces, newline(\n), tab(\t), carriage return(\r) characters from string.
# Or any given character
#
# strip() TREATES THE GIVEN CHARACTERS AS SEPARATE, SO DONT USE THIS FOR STRIPPING ENTIRE WORD

string = " google "

print(f"'{string.strip()}'")  #  strips space.  output: 'google'


# we can also give which char to strip

string = "-google-"

print(f"'{string.strip('-')}'")  #  strips -.  output: 'google'


# There are more variants:
#
# lstrip() - Removes whitespaces/given char from beginning
# rstrip() - Removes whitespaces/given char from end
#


# To remove entire word from beginning/end use these:
#
# removeprefix('word') - removes 'word' from BEGINNING of string (prefix)
# removesuffix('word') - removes 'word' from ENDING of string (suffix)


# so what if we wanna remove a word all places in a string?
#
# use str.replace("word", '')
