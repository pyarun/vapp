from flask.views import MethodView
from flask import render_template
from flask import  request
# from models import User
# from database import db_session
from vapp import app, db
import urllib2, json
import urllib
from flask_login import login_user
# from vapp.models import User

class LoginView(MethodView):
    """
    Manages user login
    """
    def get(self):
        """
        Renders Login page
        """
        return render_template("login.html", title = 'Login')
    
    def post(self):
        """
        authenticated user and set session
        """
        import ipdb;ipdb.set_trace()
        req_data = request.get_json()
        if req_data["status"]["signed_in"]:
            data = urllib.urlencode({"access_token": req_data["access_token"]})
            url = "https://www.googleapis.com/plus/v1/people/me?" + data
            response = json.loads(urllib2.urlopen(url).read())
            user_gid = response["id"]
            try:
                user = User.query.get(google_id = user_gid) 
            except:
                user = User(google_id=user_gid)
                db.session.add(user)
                db.session.commit()
            
            login_user(user)
            print response
        

class HomeView(MethodView):
    def get(self):
        import ipdb; ipdb.set_trace();
        return render_template("home/index.html") 

class WelcomeView(MethodView):
    def post(self):
        print request
        email = request.form.get('email')
        password = request.form.get('password')
        import ipdb; ipdb.set_trace();

        user = User(email, password)
        db_session.add(user)
        db_session.commit()
        return render_template("home/welcome.html",user=user) 

# @app.route('/oauth2callback')
# @googlelogin.oauth2callback
def create_or_update_user(token, userinfo, **params):
    user = User.filter_by(google_id=userinfo['id']).first()
    if user:
        user.name = userinfo['name']
        user.avatar = userinfo['picture']
    else:
        user = User(google_id=userinfo['id'],
                    name=userinfo['name'],
                    avatar=userinfo['picture'])
    db.session.add(user)
    db.session.flush()
    login_user(user)
    return redirect(url_for('index'))


# app.add_url_rule('/', view_func=views.home.HomeView.as_view('home'))
# app.add_url_rule('/oauth2callback', view_func=views.home.create_or_update_user)
# app.add_url_rule('/login/', view_func=views.users.LoginView.as_view('login'))
# app.add_url_rule('/welcome/', view_func=views.home.WelcomeView.as_view('welcome'))
# app.add_url_rule('/logout/', view_func=views.users.LogoutView.as_view('logout'))

app.add_url_rule("/", view_func=LoginView.as_view('login'))