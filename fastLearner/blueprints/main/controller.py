from flask import render_template,current_app
from .forms import RegisterForm
from . import main_bp
from ...extensions import cache

@main_bp.route('/register')
def register():
    current_app.logger.warning('start register')
    form=RegisterForm()
    return render_template('main/register.html',form=form)