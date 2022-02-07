from datetime import datetime
from unicodedata import category, name
#from flask import Flask, jsonify, abort, request, render_template, redirect, session, flash, url_for
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from flask import Flask, request, render_template, redirect, flash, url_for, jsonify, abort, session
from dao import RestaurantDao, UserDao
from flask_mysqldb import MySQL 
from models import Restaurant, User 

app = Flask(__name__)
app.secret_key = 'NEXT'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['MYSQL_HOST'] = "0.0.0.0"
app.config['MYSQL_USER'] = "root"
# app.config['MYSQL_PASSWORD'] = "admin"
app.config['MYSQL_DB'] = "app"
app.config['MYSQL_PORT'] = 3306
api = Api(app)
db = SQLAlchemy(app)

db = MySQL(app)

user1 = User('allan', 'Allan Machado', '1234')
user2 = User('pedro', 'pedro marques', '234')

users = {user1.id: user1, user2.id: user2}
restaurant_dao = RestaurantDao(db)
user_dao = UserDao(db)

order1 = Restaurant
order2 = Restaurant
list = [order1, order2]

user1 = User('allan', 'Allan Machado', '1234', 'allan_asmachado@hotmail.com')
user2 = User('pedro', 'pedro marques', '234', 'allan_asmachado@hotmail.com')
users = {user1.id: user1, user2.id: user2}

@app.route('/')
def home():
    # list = restaurant_dao.list()
    return render_template('lista.html', titulo = 'All Food Restaurant NExT', orders=list) 

@app.route('/new')
def create_order():
    category = request.form['category']
    price = request.form['price']
    order = Restaurant(plate, category, price)
    list.append(order)
    restaurant_dao.save(order)
    return redirect(url_for('home'))

@app.route('/login')
def login():

@app.route('/authentication', methods=['POST'])
def authentication():
    if request.form['user'] in users:
        user = users[request.form['user']]
        if user.password ==request.form['password']: 
    # user = user_dao.search_by_id(request.form['user'])
    # if user: 
          session ['user_logon'] = user.id 
          flash(user.name + ' login successful!')
          next_page = request.form['next']
          return redirect(next_page)
    else:
          flash('Please, Try again!')
          return redirect(url_for('login'))

@app.route('/signup')
def signup():
    next1 = request.args.get('next1')
    return render_template('signup.html', next1=next1)

@app.route('/authentications', methods=['POST'])
def authentications():
    if request.form['user'] in users:
        user = users[request.form['user']]
        if user.password ==request.form['password']: 
            session ['user_signup'] = user.id 
            flash(user.name + ' Signup successful!')
            next_page1 = request.form['next1']
            return redirect(next_page1)
        else:
            flash('Please, Try again!')
            return redirect(url_for('signup'))

@app.route('/logout')
def logout():
    session ['user_logon'] = None
    flash('No user logon')
    return redirect(url_for('home'))

app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True)
