from flask import Flask, render_template, redirect, url_for, abort, flash
from products import Product
from forms import ProductForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"

ITEMS = [
    Product("Coffeepro - Kostaryka El Mango", 0.08, "kg", 246.00),
    Product("Bracia Ziółkowscy - Indonezja Frinsa Estate", 0.25, "kg", 300.00),
    Product("Klaro - Ethiopia Flores", 0.25, "kg", 236.00),
]


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
        ITEMS.append(new_product)
        flash('Product added successfully!', 'success')
        return redirect(url_for('product_list'))
    else:
        print("Form validation failed.")
        print(form.errors)  # Show form errors in the console
    return render_template('product_list.html', items=ITEMS, active_page='products', form=form)


@app.route('/')
def home():
    return render_template('dashboard.html', active_page='dashboard')


if __name__ == "__main__":
    app.run(debug=True)
