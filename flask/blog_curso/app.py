from flask import Flask, render_template, url_for
import os


app = Flask(__name__)

empleados = ["Ana","maria","sandra"]


@app.route("/")
def index():

    return render_template("index.html",numero_empleados=len(empleados))


@app.route("/quienes")
def quienes():
    
    return render_template("quienes.html")

@app.route("/posts")
@app.route('/posts/<int:npost>')
def posts(npost = 0):
    return "este es el post: {}".format(npost)


if __name__ == '__main__':
    os.environ['FLASK_DEBUG'] = "development"
    app.run(debug=True)
