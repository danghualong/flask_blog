from flask import render_template
from .forms import RegisterForm
from . import main_bp
from ...extensions import cache

@main_bp.route('/register')
def register():
    user=cache.get('currentUser')
    if not user:
        print("no userinfo")
    else:
        print(user)
    form=RegisterForm()
    cache.set('currentUser',{'name':'xiaoming','id':1})
    return render_template('main/register.html',form=form)