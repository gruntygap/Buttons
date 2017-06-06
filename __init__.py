from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/buttons")
def buttons():
    return render_template('index.html')

@app.route("/get_color")
def get_color():
    passIn = request.args
    return passIn.get("key", "null")
