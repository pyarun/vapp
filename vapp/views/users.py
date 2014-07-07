from flask.ext import login, wtf
from flask.views import MethodView
from flask import Blueprint, render_template, redirect, request, jsonify, url_for, make_response

class LoginView(MethodView):
    methods = ['GET', 'POST']

    def dispatch_request(self):
        login.logout_user
        if login.current_user.is_anonymous():
            form = LoginForm(request.form)
            if form.validate_on_submit():
                user = form.get_user()    
                login.login_user(user)
                return redirect('/admin/')
            else:
                print 'did not validate', str(form.errors)
            return render_template('home/login.html', form=form)
        else:
            return redirect('/')


class LoginForm(wtf.Form):
    email = wtf.StringField(validators=[wtf.validators.Length(min=6, max=120),
        wtf.validators.Email(message='Emails must be valid')])

#     email = wtf.Email(validators=[wtf.validators.Required()])
    password = wtf.PasswordField(validators=[wtf.validators.Required()])

    def validate_email(self,field):
        user = self.get_user()
        if user is None:
            raise wtf.ValidationError('Invalid login')

        if user.password != self.password.data:
            raise wtf.ValidationError('Invalid password')

    def get_user(self):
        user = User.objects(email=self.email.data).first()
        return user

class LogoutView(MethodView):
    methods = ['GET', 'POST']

    @login.login_required
    def dispatch_request(self):
        login.logout_user()

        return redirect('/login/')

# users.add_url_rule('/login/', view_func=LoginView.as_view('login'))
# users.add_url_rule('/logout/', view_func=LogoutView.as_view('logout'))