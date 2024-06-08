import flask
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def films2():
    context = {
        "link":"перейти в кинотеатр"
    }
    return render_template("home.html", **context)

@app.route("/person/")
def person():
    context = {
        "link":"перейти в кинотеатр"
    }
    return render_template("about.html", **context)



if __name__ == "__main__":
    app.run()