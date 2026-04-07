def update_order():
    chai_type = "Elaichi"

    def kitchen():
        nonlocal chai_type  # wanna access parent level thing (from inside to outside function), will give error if the one level parent method doesnt have defined
        chai_type = "kesar"

    kitchen()
    print(f"After kitchen update: {chai_type}")


# global scope

chai_type = "plain"


def front_desk():
    def kitchen():
        global chai_type  # access global one

        chai_type = "Irani"

    kitchen()


front_desk()
print(f"Final global chai: {chai_type}")  # Irani

# be cautious using global keyword
# global keyword can break global var which can be used by someones code.
