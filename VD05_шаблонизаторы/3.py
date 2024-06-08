import flask
from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def films():
    context = {
        "poem" : ["Я помню чудное мгновенье",
                  "передо мной явилась ты",
                  "как мимолетное виденье",
                  "как гений чистой красоты"
                  ]
    }
    return render_template("shablon_3.html", **context)

@app.route("/shablon")
def films2():
    context = {
        "caption":"Гаррик Поттер",
        "link":"перейти в кинотеатр"
    }
    return render_template("films.html", **context)

@app.route("/person/")
def person():
    return render_template("heroes.html")



if __name__ == "__main__":
    app.run()