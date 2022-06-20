from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route("/")
def main():
    return redirect("/login")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("index.html")
    else:
        if request.form.get("username") == "C1b3rPl4y3r" and request.form.get("password") == "C1b3rWall{dont_store_passwords_in_code}":
            return render_template("secret.html")
        else:
            return render_template("index.html")


app.run("localhost", 8000)
