from flask import Flask, render_template, url_for, request, redirect
from forms import SignupForm, PostForm, LoginForm
import os

app = Flask(__name__)


app.config['SECRET_KEY'] = "e23895acc525f92e886e9fe425046e0743855fbc038a70067540742c9fd34179"

empleados = ["Ana", "maria", "sandra"]

diccionario_post = []

datos_usuario = {}

@app.route("/", methods=["GET","POST"])
def login():
    global datos_usuario
    form = LoginForm()

    if form.validate_on_submit():
        datos_usuario['usuario'] = form.email.data
        datos_usuario['clave'] = form.password.data


        print(datos_usuario)
        
    return render_template("login.html",form = form)


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


if __name__ == "__main__":
    os.environ["FLASK_DEBUG"] = "development"
    app.run(debug=True)
