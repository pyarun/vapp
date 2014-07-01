from flask.views import MethodView

class HomeView(MethodView):
    def get(self):
        return 'Hello World!'
 
