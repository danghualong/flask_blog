from flask import render_template,current_app,request,jsonify,make_response
from .forms import RegisterForm
from . import main_bp
from fastLearner.models import User
from fastLearner.responsefactory import create_response
from fastLearner.viewmodels import DHLException
import fastLearner.tools.encrypt as encrypt


@main_bp.route('/register')
def register():
    current_app.logger.warning('start register')
    form=RegisterForm()
    return render_template('main/register.html',form=form)

@main_bp.route('/login',methods=['Post'])
def getUsers():
    try:
        json1 = request.get_json()
        username = json1['name']
        password=json1['pwd']
        user = User.query.filter(User.username == username).first()
        if (user):
            if (password == user.password):
                return create_response(user)
        raise DHLException("用户信息不正确！")
    except Exception as pe:
        raise DHLException(pe.args)
        
    

