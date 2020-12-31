from flask import render_template,current_app,request,jsonify,make_response
from .forms import RegisterForm
from . import main_bp
from fastLearner.exceptions import NormalResult,ProjException
from fastLearner.models import User
import fastLearner.tools.serializer as serializer
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
                result = NormalResult(user)
                return jsonify(serializer.serialize(result))
        raise ProjException("用户信息不正确")
    except Exception as pe:
        raise ProjException(pe.args)
        
    

