def print_order(name, chai_type):  # parameter
    print(f"{name} orderded {chai_type} chai!")


print_order("Aman", "masala")  # arguments
print_order("Hitesh", "Ginger")
print_order("Jia", "Tulsi")


def fetch_sales():
    print("Fetching the sales data")


def filter_valid_sales():
    print("Filtering valid sales data")


def summarize_data():
    print("Summarizing sales data")


def generate_report():
    fetch_sales()
    filter_valid_sales()
    summarize_data()
    print("Report is ready")


generate_report()


# Readability
def calculate_bill(cups, price_per_cup):
    return cups * price_per_cup


my_bill = calculate_bill(2, 10)  # just stores, not print.
print(calculate_bill(4, 10))  # Print directly


# Traceability
def add_vat(price, vat_price):
    return price * (100 + vat_price) / 100


orders = [100, 200, 150]


for price in orders:
    print(add_vat(price, 10))
