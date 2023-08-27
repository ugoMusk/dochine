#!/usr/bin/env python3
""" starting point """

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    """ home route """
    contributors ="Sue609 | ugoMusk | Sam-ke | EVC"

    logo = "blabla.jpg"
    
    return render_template("home.html", contributors=contributors, logo=logo)
