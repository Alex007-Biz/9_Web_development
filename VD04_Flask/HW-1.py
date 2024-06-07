from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)
@app.route("/")
def index():
    current_date_time = datetime.now()
    a1 = current_date_time.strftime("%Y-%m-%d %H:%M:%S")
    html = """
    <h1>Текущая дата и время </h1>
    <p>а это просто текст</p>
    """
    return render_template('date_time.html', a1=a1)

if __name__ == "__main__":
    app.run()