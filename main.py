from flask import Flask, request, render_template, url_for, redirect, send_file, Response, Markup, abort, jsonify
app = Flask(__name__,static_folder='static')


@app.route("/")
def index():
	return render_template("index.html")

@app.route("/dashboard")
def dashboard():
	return render_template("dashboard.html")

@app.route("/dashboard/treatments")
def treatements():
	return render_template("treatments.html")



app.run(host="0.0.0.0",port=80,threaded=True,debug=True)
