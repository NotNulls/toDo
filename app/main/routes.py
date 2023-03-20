from app import db
from flask import request, render_template, redirect, flash, url_for,session
from app.main import bp
from app.models import User, Task
from flask_login import current_user, login_required
from app.main.forms import TodoForm

@bp.route('/index', methods=['GET','PUT'])
@bp.route('/', methods=['GET','PUT'])
def index():
    return render_template('index.html')


@bp.route('/add_todo',  methods=["PUT","GET"])
@login_required
def add_task():
    form = TodoForm()
    if current_user.is_authenticated:
        return redirect(url_for('main.todos'))
    if request.method == "GET":
        return render_template('add_todo.html', form=form)
    if request.method == "PUT":
        user = current_user
        if form.validate_on_submit:
            todo = Task(
                task_name = form.name.data,
                due_date = form.due_date.data,
                status = form.status.data,
                todo_owner = user.id
            )
        db.session.add(todo)
        db.session.commit()
        return redirect('/todos')
    
@bp.route('/todos', methods=['GET','PUT'])
def todos():
    todos = Task.query.filter_by(todo_owner=current_user.id)
    return render_template('todos.html', todos=todos)