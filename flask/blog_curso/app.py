from flask import Flask, render_template, url_for, request, redirect
from forms import SignupForm, PostForm, LoginForm, RegistroForm
from flask_login import LoginManager, current_user, login_user, logout_user
from models import users, get_user, User

import os

app = Flask(__name__)


app.config['SECRET_KEY'] = "e23895acc525f92e886e9fe425046e0743855fbc038a70067540742c9fd34179"

login_manager = LoginManager(app)


diccionario_post = []


@app.route("/", methods=["GET", "POST"])
def login():

    if current_user.is_aunthenticated:
        return redirect(url_for("index"))

    form = LoginForm()

    if form.validate_on_submit():
        user = get_user(form.email.data)

        if user is not None and (user.chek_password(form.password.data)) == form.password.data:
            login_user(user, remember=form.remember_me.data)

            next_page = request.args.get("next")

            if not next_page:
                next_page = url_for("login")

            return redirect(next_page)

    return render_template("login.html", form=form)


@app.route("/registrarse", methods=["GET", "POST"])
def registrar():
    global usuarios
    form = RegistroForm()

    if form.validate_on_submit():
        email = form.usuario.data
        password = form.password.data
        nombre = form.nombre.data

        user = User(len(users) + 1, nombre, email, password)

        users.append(user)

        login_user(user, remember=True)

        return redirect(url_for('index'))
    else:
        pass

    return render_template("registro_usuarios.html", form=form)


@app.route("/inicio")
def index():

    global diccionario_post

    return render_template("index.html", diccionario_posts=diccionario_post)


@app.route("/quienes")
def quienes():

    return render_template("quienes.html")


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


@app.route("/logout")
def logout():
    logout_user()

    return redirect(url_for("login"))


@login_manager.user_loader
def load_user(user_id):
    for user in users:
        if user.id == int(user_id):
            return user
    return None


if __name__ == "__main__":
    os.environ["FLASK_DEBUG"] = "development"
    app.run(debug=True)
