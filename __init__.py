from flask import Flask, render_template
app = Flask(__name__)


@app.route("/buttons")
def buttons():
    my_list = []
    for x in range(0, 100):
        my_list.append(x)

    return render_template('index.html', **locals())

@app.route("/get_red_color")
def get_red_color():
    return "red"
