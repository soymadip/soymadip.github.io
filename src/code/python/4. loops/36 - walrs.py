# walrus

x = 5  # statement, doesn't return a value
3 + 3  # Expression, returns value


## without walrus operator
remainder = 13 % 5
if remainder:
    print("not devisible by 5")


# with walrus
if remainder := 13 % 5:
    print("not divisible by 5")


class config:
    server_username = ""

    def write_output(self, name: str) -> type[str]:
        return str


dsd_config = config()
plugin_utils = config()


# without walrus
def set_server_username():
    username = os.environ.get("DO_DJANGO_USER")
    if username:
        # Use this custom username.
        dsd_config.server_username = username
        plugin_utils.write_output(f"  username: {username}")
        return

    # No custom username. Try to connect with default username.


# with walrus operator
def set_server_username2():
    if username := os.environ.get("DO_DJANGO_USER"):
        # Use this custom username.
        dsd_config.server_username = username
        plugin_utils.write_output(f"  username: {username}")
        return

    # No custom username. Try to connect with default username.


flavours: list[str] = ["mint", "lemon", "mirch"]

while user_flav := input("choose your flavour: ").strip().lower():
    print(f"sorry we dont have {user_flav}")

print(f"you choose: {user_flav}")
