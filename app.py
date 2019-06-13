from flask_heroku import Heroku
from flask import Flask, render_template

app = Flask(__name__)
heroku = Heroku(app)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == '__main__':
    app.debug = True
    app.run()