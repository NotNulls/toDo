from app import db
from flask_login import UserMixin
from app import login

class User(db.Model, UserMixin):
    __tablename__= 'user'
    id=db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(100),index=True, unique=True)
    password_hash = db.Column(db.String(100))
    todos = db.relationship('Task', backref='owner')

    def __repr__(self) -> str:
        return f'User: {self.name} {self.last_name} - {self.email}'
    
    @login.user_loader
    def load_user(id):
        return User.query.get(int(id))
    

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(200))
    due_date = db.Column(db.DateTime())
    status = db.Column(db.String(200))
    todo_owner = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self) -> str:
        return f'Task {self.task_name}{self.due_date}'