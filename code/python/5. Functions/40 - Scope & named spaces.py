# Local - inside the function
# Enclosing from outer functin if nested
# Global - top level script
# Built In


def serve_chai():
    chay_type = "masalla chay"  # local scope (just inside method)

    print(f"Inside function: {chay_type}")


chay_type = "lemon"  # global scope
serve_chai()
print(f"outside function: {chay_type}")


def chai_counter():
    chay_order = "lemon"  # Enclosing scope

    def print_order():
        chay_order = "ginger"
        print(f"Inner function: {chay_order}")

    print_order()
    print(f"outer function: {chay_order}")


chay_order = "tulsi"  # Global
chai_counter()
print(f"Global: {chay_order}")
