from app import db
from  app.main.forms import RegisterForm
from flask import request, render_template, redirect
from app.main import bp
from app.models import User
from werkzeug.security import generate_password_hash, check_password_hash

@bp.route('/index', methods=['GET','PUT'])
@bp.route('/', methods=['GET','PUT'])
def index():
    return 'Hello there, from the flask app.'

@bp.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()
    if request.method == 'GET':
        return render_template('register.html', form=form, title = 'Register')
    
    if request.method == 'POST':
        if form.validate_on_submit:
            user = User(
                name = form.first_name.data,
                last_name = form.last_name.data,
                email = form.email.data,
                password_hash = generate_password_hash(form.password.data)
            )
        db.session.add(user)
        db.session.commit()
        return redirect ('/login')