from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def get_quote():
    url = 'https://api.quotable.io/random'
    response = requests.get(url)
    data = response.json()
    quote = data['content']
    author = data['author']
    return render_template('quote.html', quote=quote, author=author)

@app.route('/new_quote')
def get_new_quote():
    url = 'https://api.quotable.io/random'
    response = requests.get(url)
    data = response.json()
    quote = data['content']
    author = data['author']
    return {'content': quote, 'author': author}

if __name__ == '__main__':
    app.run(debug=True)