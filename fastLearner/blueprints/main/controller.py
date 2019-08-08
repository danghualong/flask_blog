from flask import render_template
from .forms import RegisterForm
from . import main_bp
from ...extensions import cache

@main_bp.route('/register')
def register():
    form=RegisterForm()
    return render_template('main/register.html',form=form)

@main_bp.route('/')
def index():
    return render_template('main/index.html')