from flask import Flask, render_template, json

# save this as app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/<gebiet>")
def usa(gebiet):
    with open(f"./static/data/{gebiet}.json", "r") as f:
        stamps = json.load(f)

   
    return render_template("std.html", gebiet=gebiet.upper(), stamps=stamps)

@app.route("/ziffern_spezial")
def ziffern_spezial():
    return "Hello, Ziffern!"