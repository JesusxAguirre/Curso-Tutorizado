from flask import Flask, render_template, url_for, request, redirect
import os
from forms import SignupForm


app = Flask(__name__)

empleados = ["Ana", "maria", "sandra"]


@app.route("/")
def index():

    return render_template("index.html", numero_empleados=len(empleados))


@app.route("/quienes")
def quienes():

    return render_template("quienes.html")


@app.route("/posts")
@app.route("/posts/<int:npost>")
def posts(npost):
    return render_template("posts.html", npost=npost)


@app.route("/contacto", methods=["GET", "POST"])
def contacto():

    form = SignupForm()
    if form.validate_on_submit:

        nombre = form.name
        email = form.email
        password = form.password

        return redirect(url_for("index"))

    return render_template("contacto.html")


if __name__ == "__main__":
    os.environ["FLASK_DEBUG"] = "development"
    app.run(debug=True)
