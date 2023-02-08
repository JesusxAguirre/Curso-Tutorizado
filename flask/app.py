from flask import Flask,render_template,url_for
import os
#from markupsafe import escape

app = Flask(__name__)

empleados = ["Ana","Maria","Sandra","Reina"]


@app.route("/")
def index():

  return render_template("index.html",numero_empleados=len(empleados))

@app.route('/hola-mundo')
def hola_mundo():

  return render_template("hello.html")

@app.route("/usuarios/<string:nombre_usuario>")
def get_usuario(nombre_usuario):

  return f"Bienvenido a la web {nombre_usuario}"

@app.route("/usuarios/<int:id_usuario>")
def get_id_usuario(id_usuario):

  #return f"Bienvenido a la web. usuario numero-> {id_usuario}"
  return render_template("usuarios/usuarios.html",id_usuario=id_usuario)


@app.route("/usuarios/<int:id>/<string:nombre_usuario>")
def get_datos_usuarios(id,nombre_usuario):
  #return f"Estos son los datos del usuario. id-> {id}, nombre-> {nombre_usuario}"
  return render_template("usuarios/datos_usuarios.html",id=id,nombre_usuario=nombre_usuario)

@app.route("/posts")
@app.route("/posts/<int:n_post>")
def post(n_post=0):

  return f"este es el post numero {n_post}"


if __name__ == "__main__":
  os.environ['FLASK_DEBUG']= "development"
  app.run(debug=True)


"""
@app.route("/username/<username>")
def show_user_profile(username):
  return f'User{escape(username)}'
"""