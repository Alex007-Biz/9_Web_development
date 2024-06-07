import flask
from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def films():
    return render_template("films.html", caption="Фильмы про Гарри")

@app.route("/shablon")
def films2():
    return render_template("films.html", caption="Гарри Поттер")

@app.route("/person/")
def person():
    return render_template("heroes.html")



if __name__ == "__main__":
    app.run()