from flask import Flask, render_template
app = Flask(__name__)


# LEVEL 1
@app.route("/play")
def index():
    return render_template("index.html", num_boxes=3)


# LEVEL 2
@app.route("/play/<int:num_box_var>")
def display_boxes(num_box_var):
    return render_template("index.html", num_boxes=num_box_var)

# LEVEL 3
@app.route("/play/<int:num_box_var>/<string:color>")
def display_boxes_colors(num_box_var, color):
    return render_template("index.html", num_boxes=num_box_var, chosen_color=color)

if __name__ == ("__main__"):
    app.run(debug=True, port=8000)
