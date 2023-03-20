from app import db
from app.auth.forms import RegisterForm, LoginForm
from flask import request, render_template, redirect, flash, url_for
from app.auth import bp
from app.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import logout_user, login_user, current_user

@bp.route('/register', methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.tasks'))
    form = RegisterForm()
    if request.method == 'GET':
        return render_template('register.html', form=form, title = 'Register')
    
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User(
                name = form.first_name.data,
                last_name = form.last_name.data,
                email = form.email.data,
                password_hash = generate_password_hash(form.password.data)
            )
        db.session.add(user)
        db.session.commit()
        return redirect (url_for('auth.login'))
    

@bp.route('/login', methods=['POST','GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit:
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(user)
            return redirect(url_for('main.todos'))
        flash ('Invalid credentials.')

    return render_template('login.html', form=form)

@bp.route('/logout', methods=["PUT","GET"])
def logout():
    logout_user
    return redirect(url_for('auth.login'))