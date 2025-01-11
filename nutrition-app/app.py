from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/hi")
def hi():
    return "<p>Ok</p>"

@app.route("/")
def hello_world():
    message = "<p>Hello World!</p>"
    link = '<p><a href="/hi">F*ck you!</a></p>'

    return message + link