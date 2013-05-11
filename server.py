#!/usr/bin/env python
from flask import *

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
	return render_template("index.html")

@app.route("/register", methods=['GET', 'POST'])
def register():
	if request.method == 'POST':
		#user = User(form.username.data, form.email.data, form.password.data)
		#userDB.add(user)
		user_data = request.values
		return render_template('main.html', nickname=user_data['nickname'])
	return render_template("register.html")

@app.route("/main", methods=['GET'])
def get_main_page():
	return render_template('main.html', nickname)
if __name__ == "__main__":
    app.run(debug=True)
