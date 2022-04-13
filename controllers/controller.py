from flask import render_template
from app import app
from models.order_list import orders

@app.route('/tasks')
def index():
    return render_template('index.html',
    title="PokeMart", order_list=orders)

# @app.route('/tasks/order_list/0')
# def index():
#     return render_template('index.html',
#     title="Charles Avery", order_list=orders)
@app.route('/tasks/<index>')
def single_order(index):
  chosen_order = orders[int(index)]
  
  return render_template('order.html', order_list=chosen_order)