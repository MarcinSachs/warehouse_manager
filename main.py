# items format [{name: x, quantity: i, unit: y, unit_price: j}]
items = [
    {"name": "Coffeepro - Kostaryka El Mango",
        "quantity": 0.08, "unit": "kg", "unit_price": 246.00},
    {"name": "Bracia Ziółkowscy - Indonezja Frinsa Estate",
        "quantity": 0.25, "unit": "kg", "unit_price": 300.00},
    {"name": "Klaro - Ethiopia Flores", "quantity": 0.25,
        "unit": "kg", "unit_price": 236.00},
]


def get_column_width(items, key, extra=2):
    return max(len(str(item[key])) for item in items) + extra


def get_items():
    name_width = get_column_width(items, "name", 2)  # dynamically form items
    quantity_width = 10  # fixed for header
    unit_width = 6  # fixed for header
    unit_price_width = 18  # fixed for header

    header = f"{'Name':<{name_width}}{'Quantity':<{quantity_width}}{'Unit':<{unit_width}}{'Unit Price (PLN)':<{unit_price_width}}"
    print(header)
    print('-' * (name_width + quantity_width + unit_width + unit_price_width))
    for item in items:
        print(
            f"{item['name']:<{name_width}}{str(item['quantity']):<{quantity_width}}{item['unit']:<{unit_width}}{str(item['unit_price']):<{unit_price_width}}"
        )


def show_menu():
    response = get_response_from_user("What would you like to do? ")
    run_command(response)


def get_response_from_user(message):
    return input(f"{message}")


def run_command(command):
    if command == "exit":
        print("Exiting... Bye!")
        exit(0)
    elif command == "show":
        get_items()


if __name__ == '__main__':
    while True:
        show_menu()
