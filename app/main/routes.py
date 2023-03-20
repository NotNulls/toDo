from app import db
from flask import request, render_template, redirect, flash, url_for, abort
from app.main import bp
from app.models import User, Task
from flask_login import current_user, login_required
from app.main.forms import TodoForm, EditTodoForm

@bp.route('/index', methods=['GET','PUT'])
@bp.route('/', methods=['GET','PUT'])
def index():
    return render_template('index.html')


@bp.route('/add_todo',  methods=["POST","GET"])
@login_required
def add_task():
    form = TodoForm()
    if request.method == "GET":
        return render_template('add_todo.html', form=form)
    if request.method == "POST":
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
        return redirect(url_for('main.todos'))
    
@bp.route('/todos', methods=['GET','POST'])
@login_required
def todos():
    todos = Task.query.filter_by(todo_owner=current_user.id)
    return render_template('todos.html', todos=todos)

@bp.route('/edit_task/<int:id>', methods=['POST','GET'])
def edit_task(id):
    user = current_user
    form = EditTodoForm()
    task = Task.query.filter_by(id=id, todo_owner=current_user.id).first()
    print(task)

    if form.validate_on_submit():
        task.task_name = form.task_name.data
        task.due_date = form.due_date.data
        task.status = form.status.data
        db.session.commit()
        return redirect('main.todos')

    elif request.method == "GET":
        form.task_name.data = task.task_name
        form.due_date.data = task.due_date
        form.status.data = task.status
    
    return render_template('edit_todo.html', form=form, user=user)

@bp.route('/delete_task/<int:id>',methods=['GET','POST'])
def delete(id):
    task = Task.query.filter_by(id=id, todo_owner=current_user.id).first_or_404()
    if request.method == 'POST':
        if task:
            db.session.delete(task)
            db.session.commit()
            return redirect(url_for('main.todos'))
        else:
            return 404
    abort(404)

