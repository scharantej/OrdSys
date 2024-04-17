
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class OrderForm(FlaskForm):
    customer_name = StringField('Customer Name')
    product_name = StringField('Product Name')
    quantity = IntegerField('Quantity')
    submit = SubmitField('Submit')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key'

@app.route('/')
def index():
    form = OrderForm()
    return render_template('index.html', form=form)

@app.route('/order', methods=['POST'])
def order():
    form = OrderForm()
    if form.validate_on_submit():
        # Save the order details to a database or other persistent storage
        # ...
        return redirect(url_for('confirmation'))
    return render_template('index.html', form=form)

@app.route('/confirmation')
def confirmation():
    return render_template('confirmation.html')

if __name__ == '__main__':
    app.run(debug=True)
