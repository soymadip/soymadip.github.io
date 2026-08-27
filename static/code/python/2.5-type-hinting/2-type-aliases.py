# ------------------- Type Aliases ---------------------

# Sometimes, types can get quite long and repetitive
def create_usr(name: str, age: int | None = None) -> dict[str, int | str | None]:
    return {"name": name, "age": age}


# So we can create a type alias for the dictionary
type User = dict[str, int | str | None]


def create_user(name: str, age: int | None = None) -> User:
    return {"name": name, "age": age}


# Let's create a practical example

type RGB = tuple[int, int, int]
type Color = RGB | str

type Usr = dict[str, int | str | Color | None]


def crt_usr(
    name: str,
    age: int,
    middle_name: str | None = None,
    fav_color: Color | None = None,
) -> Usr:
    return {
        "email": f"{name}@example.com",
        "name": name,
        "age": age,
        "middle_name": middle_name,
        "fav_color": fav_color,
    }


usr1 = crt_usr("soymadip", 12, fav_color=(102, 120, 255))
