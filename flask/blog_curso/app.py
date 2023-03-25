from flask import Flask, render_template, url_for

app = Flask(__name__)

empleados = ["Ana","maria","sandra"]


@app.route("/")
def index():

    return render_template("index.html",numero_empleados=len(empleados))
