"""
static methods are useful when we want utility functions to be grouped with our classes without depending on  instances

Use a static method when the method:
 - Doesn't need access to instance data
 - Doesn't need access to class data
 - Logically belongs to the class

"""


class ChaiUtils:
    def clean_ingredients(text: str):
        return [item.strip() for item in text.split(",")]


raw = "water , milk, ginter , honey"


obj = ChaiUtils()
print(obj.clean_ingredients(raw))  # will through error about not enough arguments given

print(ChaiUtils.clean_ingredients(raw))  # This works but is dirty


#
# We use @staticmethod decorator to declare this as static method, dont need 'self'


class ChaiUtils_:
    @staticmethod
    def clean_ingredients(text: str):
        return [item.strip() for item in text.split(",")]


raw = "water , milk, ginter , honey"

obj = ChaiUtils_()

print(obj.clean_ingredients(raw))
