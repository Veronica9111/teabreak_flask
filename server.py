#!/usr/bin/env python
from flask import *
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
	return render_template("index.html")

@app.route("/register")
def register():
	return render_template("register.html")

if __name__ == "__main__":
    app.run()
