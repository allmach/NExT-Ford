import os 

SECRET_KEY= 'NEXT'
# SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
# SQLALCHEMY_TRACK_MODIFICATIONS = True
MYSQL_HOST = "0.0.0.0"
MYSQL_USER = "root"
MYSQL_DB = "models"
MYSQL_PORT = 3306
UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'
# app.config['MYSQL_PASSWORD'] = "admin"