from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Форма для редактирования профиля
@app.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        # Здесь вы можете добавить логику для сохранения изменений профиля
        return redirect(url_for('profile', name=name, email=email))
    return render_template('edit_profile.html')

@app.route('/profile')
def profile():
    name = request.args.get('name', 'No Name')
    email = request.args.get('email', 'No Email')
    return f'<h1>Profile Page</h1><p>Name: {name}</p><p>Email: {email}</p>'

if __name__ == '__main__':
    app.run(debug=True)