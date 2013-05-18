#!/usr/bin/env python
from flask import *
import os
import sys

sys.path.append(os.path.abspath('.') + "/modules/controller")
sys.path.append(os.path.abspath('.') + "/modules/model")
from UserManager import *

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
	return render_template("index.html")

@app.route("/register", methods=['GET', 'POST'])
def register():
	if request.method == 'POST':
		user_data = request.values
		um = UserManager(user_data['nickname'],user_data['email'],user_data['password'],)
		um.create_new_user()
		return render_template('main.html', nickname=user_data['nickname'])
	return render_template("register.html")

@app.route("/main", methods=['GET'])
def get_main_page():
	return render_template('main.html', nickname)
if __name__ == "__main__":
    app.run(debug=True)
