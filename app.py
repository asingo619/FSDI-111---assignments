from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello, world!<h1>"

@app.route("/about")
def about_me():
    me = {
        "first_name": "Andrew",
        "last_name": "Singo",
        "hobbie": "Various",
        "active": True
    } 
    return me