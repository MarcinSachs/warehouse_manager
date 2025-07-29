from flask import Flask, render_template, redirect, url_for, abort, flash, Response, send_file
from products import Product
from forms import ProductForm, ProductSaleForm
from decimal import Decimal
import csv
import io

app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"

ITEMS = {
    "Coffeepro - Kostaryka El Mango": Product("Coffeepro - Kostaryka El Mango", 0.08, "kg", 246.00),
    "Bracia Ziółkowscy - Indonezja Frinsa Estate": Product("Bracia Ziółkowscy - Indonezja Frinsa Estate", 0.25, "kg", 300.00),
    "Klaro - Ethiopia Flores": Product("Klaro - Ethiopia Flores", 0.25, "kg", 236.00),
}


SOLD_ITEMS = []


@app.route('/products', methods=['GET', 'POST'])
def product_list():
    form = ProductForm()
    if form.validate_on_submit():
        new_product = Product(
            name=form.name.data,
            quantity=form.quantity.data,
            unit=form.unit.data,
            unit_price=form.unit_price.data
        )
        ITEMS[new_product.name] = new_product
        flash('Product added successfully!', 'success')
        return redirect(url_for('product_list'))
    else:
        print("Form validation failed.")
        print(form.errors)  # Show form errors in the console
    return render_template('product_list.html', items=ITEMS, active_page='products', form=form)


@app.route('/')
def home():
    return render_template('dashboard.html', active_page='dashboard')


@app.route('/sell_product/<product_name>', methods=['GET', 'POST'])
def sell_product(product_name):
    form = ProductSaleForm()
    form.product_name.data = product_name
    # Pobierz produkt ze słownika ITEMS po nazwie z URL
    product = ITEMS.get(product_name)
    if product is None:
        abort(404)  # Produkt nie istnieje

    if form.validate_on_submit():
        quantity_to_sell = form.quantity.data
        # Porownanie Decimal z Decimal
        if quantity_to_sell > Decimal(str(product.quantity)):
            flash("Not enough products in stock!", "error")
        else:
            # Konwersja na float przed odjęciem
            product.quantity -= float(quantity_to_sell)
            SOLD_ITEMS.append({"name": product.name, "quantity": quantity_to_sell, "unit": product.unit,
                              "unit_price": product.unit_price})  # dodawanie do listy sprzedanych
            flash(f"Sold {quantity_to_sell} of {product.name}!", "success")
            return redirect(url_for('product_list'))

    return render_template('sell_product.html', form=form, product=product)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/load_products')
def load_products():
    # Load products from a CSV file
    try:
        with open('magazyn.csv', 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                product = Product(
                    name=row['name'],
                    quantity=float(row['quantity']),
                    unit=row['unit'],
                    unit_price=float(row['unit_price'])
                )
                ITEMS[product.name] = product
        flash("Products loaded successfully!", "success")
    except FileNotFoundError:
        flash("File not found. Please upload the CSV file.", "error")
    return redirect(url_for('product_list'))


@app.route('/export_products')
def export_products():
    with open('magazyn.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['name', 'quantity', 'unit', 'unit_price']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for product in ITEMS.values():
            writer.writerow({
                'name': product.name,
                'quantity': product.quantity,
                'unit': product.unit,
                'unit_price': product.unit_price
            })
    flash("Products exported successfully!", "success")
    return redirect(url_for('product_list'))


if __name__ == "__main__":
    app.run(debug=True)
