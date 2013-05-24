#!/usr/bin/env python
from flask import *
import flask_login
from flask_login import LoginManager, login_user, current_user, login_required, logout_user
import os
import sys

sys.path.append(os.path.abspath('.') + "/modules/controller")
sys.path.append(os.path.abspath('.') + "/modules/model")
from UserManager import *

app = Flask(__name__)
app.secret_key = os.urandom(24)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(userid):
    return UserManager.get(userid)

@app.route("/index", methods=['GET', 'POST'])
def index():
    for key in session.iterkeys():
        print key
        print session[key]
	return render_template("index.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_data = request.values
        print request.args.get('remember_me')
        user = UserManager(mail=user_data['email'], password=user_data['password'])
        print request.args
        session['remember_me'] = request.args.get('remember_me', 1)
        if user.is_validate():
            login_user(user, remember=True)
            for key in session.iterkeys():
                print key
                print session[key]
            #print session['user_id']
            flash("Log in successfully")
            #nickname = user.get_nickname()
            return render_template('main.html', nickname=current_user._mail)

@app.route("/register", methods=['GET', 'POST'])
def register():
	if request.method == 'POST':
		user_data = request.values
		um = UserManager(name=user_data['nickname'], mail=user_data['email'], password=user_data['password'])
		um.create_new_user()
		return render_template('main.html', nickname=user_data['nickname'])
	return render_template("register.html")

@app.route("/")
@app.route("/main", methods=['GET'])
def get_main_page():
    if not current_user.is_anonymous():
        for key in session.iterkeys():
            print key
            print session[key]
	    return render_template('main.html', nickname=current_user._mail)
    else:
        return render_template('index.html')

@app.route("/logout")
@login_required
def logout():
    logout_user()
    print current_user
    for key in session.iterkeys():
        print key
        print session[key]
    return redirect(url_for('index'))
if __name__ == "__main__":
    app.run(debug=True)
