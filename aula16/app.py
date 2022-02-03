from itertools import product
import os

from datetime import datetime
from unicodedata import category, name
from flask import Flask, jsonify, abort, request, render_template, redirect, session, flash, url_for
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
api = Api(app)

db = SQLAlchemy(app)

#CREATE DATABASE 'restaurante'

@app.route('/')
def home():
    return render_template('index.html', titulo = 'Restaurante') 

@app.route('/new')
def new():
    if 'user_logon' not in session or session ['user_logon'] == None:
        return redirect(url_for('home', next = url_for('new')))
    return render_template('newplate.html', titulo = 'All Food Restaurant New Order') 


@app.route('/createorder', methods=['POST'])
def create_order():
    plate = request.form['plate']
    name = request.form['name']
    category = request.form['category']
    price = request.form['price']
    order = Product(plate, name, category, price)
    list.append(order)
    return redirect(url_for('home'))

# class Choices(enum.Enum):
#     TAKE_AWAY = 'Takeaway'
#     TO_HAVE_HERE = 'Tohavehere'

class Client(db.Model, SerializerMixin):
    __tablename__ = 'client'
    serialize_rules = ('product.client.product')
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50),nullable=False)
    mobile = db.Column(db.String(14))
    address = db.Column(db.String(50))

    order = db.relationship('ProductOrder', back_populates='client', lazy=True)

    def __repr__(self):
        return '<Client %r>' % self.name

class Product(db.Model, SerializerMixin):
    __tablename__ = 'product'
    plate = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float(2), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey(
        'category.id', ondelete="CASCADE"), nullable=False)
    category = db.relationship(
        'Category', back_populates='products', lazy=True)

    def __repr__(self):
        return '<Product %r>' % self.name

class Category(db.Model, SerializerMixin):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    products = db.relationship(
        'Product',
        back_populates='category',
        cascade='all, delete, delete-orphan',
        single_parent=True,
        lazy=True,
        passive_deletes=True,
        order_by='desc(Product.name)'
    )

    def __repr__(self):
        return '<Category %r>' % self.name


class ProductOrder(db.Model, SerializerMixin):
   __tablename__ = 'product_order'
   product_id = db.Column(db.ForeignKey('product.plate'), primary_key=True)
   order_id = db.Column(db.ForeignKey('category.id'), primary_key=True)
   quantity = db.Column(db.Integer, nullable=False)

class Order(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, nullable=False, unique=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    # products = db.relationship("ProductOrder", backref="orders")

    def __repr__(self):
        return '<Order %r>' % self.name

@app.before_first_request
def create_db():
    # Delete database file if it exists currently
    if os.path.exists("database.db"):
        os.remove("database.db")
    db.create_all()

@app.route('/product', methods=['GET'])
def list_prod():
    data_product = Product.query.all()
    return jsonify(
        {"product": [data_product_.to_dict() for data_product_ in data_product]}
    )

@app.route('/product', methods=['POST'])
def create_prod():
    data_prod = request.json

    prod_plate = data_prod['plate']
    prod_name = data_prod['name']
    prod_price = data_prod['price']
    prod_category_id = data_prod['category_id']

    product = Product(plate=prod_plate, name=prod_name, price=prod_price, category_id=prod_category_id)
    db.session.add(product)
    db.session.commit()

    return jsonify({"success": True, "response": "Product added"})

@app.route('/category', methods=['GET'])
def list_category():
    category = Category.query.all()
    return jsonify(
        {"category": [category_.to_dict() for category_ in category]}
    )

@app.route('/category', methods=['POST'])
def create_cat():
    data_categ = request.json
    db.session.add(Category(name=data_categ['name']))
    db.session.commit()

    return jsonify({"success": True, "response": "Product added"})


class CategoryResource(Resource):
    def get(self):
        categories = Category.query.all() or abort(404, description="Resource not found")
        return jsonify(
            {"Categories": [category.to_dict() for category in categories]})
    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=ascii,help='recurso não enviado, por favor mande um nome')
        args = parser.parse_args()

        category = Category(**args)
        db.session.add(category)
        db.session.commit()

        return jsonify({"success": True, "response": "Category added"})

class ProductResource(Resource):
    def get(self):
        products = Product.query.all() or abort(404, description="Resource not found")
        return jsonify(
            {"products": [product.to_dict() for product in products]}
        )

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=ascii,help='recurso não enviado, por favor mande um nome')
        parser.add_argument('price', type=float)
        parser.add_argument('category_id', type=int)

        args = parser.parse_args()

        plate = Product(**args)
        db.session.add(plate)
        db.session.commit()

        return jsonify({"success": True, "response": "Plate added"})


    def put(self):
        pass

    def delete(self):
        pass

class OrderResource(Resource):
    def get(self):
        orders = Order.query.all() or abort(404, description="Resource not found")
        return jsonify(
            {"Order": [order.to_dict() for order in orders]}
        )

class ProductOrderResource(Resource):
    def get(self, product_id):
        product = Product.query.filter_by(id=product_id).first() or abort(
            404, description=f"Resource id {product_id} not found")
        return jsonify(product.to_dict())


# api.add_resource(ProductResource, "/product/")
# api.add_resource(ProductItemResource, "/product/<int:product_id>")
api.add_resource(CategoryResource,"/Category")
api.add_resource(ProductResource,"/Product")
api.add_resource(OrderResource,"/Order")
api.add_resource(ProductOrderResource,"/product/<int:product_id>")


@app.route('/cadastra')
def registerplate():
    categories = Category.query.all() or abort(404, description="Resource not found")
    return render_template("newplate.html",categories=categories)


if __name__ == '__main__':
    app.run(debug=True)


