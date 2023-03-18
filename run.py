from app import create_app
from app.models import db, User, Task

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db':db, 'User':User, 'Task':Task}

if __name__ == "__main__":
    app.run(debugger=True)