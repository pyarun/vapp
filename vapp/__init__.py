from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_googlelogin import GoogleLogin

APPLICATION_DIR = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config.from_pyfile('config.py')
#configure db
app = Flask(__name__)
db = SQLAlchemy(app)

import views
#configure login manager
login_manager = LoginManager()
login_manager.init_app(app)
googlelogin = GoogleLogin(app, login_manager)

@login_manager.user_loader
def load_user(userid):
    import models
    return models.User.query.get(int(userid))






# 
# def init_login():
#     from models import User
#     login_manager = LoginManager()
#     login_manager.setup_app(app)
# #     googlelogin = GoogleLogin(app, login_manager)
#     login_manager.login_view = "/login/"
#     def load_user(user_id):
#         return User.objects(id=user_id).first()
# 
#     @app.before_request
#     def before_request():
#         g.user = current_user
# 
#     login_manager.user_loader(load_user)
# 
# 
# init_login()

