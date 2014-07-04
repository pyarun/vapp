from flask.views import MethodView
import serve
from flask import render_template
from flask import  request
from models import User
from database import db_session

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

# app.add_url_rule('/', view_func=HomeView.as_view('home'))
# # app.add_url_rule('/oauth2callback', view_func=create_or_update_user)

