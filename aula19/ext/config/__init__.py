def init_app(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://allmach1:FOOT035a#@allmach1.mysql.pythonanywhere-services.com/allmach1$default'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['SECRET_KEY'] = "asdasdsadasd"
    app.config['JWT_SECRET_KEY'] = 'asfasfasfas'
    app.config['JWT_BLACKLIST_ENABLED'] = True
