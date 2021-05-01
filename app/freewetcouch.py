from flask import Flask, render_template, url_for, make_response
import random, os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/style.css')
def css():
    response = make_response(render_template("style.css", couch_file=couch()))
    response.headers['Content-Type'] = 'text/css'
    return response


def couch():
    path = './static'
    random_couch = random.choice([x for x in os.listdir(path)
                                  if os.path.isfile(os.path.join(path, x))])
    return url_for('static', filename=random_couch)


if __name__ == '__main__':
    app.run(debug=False)
