from flask import request, render_template, redirect, flash, url_for, session, send_from_directory
import time 

from models import Restaurant 
from dao import RestaurantDao, UserDao

from commands import recovery_image, delete_file 
from app import db, app


restaurant_dao = RestaurantDao(db)
user_dao = UserDao(db)

@app.route('/')
def home():
    list = restaurant_dao.list()
    return render_template('lista.html', titulo = 'All Food Restaurant NExT - Orders ', orders=list) 

@app.route('/new')
def new():
    if 'user_logon' not in session or session['user_logon'] == None:
        return redirect(url_for('login', proxima=url_for('new')))
    return render_template('new.html', titulo='All Food Restaurant NExT - New Order')

@app.route('/createorder', methods=['POST'])
def create_order():
    plate = request.form['plate']
    category = request.form['category']
    price = request.form['price']
    order = Restaurant(plate, category, price)
    order = restaurant_dao.save(order)

    file=request.files['file']
    upload_path = app.config['UPLOAD_PATH']
    timestamp = time.time()
    file.save(f'{upload_path}/image{order.id}-{timestamp}.jpg')
    return redirect(url_for('home'))

@app.route('/edit/<int:id>')
def edit(id):
    if 'user_logon' not in session or session['user_logon'] == None:
        return redirect(url_for('login', proxima=url_for('edit')))
    order = restaurant_dao.search_by_id(id)
    image_name = recovery_image(id)
    front_image = f'image{id}.jpg'
    return render_template('edit.html', titulo='All Food Restaurant NExT - Edit Order', order=order, front_image = image_name)

@app.route('/update', methods=['POST'])
def update():
    plate = request.form['plate']
    category = request.form['category']
    price = request.form['price']
    order = Restaurant(plate, category, price, id=request.form['id'])
    restaurant_dao.save(order)

    file=request.files['file']
    upload_path = app.config['UPLOAD_PATH']
    timestamp = time.time()
    delete_file(order.id)
    file.save(f'{upload_path}/image{order.id}-{timestamp}.jpg')
    return redirect(url_for('home'))

@app.route('/delete/<int:id>')
def delete(id):
    restaurant_dao.delete(id)
    flash('Order has been removed')
    return redirect(url_for('home'))

@app.route('/login')
def login():
    next = request.args.get('next')
    return render_template('login.html', next=next)

@app.route('/authentication', methods=['POST'])
def authentication():
    user = user_dao.search_by_id(request.form['user'])
    if user: 
        if user.password ==request.form['password']: 
            session ['user_logon'] = user.id 
            flash(user.name + ' login successful!')
            next_page = request.form['next']
            return redirect(next_page)
    else:
        flash('Please, Try again!')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session ['user_logon'] = None
    flash('No user logon')
    return redirect(url_for('home'))

@app.route('/uploads/<file_name>')
def image(file_name):
    return send_from_directory('uploads', file_name)

