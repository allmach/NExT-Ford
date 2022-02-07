class Restaurant():
    def __init__(self, plate, category, price, id=None):
        self.id = id
        self.plate = plate
        self.category = category
        self.price = price

class User():
    def __init__(self, id, name, password, email):
        self.id = id
        self.name = name
        self.password = password 
        self.email = email