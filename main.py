import csv
import sys
# items format [{name: x, quantity: i, unit: y, unit_price: j}]
items = [
    {"name": "Coffeepro - Kostaryka El Mango",
        "quantity": 0.08, "unit": "kg", "unit_price": 246.00},
    {"name": "Bracia Ziółkowscy - Indonezja Frinsa Estate",
        "quantity": 0.25, "unit": "kg", "unit_price": 300.00},
    {"name": "Klaro - Ethiopia Flores", "quantity": 0.25,
        "unit": "kg", "unit_price": 236.00},
]
sold_items = []


def get_column_width(items, key, extra=2):
    return max(len(str(item[key])) for item in items) + extra


def get_response_from_user(message):
    return input(f"{message}")


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


def get_sold_items():
    name_width = get_column_width(items, "name", 2)  # dynamically form items
    quantity_width = 10  # fixed for header
    unit_width = 6  # fixed for header
    unit_price_width = 18  # fixed for header

    header = f"{'Name':<{name_width}}{'Quantity':<{quantity_width}}{'Unit':<{unit_width}}{'Unit Price (PLN)':<{unit_price_width}}"
    print(header)
    print('-' * (name_width + quantity_width + unit_width + unit_price_width))
    for item in sold_items:
        print(
            f"{item['name']:<{name_width}}{str(item['quantity']):<{quantity_width}}{item['unit']:<{unit_width}}{str(item['unit_price']):<{unit_price_width}}"
        )


def add_item(name, unit_name, quantity, unit_price):
    new_item = {"name": name, "quantity": quantity,
                "unit": unit_name, "unit_price": unit_price}
    items.append(new_item)


def sell_item(name, quantity):
    item = get_item_by_name(name)
    item["quantity"] = item["quantity"] - quantity


def show_menu():
    response = get_response_from_user("What would you like to do? ")
    run_command(response)


def get_item_by_name(name):
    for item in items:
        if item["name"] == name:
            return item


def get_costs():
    return sum(item["quantity"] * item["unit_price"] for item in items)


def get_income():
    return sum(sold_item["quantity"] * sold_item["unit_price"] for sold_item in sold_items)


def show_revenue():
    income = get_income()
    costs = get_costs()
    print("Revenue breakdown (PLN)")
    print(f"Income: {round(income, 2)}")
    print(f"Costs: {round(costs, 2)}")
    print("---------------------")
    print(f"Revenue: {income - costs}")


def export_items_to_csv():
    with open('magazyn.csv', 'w', newline='', encoding="utf8") as csvfile:
        fieldnames = ['name', 'quantity', 'unit', "unit_price"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for item in items:
            writer.writerow(item)


def export_sales_to_csv():
    with open('sales.csv', 'w', newline='', encoding="utf8") as csvfile:
        fieldnames = ['name', 'quantity', 'unit', "unit_price"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for sold_item in sold_items:
            writer.writerow(sold_item)


def load_items_from_csv(path_to_csv_file='magazyn.csv'):
    items.clear()
    with open(path_to_csv_file, 'r', newline='', encoding="utf8") as csvfile:
        fieldnames = ['name', 'quantity', 'unit', "unit_price"]
        reader = csv.DictReader(csvfile, fieldnames=fieldnames)
        for row in reader:
            items.append(row)
    print("Successfully loaded data from magazyn.csv")


def run_command(command):
    if command == "exit":
        print("Exiting... Bye!")
        exit(0)
    elif command == "show":
        get_items()
    elif command == "add":
        print("Adding to warehouse...")
        item_name = ""
        item_quantity = 0
        item_unit_of_measure = ""
        item_price = 0
        while item_name == "":
            item_name = get_response_from_user("Item name: ")
        while item_quantity == 0:
            item_quantity = float(get_response_from_user("Item quantity: "))
        while item_unit_of_measure == "":
            item_unit_of_measure = get_response_from_user(
                "Item unit of measure: ")
        while item_price == 0:
            item_price = float(get_response_from_user("Item price in PLN: "))
        add_item(item_name, item_unit_of_measure, item_quantity, item_price)
        print("Successfully added to warehouse. Current status: ")
        get_items()
    elif command == "sell":
        item_name = ""
        item_quantity = 0
        while item_name == "":
            item_name = get_response_from_user("Item name: ")
        while item_quantity == 0:
            item_quantity = float(get_response_from_user("Quantity to sell: "))
        sell_item(item_name, item_quantity)
        item_unit_of_measure = get_item_by_name(item_name)["unit"]
        sold_items.append(get_item_by_name(item_name))
        print(
            f"Successfully sold {item_quantity} {item_unit_of_measure} of {item_name}. Current status: ")
        get_items()
    elif command == "show_revenue":
        show_revenue()
    elif command == "save":
        export_items_to_csv()
        export_sales_to_csv()
        print("Successfully exported data to magazyn.csv and sales.csv.")
    elif command == "load":
        load_items_from_csv()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        load_items_from_csv(sys.argv[1])
    while True:
        show_menu()
