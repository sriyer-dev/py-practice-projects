from flask import Flask, request, render_template, make_response, redirect, url_for
from todo.model.item import Item
from todo.db.db import DB
import datetime

app = Flask(__name__)
db = DB.initialize()


@app.route('/items')
def get_all_items():
    return Item.find_all()


@app.route('/items/<string:_id>')
def get_item(_id):
    return Item.find_one(_id)


@app.route('/items', methods=['POST'])
def create_item():
    # Use request.json to test with postman. In actual E2E code, we have to use request.form instead
    # return Item(**request.json).save()
    item = Item(request.form['title'], request.form['target'], request.form['description'])
    item.save()
    return redirect(url_for('home'))


@app.route('/items/<string:itemid>', methods=['PUT', 'POST'])
def update_item(itemid):
    # Use request.json to test with postman. In actual E2E code, we have to use request.form instead
    # return Item.update(request.json)
    item = Item.find_one({'_id': itemid})
    # item.target_date = request.form['target']
    item['description'] = request.form['description']
  # item['status'] = request.form['status']
    item['title'] = request.form['title']
    Item.update(item)
    return redirect(url_for('home'))


@app.route('/')
@app.route('/home')
def home():
    items = get_all_items()['items']
    for item in items:
        item['target_date'] = item['target_date'].strftime('%d/%m/%Y')
    return render_template('home.html', user='xyz', items=items)


@app.route('/items/new')
def new_item_page():
    return render_template('new_item.html')


@app.route('/items/<string:itemid>/update')
def update_item_page(itemid):
    item = get_item(itemid)
    item['target_date'] = item['target_date'].strftime('%d/%m/%Y')
    item['create_date'] = item['create_date'].strftime('%d/%m/%Y')
    return render_template('update_item.html', item=item)


app.run()
