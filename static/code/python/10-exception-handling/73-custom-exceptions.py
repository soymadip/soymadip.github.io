# usually we use raise keyword to raise builtin Exceptions
def brew_chai(flavour):
    if flavour not in ["masala", "ginger", "elaichi"]:
        raise ValueError("Unsupported chai flavur...")

    print(f"Brewing {flavour} chai...")


# brew_chai("mint")


#
#
# We can create Custom Exceptions.


# To do this, we have to class inheriting Exception class
class UnknownFlavourError(Exception):
    pass


def brew_chai_2(flavour):
    if flavour not in ["masala", "ginger", "elaichi"]:
        raise UnknownFlavourError("Unsupported chai flavur...")   # we use our custom class/error

    print(f"Brewing {flavour} chai...")


brew_chai_2("mint")
