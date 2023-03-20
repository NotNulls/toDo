from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField,SelectField, DateField, SubmitField
from wtforms.validators import DataRequired


class TodoForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    due_date = DateField('Due Date', validators=[DataRequired()])
    status = SelectField('Status', choices=[('Complete', 'Complete'), ('Not Started', 'Not Started ')])
    submit = SubmitField('Add Task')

class EditTodoForm(FlaskForm):
    task_name = StringField('Name', validators=[DataRequired()])
    due_date = DateField('Due Date', validators=[DataRequired()])
    status = SelectField('Status', choices=[('COMPLETED', 'COMPLETED'), ('NOTSTARTED', 'NOTSTARTED')])
    submit = SubmitField('Edit Task')