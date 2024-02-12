from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
db = SQLAlchemy()
DB_NAME = "database.db"
def create_application():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "sana"
    app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    from .view import view
    from .authentication import authentication
    app.register_blueprint(view,url_prefix="/")
    app.register_blueprint(authentication,url_prefix="/")
    from .models import User
    database(app)
    login = LoginManager()
    login.login_view = "authentication.login"
    login.init_app(app)
    @login.user_loader
    def load_user(id):
        return User.query.get(int(id))  
    return app
def database(app):
    if not path.exists("website/"+DB_NAME):
        with app.app_context():
            db.create_all()
        print("Created Database")
