from flask import Flask,render_template,url_for
import os
from markupsafe import escape

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


if __name__ == "__main__":
  os.environ['FLASK_DEBUG']= "development"
  app.run(debug=True)


"""
@app.route("/username/<username>")
def show_user_profile(username):
  return f'User{escape(username)}'
"""