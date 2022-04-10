import re

from flask import request, redirect, render_template, url_for, flash
from sqlalchemy import exc
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from email_validate import validate

from marketplace.__init__ import app, db, login_manager
from marketplace.ModelsDB import User


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('psw')
        password2 = request.form.get('psw2')
        if not (email or password or password2):
            flash('Поля заполнены некорректно')
        if validate(email) and \
                password == password2 and \
                re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$',
                         password):
            try:
                passwordHash = generate_password_hash(request.form['psw'])
                user = User(email=email, passwordHash=passwordHash)
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
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('psw')
        if email and password:
            user = User.query.filter_by(email=email).first()
            if user and check_password_hash(user.passwordHash, password):
                login_user(user)
                return redirect(url_for('index'))
            else:
                flash('Email или пароль введены некорректно')
        else:
            flash('Заполните поля email и пароль')
    return render_template('login.html')


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/settings', methods=['GET'])
@login_required
def settings():
    return "Settings_page"


@app.after_request
def redirect_to_signin(response):
    if response.status_code == 401:
        return redirect(url_for('login') + '?next_page=' + request.url)
    return response
