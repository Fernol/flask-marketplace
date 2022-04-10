import re

from flask import request, redirect, render_template, url_for, flash
from sqlalchemy import exc
from werkzeug.security import generate_password_hash
from email_validate import validate

from marketplace.__init__ import app, db
from marketplace.ModelsDB import User


@app.route('/', methods=['GET', 'POST'])
def index():
    return 'Main page'


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        if validate(request.form['email']) and \
                request.form['psw'] == request.form['psw2'] and \
                re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$',
                         request.form['psw']):
            try:
                passwordHash = generate_password_hash(request.form['psw'])
                user = User(email=request.form['email'], passwordHash=passwordHash)
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('login'))
            except exc.IntegrityError:
                flash('Пользователь существует')
                db.session.rollback()
            except exc.DBAPIError:
                flash('Ошибка соединения с базой данных')
                db.session.rollback()
        else:
            flash('Поля заполнены некорректно')
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    return 'Login page'


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    return 'Logout page'
