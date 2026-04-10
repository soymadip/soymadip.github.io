"""Order Invoice Generator

You are building an Order Invoice Generator system for a restaurant. The function should be versatile enough to accept a customer's name, a flexible number of ordered items, and a set of dynamic extra charges (like tax, service charge, etc.).

Your Tasks:

    Function: generate_invoice(customer_name: str, *items: str, **charges: float) -> str

        customer_name: optional; defaults to "Guest" if not provided.
        items: an arbitrary number of strings representing food items ordered.
        *charges: keyword arguments representing different charges like tax=50.0, service=20.0, delivery=15.0, etc.

    Invoice Structure:

        Header: Invoice for <customer_name>

        Items Section (only if items are provided):
            Line: Items:
            Each item on its own line with format: - <item_name>

        Charges Section (only if charges are provided):
            Line: Charges:
            Each charge on its own line with format: <Charge_name>: <amount>

        At the end, the display Total Amount Due: ₹<total>.

    Important Notes:

        Sum only the values from *charges for total.

        Items are only for listing, not costing.

        Charge names should be capitalized (e.g., tax becomes Tax)

        Use `\n` to join all lines into a single string

Examples:

    # Example 1: Full invoice with items and charges
    generate_invoice("Amit", "Burger", "Fries", tax=50.0, service=20.0)
    # Output:
    # Invoice for Amit:
    # Items:
    # - Burger
    # - Fries
    # Charges:
    # Tax: 50.0
    # Service: 20.0
    # Total Amount Due: 70.0

    # Example 2: Only charges, no items
    generate_invoice("Riya", tax=30.0)
    # Output:
    # Invoice for Riya:
    # Charges:
    # Tax: 30.0
    # Total Amount Due: 30.0

    # Example 3: Default customer, no items or charges
    generate_invoice()
    # Output:
    # Invoice for Guest:
    # Total Amount Due: 0.0

    # Example 4: Only items, no charges
    generate_invoice("John", "Pizza", "Coke")
    # Output:
    # Invoice for John:
    # Items:
    # - Pizza
    # - Coke
    # Total Amount Due: 0.0
"""
