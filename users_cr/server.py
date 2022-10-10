from flask import Flask, render_template, redirect, request
from users import User
app = Flask(__name__)


@app.route("/")
def index():
    return redirect("/users")


@app.route("/users")
def all_users():
    return render_template("read_all.html", users=User.get_all())


@app.route("/user/create")
def create_page():
    return render_template("create.html")


@app.route("/user/new", methods=["POST"])
def add_new_user():
    print(request.form)
    User.save(request.form)
    return redirect("/users")


if __name__ == ("__main__"):
    app.run(debug=True, port=8001)
