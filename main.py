from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)


@app.route("/")
def main():
    return redirect("/login")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("index.html")
    else:
        if request.form.get("username") == os.environ.get('USER') and request.form.get("password") == os.environ.get('password'):
            return render_template("secret.html")
        else:
            return render_template("index.html")


app.run("localhost", 8000)
