from flask import Flask
import os
from views.home import HomeView
from flask.ext.mail import Message, Mail
 
mail = Mail()

APPLICATION_DIR = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.debug = True

app.secret_key = 'development key'
 
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'contact@example.com'
app.config["MAIL_PASSWORD"] = 'your-password'
 
mail.init_app(app)
 
 
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/demo'
 
from models import db
db.init_app(app)
# import intro_to_flask.routes

app.add_url_rule('/', view_func=HomeView.as_view('home'))
