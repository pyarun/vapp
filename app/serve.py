from flask import Flask, g
import os
from flask.ext.login import LoginManager, current_user

import views.home
import views.users #import LoginView, LoginForm, LogoutView 
# , LoginView
# from flask.ext.mail import Message, Mail
 
# mail = Mail()

APPLICATION_DIR = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.debug = True

app.secret_key = 'development key'

from flask_googlelogin import GoogleLogin
# googlelogin = GoogleLogin(app)
 
GOOGLE_LOGIN_CLIENT_ID = "36222678620-dsj4q2hisjohknuhcf36cdhgon0j66m1.apps.googleusercontent.com"
GOOGLE_LOGIN_CLIENT_SECRET =  "GF6q7IusyvDr-vFAvvPp20Cg"

# app.config["MAIL_SERVER"] = "smtp.gmail.com"
# app.config["MAIL_PORT"] = 465
# app.config["MAIL_USE_SSL"] = True
# app.config["MAIL_USERNAME"] = 'contact@example.com'
# app.config["MAIL_PASSWORD"] = 'your-password'
 
# mail.init_app(app)
 
# db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
#  
# from models import db
# db.init_app(app)
# # import intro_to_flask.routes
# 
# lm = LoginManager()
# lm.init_app(app)
# oid = OpenID(app, os.path.join(basedir, 'tmp'))


def init_login():
    from models import User
    login_manager = LoginManager()
    login_manager.setup_app(app)
    googlelogin = GoogleLogin(app, login_manager)
    login_manager.login_view = "/login/"
    def load_user(user_id):
        return User.objects(id=user_id).first()

    @app.before_request
    def before_request():
        g.user = current_user

    login_manager.user_loader(load_user)


init_login()

app.add_url_rule('/', view_func=views.home.HomeView.as_view('home'))
app.add_url_rule('/oauth2callback', view_func=views.home.create_or_update_user)
app.add_url_rule('/login/', view_func=views.users.LoginView.as_view('login'))
app.add_url_rule('/welcome/', view_func=views.home.WelcomeView.as_view('welcome'))
app.add_url_rule('/logout/', view_func=views.users.LogoutView.as_view('logout'))


