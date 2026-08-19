def func_name(flavor="masalla") -> str:
    """The Example function's docstring
    Returns the flavor of the function.
    """
    return flavor


print(func_name.__doc__)  # Dunder attribute, returns the docstring
print(func_name.__name__)  # Dunder attribute, returns the function name


help(func_name)  # help returns the docstring and signature


# documenting your code
def gen_bil(chai: int = 0, samosa: int = 0) -> tuple[int, str]:
    """
    calculate total bill for chai & samosa.

    :param chai: Number of chai cups (10/cup)
    :param samosa: Number of samosa (15/per)
    :return (total amount, thanks message)
    """

    total: int = chai * 10 + samosa * 15
    return total, "Thanks for eating!"


ss = gen_bil(5, 90)
