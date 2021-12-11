from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/tree")
def hello_world():
    return "<p>See you later, World!</p>"

from markupsafe import escape

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"

@app.route("/bambimbom")
def bambimbom():
    return "jadhfjkdhfjkhdlfajkhdslfakjsfhuwirhehnciurtbewjibwavlrehb"

@app.route('/user/<usud>')
def show_ur_name(usud):
    return f'Usdr {escape(usud)}87'

@app.route('/')
def show_a_html_file():
    return render_template("'ello.html", name="'ello.html")