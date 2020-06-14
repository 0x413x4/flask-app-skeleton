from app import create_app, db
from app.models.user import User
from app.models.project import Project
from config import Config


app = create_app(Config)


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Project': Project}
