from flask import Blueprint,make_response
from fastLearner.tools.serializer import DHLEncoder
import json

api_bp = Blueprint('api', __name__)

class DHLException(Exception):
    def __init__(self,message,code=500):
        self.message=message[0] if message and len(message)>0 else ''
        self.code=code

@api_bp.app_errorhandler(DHLException)
def unexpectExcpet(error):
    resp=json.dumps(error,cls=DHLEncoder,ensure_ascii=False)
    resp = make_response(resp)
    resp.mimetype = 'application/json'
    # resp.status_code=error.code
    return resp

