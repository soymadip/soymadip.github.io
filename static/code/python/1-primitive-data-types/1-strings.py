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
