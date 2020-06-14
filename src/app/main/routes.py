from app.main import bp
from flask import render_template
from flask_login import current_user, login_required


@bp.route('/')
@bp.route('/index')
@login_required
def index():
    projects = current_user.projects
    return render_template('index.html', title='Home', projects=projects)
