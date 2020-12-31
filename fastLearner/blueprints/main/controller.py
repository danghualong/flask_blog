from flask import render_template,current_app,request,json,make_response
from .forms import RegisterForm
from . import main_bp
from fastLearner.exceptions import ProjException
from fastLearner.models import User
import fastLearner.utils as util 

@main_bp.route('/register')
def register():
    current_app.logger.warning('start register')
    form=RegisterForm()
    return render_template('main/register.html',form=form)

@main_bp.route('/users',methods=['POST'])
def getUsers():
    try:
        # json1=json.loads(request.get_json())
        json1 = request.get_json()
        if(json1 and 'id' in json1):
            strId = str(json1["id"])
            id = int(strId)
            users = User.query.filter(User.id == id).all()
        return json.dumps(util.serialize(users))
    except Exception as pe:
        raise ProjException(pe.args,status_code=500)
        
    

