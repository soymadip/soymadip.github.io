# create a alias
type RGb = tuple[int, int, int]


def color(color: RGb):
    print(color)


# What if someone passes HSL instad of RGB

color((255, 0, 0))  # valid type with rgb
color((0, 100, 50))  # valid type with hsl

# Why? because type checker only checks for type int.


# --------------------- New Types -----------------------

from typing import NewType

RGB = NewType("RGB", tuple[int, int, int])
HSL = NewType("HSL", tuple[int, int, int])


type User = dict[str, int | str | float | RGB | HSL]


def crt_usr(name: str, age: int, fav_color: RGB | HSL) -> User:
    return {
        "name": name,
        "age": age,
        "fav_color": fav_color,
    }


# Now we have to explicitly pass a `RGB` or `HSL` instance
_ = crt_usr("soymadip", 4, RGB((255, 0, 0)))

_ = crt_usr("soymadip", 4, HSL((0, 4, 50)))
