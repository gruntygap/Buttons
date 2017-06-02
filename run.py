from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def template_test():
    my_list = []
    for x in range(0, 100):
        my_list.extend(str(x))

    return render_template('template.html', my_string="Wheeeee!", my_list = my_list)


if __name__ == '__main__':
    app.run(debug=True)