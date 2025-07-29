from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField


class ProductForm(FlaskForm):
    name = StringField('Name')
    quantity = DecimalField('Quantity')
    unit = StringField('Unit')
    unit_price = DecimalField('Unit Price')
    submit = SubmitField('Add Product')
