from flask import Flask, render_template, url_for, request, redirect
from forms import SignupForm,PostForm
import os

app = Flask(__name__)


app.config['SECRET_KEY'] = "e23895acc525f92e886e9fe425046e0743855fbc038a70067540742c9fd34179"

empleados = ["Ana", "maria", "sandra"]

diccionario_post = []


@app.route("/")
def index(diccionario_posts):

    return render_template("index.html", posts=diccionario_post)


@app.route("/quienes")
def quienes():

    return render_template("quienes.html")


@app.route("/posts")
@app.route("/posts/<int:npost>")
def posts(npost):
    global diccionario_post
    form = PostForm()

    if form.validate_on_submit():
        diccionario_post.append(
            {"titulo": form.titulo.data, "contenido": form.contenido.data})

        redirect(url_for("index",diccionario_post))

    return render_template("posts.html", npost=npost)


@app.route("/contacto", methods=["GET", "POST"])
def contacto():

    form = SignupForm()
    if form.validate_on_submit():

        nombre = form.name.data
        email = form.email.data
        password = form.password.data

        return redirect(url_for("index"))

    return render_template("contacto.html", form=form)


if __name__ == "__main__":
    os.environ["FLASK_DEBUG"] = "development"
    app.run(debug=True)
