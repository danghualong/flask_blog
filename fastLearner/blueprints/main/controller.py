from flask import render_template,current_app,request,json,make_response
from .forms import RegisterForm
from . import main_bp
from ...extensions import cache
from fastLearner.exceptions import ProjException

def getAllUsers():
    return [{'id':1,'name':'¡ı±∏'},{'id':2,'name':'πÿ”'},{'id':3,'name':'’≈∑…'}]


@main_bp.route('/register')
def register():
    current_app.logger.warning('start register')
    form=RegisterForm()
    return render_template('main/register.html',form=form)

@main_bp.route('/users',methods=['POST'])
def getUsers():
    try:
        users=getAllUsers()
        # json1=json.loads(request.get_json())
        json1=request.get_json()
        if(json1!=None and 'id' in json1):
            strId=str(json1["id"])
            if(strId.isdigit()):
                id=int(strId) 
                users=list(filter(lambda x:x['id']==id,users))
        return json.dumps(users)
    except Exception as pe:
        raise ProjException(pe.args,status_code=500)
        
    

