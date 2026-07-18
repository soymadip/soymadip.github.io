"""
JSON = JavaScript Object Notation

We work with json in python using 'json' library

video: https://www.youtube.com/watch?v=-51jxlQaxyA
"""

# Always use r before triple quotes in json strings,
# This helps escaping the escape sequences
json_str = r"""{
  "bool": null,
  "key": "value",
  "keys": "must always be enclosed in double quotes",
  "strings": "\"escaping\".",
  "numbers": 0,
  "big number": 1.2e+100,
  "array": [1,2,3,"go"]
}
"""

import json  # noqa: E402

# We use json.loads() method to parse and convert json string to python dictionary
data = None

try:
    data = json.loads(json_str)  # we parse the json string
except Exception as e:
    print(f"Error: {e}")
else:
    print(data)
    print()
    print(data["strings"])
    print(data["array"])


# use json.dumps() to convert dictionary to json string
json_data = json.dumps(data)


# Python to json conversion table:
#
# | Python  |	JSON  |
# | ------- | ------- |
# | dict	|  Object |
# | list	|  Array  |
# | tuple	|  Array  |
# | str	    |  String |
# | int	    |  Number |
# | float	|  Number |
# | True	|  true   |
# | False	|  false  |
# | None	|  null   |

print()
print(json_data)

# Formatting the output
print(
    json.dumps(data, indent=2, sort_keys=True)  # indent spaces, pretty json, sort keys
)

# --------------------------------
# Handling json file

# Reading and Loading json from a file/stream
try:
    with open("data.json", "r") as json_file:
        data = json.load(json_file)  # no s in json.load()..
except Exception as e:
    print(e)

print()
print(data)


# Writing back to file/stream
try:
    with open("ss.json", "x") as file:
        json.dump(data, file)
except Exception as e:
    print(e)
