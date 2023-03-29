from flask import Flask, render_template, url_for, request, redirect
from forms import SignupForm, PostForm, LoginForm, RegistroForm
import os

app = Flask(__name__)


app.config['SECRET_KEY'] = "e23895acc525f92e886e9fe425046e0743855fbc038a70067540742c9fd34179"

empleados = ["Ana", "maria", "sandra"]

diccionario_post = []

usuarios = []

login = 0


@app.route("/", methods=["GET", "POST"])
def login():
    global usuarios
    global login
    form = LoginForm()

    if form.validate_on_submit():

        for usuario in usuarios:
            if usuario['usuario'] == form.email.data and usuario['password'] == form.password.data:
                login = 1
                return redirect(url_for("index"))

    return render_template("login.html", form=form)


@app.route("/registrarse")
def registrar():
    global usuarios
    form = RegistroForm()

    if form.validate_on_submit():
        usuarios.append({"usuario": form.email.data,
                        "password": form.password.data})

        return redirect(url_for('login'))

    return render_template("registro_usuarios.html", form=form)


@app.route("/inicio")
def index():
    global login
    if login:
        global diccionario_post

        return render_template("index.html", diccionario_posts=diccionario_post)
    else:
        return redirect(url_for("login"))


@app.route("/quienes")
def quienes():
    global login
    if login:
        return render_template("quienes.html")
    else:
        return redirect(url_for("login"))


@app.route("/posts", methods=["GET", "POST"])
@app.route("/posts/<int:npost>", methods=["GET", "POST"])
def posts():
    global diccionario_post
    form = PostForm()

    if form.validate_on_submit():
        diccionario_post.append(
            {"titulo": form.titulo.data, "contenido": form.contenido.data})

        return redirect(url_for("index"))

    return render_template("posts.html", form=form)


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
