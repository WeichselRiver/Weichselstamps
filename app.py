from flask import Flask, render_template, json

# save this as app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("Index.html")

@app.route("/usa")
def usa():
    with open(f"./static/data/usa.json", "r") as f:
        stamps = json.load(f)
    return render_template("std.html", stamps=stamps, gebiet="USA")

@app.route("/ziffern_spezial")
def ziffern_spezial():
    with open(f"./static/data/ziffern.json", "r") as f:
        marken = json.load(f)
    return render_template("spezial.html", marken = marken, gebiet="I. Kontrollratsausgabe - Ziffernserie")