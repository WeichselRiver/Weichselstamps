from flask import Flask

# save this as app.py
from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello, World!"