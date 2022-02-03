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

@app.route('/inicio')
def inicio():
    return render_template('lista.html', titulo = 'Restaurante') 

app.run()

class Plate(db.Model, SerializerMixin):
    __tablename__ = 'plate'
    product = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float(2), nullable=False)
    category= db.Column(db.Integer, db.ForeignKey(
        'category', ondelete="CASCADE"), nullable=False)
    # category = db.relationship(
    #     'Category', back_populates='products', lazy=True)

    def __repr__(self):
        return '<Plate %r>' % self.name

class Category(db.Model, SerializerMixin):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    products = db.relationship(
        'Plate',
        back_populates='category',
        cascade='all, delete, delete-orphan',
        single_parent=True,
        lazy=True,
        passive_deletes=True,
        order_by='desc(Plate.product)'
    )

    def __repr__(self):
        return '<Category %r>' % self.name

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

@app.route('/new', methods=['GET'])
def list_prod():
    data_product = Plate.query.all()
    return jsonify(
        {"plate": [data_product_.to_dict() for data_product_ in data_product]}
    )

@app.route('/new', methods=['POST'])
def create_plate():
    data_plate = request.json

    prod_plate = data_plate['plate']
    prod_price = data_plate['price']
    prod_category_id = data_plate['category_id']

    product = Plate(plate=prod_plate, price=prod_price, category_id=prod_category_id)
    db.session.add(product)
    db.session.commit()

    return jsonify({"success": True, "response": "Plate added"})

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

    return jsonify({"success": True, "response": "Plate added"})

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

class PlateResource(Resource):
    def get(self):
        products = Plate.query.all() or abort(404, description="Resource not found")
        return jsonify(
            {"products": [product.to_dict() for product in products]}
        )

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=ascii,help='recurso não enviado, por favor mande um nome')
        parser.add_argument('price', type=float)
        parser.add_argument('category_id', type=int)

        args = parser.parse_args()

        plate = Plate(**args)
        db.session.add(plate)
        db.session.commit()

        return jsonify({"success": True, "response": "Plate added"})


    def put(self):
        pass

    def delete(self):
        pass


class OrderResource(Resource):
    def get(self, product_id):
        product = Order.query.filter_by(id=product_id).first() or abort(
            404, description=f"Resource id {product_id} not found")
        return jsonify(product.to_dict())

api.add_resource(CategoryResource,"/Category")
api.add_resource(PlateResource,"/Plate")
api.add_resource(OrderResource,"/Order")

if __name__ == '__main__':
    app.run(debug=True)

