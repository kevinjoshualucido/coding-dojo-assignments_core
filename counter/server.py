from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "this is my secret key."


@app.route("/")
def index():
    if "counter" not in session:
        session["counter"] = 0
    else:
        session["counter"] += 1
    return render_template("index.html")


@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True, port=8000)
