from flask import Flask, render_template, url_for, request, redirect
from forms import SignupForm, PostForm, LoginForm, RegistroForm
import os
from flask_login import LoginManager


app = Flask(__name__)


app.config['SECRET_KEY'] = "e23895acc525f92e886e9fe425046e0743855fbc038a70067540742c9fd34179"

login_manager = LoginManager(app)

empleados = ["Ana", "maria", "sandra"]

diccionario_post = []

usuarios = []

nombre_usuario = ""

login = 0



@app.route("/", methods=["GET", "POST"])
def login():
    global usuarios
    global login
    global nombre_usuario
    form = LoginForm()

    if form.validate_on_submit():

        for usuario in usuarios:
            if usuario['usuario'] == form.email.data and usuario['password'] == form.password.data:
                login = 1
                nombre_usuario = usuario['nombre']
                return redirect(url_for("index"))

    return render_template("login.html", form=form)


@app.route("/registrarse", methods=["GET", "POST"])
def registrar():
    global usuarios
    form = RegistroForm()

    if form.validate_on_submit():
        usuarios.append({"usuario": form.usuario.data,
                        "password": form.password.data,
                         "nombre": form.nombre.data})

        return redirect(url_for('login'))
    else:
        pass

    return render_template("registro_usuarios.html", form=form)


@app.route("/inicio")
def index():
    global nombre_usuario
    global login
    if login == 1:
        global diccionario_post

        return render_template("index.html", diccionario_posts=diccionario_post, nombre_usuario=nombre_usuario)
    else:
        return redirect(url_for("login"))


@app.route("/quienes")
def quienes():
    global login
    if login == 1:
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
