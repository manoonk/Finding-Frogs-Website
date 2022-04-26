#! /usr/bin/env python
from flask import Flask, render_template
import json
from random import choice

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True




@app.route("/")
def home():
    return render_template("index.html")




@app.route("/cats")
def cats():
    return render_template("cats.html")

@app.route("/spiel")
def spiel():
    return render_template("spiel.html")

@app.route("/cat1")
def cat1():
    return render_template("cat1.html")

@app.route("/cat2")
def cat2():
    return render_template("cat2.html")

@app.route("/cat3")
def cat3():
    return render_template("cat3.html")

if __name__ == "__main__":
    app.run()

