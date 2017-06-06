from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/buttons")
def buttons():
    return render_template('index.html')


@app.route("/buttons_v2")
def buttons_v2():
    return render_template('buttons_v2.html')


@app.route("/get_color")
def get_color():
    pass_in = request.args
    if pass_in.get("key", "null") == "red":
        color = 'tomato'
    elif pass_in.get("key", "null") == "green":
        color = 'forestgreen'
    elif pass_in.get("key", "null") == 'blue':
        color = 'aqua'
    else:
        color = 'No Color fit the parameter'
    return color
