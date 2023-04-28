from flask import Flask, render_template, url_for, request, redirect,flash
from flask_sqlalchemy import SQLAlchemy
from forms import SignupForm, PostForm, LoginForm, RegistroForm
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from models import User, db, login_manager
from sanitizar import sanitizar_caracteres


import os

app = Flask(__name__)

app.config['SECRET_KEY'] = "e23895acc525f92e886e9fe425046e0743855fbc038a70067540742c9fd34179"

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:admin123@localhost:5432/flask-app-post'

app.config['SQLALCHEMY_TRACK_MODIFICATION']= False

db.init_app(app)

login_manager.init_app(app)

login_manager.login_view = "error"

@app.before_first_request
def create_table():
    db.create_all()


diccionario_post = []

@app.route("/", methods=["GET", "POST"])
def login():

    if current_user.is_authenticated:
        return redirect(url_for("index"))




    form = LoginForm()

    if form.validate_on_submit():
        email = request.form['email']

        user = User.query.filter_by(email = email).first()


        if user is not None and user.check_password(request.form['password']):

            login_user(user)

            return redirect(url_for('index'))
        


    return render_template("login.html", form=form)


@app.route("/registrarse", methods=["GET", "POST"])
def registrar():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    
    form = RegistroForm()

    if form.validate_on_submit():
        
        
        email = sanitizar_caracteres(form.usuario.data)        
        password = form.password.data
        nombre = sanitizar_caracteres(form.nombre.data)
        nombre = nombre.capitalize()
       
        user = User(email = email, name = nombre)

        user.set_password(password)

        #COMENTANDO LOGIN AUTOMATICO AL REGISTRARSE
        #login_user(user, remember=True)
        
        db.session.add(user)
        
        db.session.commit()
        
        return redirect(url_for('login'))
   
    return render_template("registro_usuarios.html", form=form)


@app.route("/inicio")
@login_required
def index():

    global diccionario_post

    return render_template("index.html", diccionario_posts=diccionario_post)


@app.route("/quienes")
@login_required
def quienes():

    return render_template("quienes.html")


@app.route("/posts", methods=["GET", "POST"])
@app.route("/posts/<int:npost>", methods=["GET", "POST"])
@login_required
def posts():
    global diccionario_post
    form = PostForm()

    if form.validate_on_submit():
        diccionario_post.append(
            {"titulo": form.titulo.data, "contenido": form.contenido.data})

        return redirect(url_for("index"))

    return render_template("posts.html", form=form)


@app.route("/contacto", methods=["GET", "POST"])
@login_required
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


@app.route("/error")
def error():

    return render_template("error_login.html")




if __name__ == "__main__":
    os.environ["FLASK_DEBUG"] = "development"
    app.run(debug=True)
