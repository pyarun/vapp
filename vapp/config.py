import os 
 
 
DEBUG = True
 
CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(BASE_DIR, 'migrations')


GOOGLE_LOGIN_CLIENT_ID = "36222678620-dsj4q2hisjohknuhcf36cdhgon0j66m1.apps.googleusercontent.com"
GOOGLE_LOGIN_CLIENT_SECRET = "GF6q7IusyvDr-vFAvvPp20Cg"

# app.config["MAIL_SERVER"] = "smtp.gmail.com"
# app.config["MAIL_PORT"] = 465
# app.config["MAIL_USE_SSL"] = True
# app.config["MAIL_USERNAME"] = 'contact@example.com'
# app.config["MAIL_PASSWORD"] = 'your-password'
 
# db = SQLAlchemy(app)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
#  
# from models import db
# db.init_app(app)
# # import intro_to_flask.routes
# 
# lm = LoginManager()
# lm.init_app(app)
# oid = OpenID(app, os.path.join(basedir, 'tmp'))

