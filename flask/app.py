from flask import Flask,render_template,url_for

#from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def index():

  return render_template("index.html")

@app.route('/hello')
def hola_mundo():

  return "hello.html"

"""
@app.route("/username/<username>")
def show_user_profile(username):
  return f'User{escape(username)}'
"""