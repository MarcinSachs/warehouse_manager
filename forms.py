from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField, HiddenField


class ProductForm(FlaskForm):
    name = StringField('Name')
    quantity = DecimalField('Quantity')
    unit = StringField('Unit')
    unit_price = DecimalField('Unit Price')
    submit = SubmitField('Add Product')


class ProductSaleForm(FlaskForm):
    quantity = DecimalField('Quantity')
    product_name = HiddenField()
    submit = SubmitField('Sell Product')
