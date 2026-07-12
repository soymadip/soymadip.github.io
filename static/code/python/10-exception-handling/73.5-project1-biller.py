class UnknownChaiError(Exception):
    pass


class OutOfStockError(Exception):
    pass


class Shop:
    def __init__(self, name: str) -> None:
        self.name = name
        self._stock: dict[str, int] = {}

    @property
    def stock(self) -> dict[str, int]:
        return self._stock  # caution, this returns direct reference to the _stock dict, allowing anyone to change, if not intendet, use .copy() to pass a copy

    @stock.setter
    def stock(self, stock: dict[str, int]) -> None:
        self._stock = stock

    def show_menu(self) -> None:
        print(f"--- {self.name} Menu ---")
        for i, item in enumerate(self._stock, start=1):
            print(f" {i}. {item.capitalize()} (Stock: {self._stock[item]})")

    def order(self, flavour: str, cups: int) -> None:
        if not isinstance(cups, int) or cups <= 0:
            raise ValueError("Cups must be a positive integer!")

        if flavour not in self._stock:
            raise UnknownChaiError(f"Sorry, flavor '{flavour}' not found!")

        if cups > self._stock[flavour]:
            raise OutOfStockError(
                f"Sorry, only {self._stock[flavour]} cup(s) of {flavour} available!"
            )

        # Process the Order
        print(f"Preparing {cups} cup(s) of {flavour}....")

        self._stock[flavour] -= cups
        print(f"Here is your {flavour} Chai. Enjoy Your Tea!\n")


chai_shop = Shop("chai")
chai_shop.stock = {"masala": 20, "adrak": 30, "ginger": 4}

print(chai_shop.stock)

chai_shop.stock["masala"] += 5 # This doesn't actually call the setter. getter is called -> it gives reference to dict _stock, then python evaluates like dict updating.

chai_shop.show_menu()
chai_shop.order("masala", 70)
