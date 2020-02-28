from flask import Blueprint,jsonify
from fastLearner.exceptions import ProjException

common_bp=Blueprint('common',__name__)

@common_bp.app_errorhandler(ProjException)
def unexpectExcpet(error):
    resp=jsonify(error.to_dict())
    resp.status_code=error.status_code
    return resp

