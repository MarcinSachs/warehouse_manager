from flask import Flask, render_template
from products import Product

app = Flask(__name__)

ITEMS = [
    Product("Coffeepro - Kostaryka El Mango", 0.08, "kg", 246.00),
    Product("Bracia Ziółkowscy - Indonezja Frinsa Estate", 0.25, "kg", 300.00),
    Product("Klaro - Ethiopia Flores", 0.25, "kg", 236.00),
]


@app.route('/products')
def product_list():
    return render_template('product_list.html', items=ITEMS, active_page='products')


@app.route('/')
def home():
    return render_template('dashboard.html', active_page='dashboard')


if __name__ == "__main__":
    app.run(debug=True)
