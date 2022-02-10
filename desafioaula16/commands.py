import os 
from app import app

def recovery_image(id):
    for file_name in os.listdir(app.config['UPLOAD_PATH']):
        if f'image{id}' in file_name:
            return file_name 

def delete_file(id):
    file = recovery_image(id)
    os.remove(os.path.join(app.config['UPLOAD_PATH'], file))