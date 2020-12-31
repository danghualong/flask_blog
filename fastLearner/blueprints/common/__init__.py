from flask import Blueprint,jsonify
from fastLearner.exceptions import ProjException
import json

common_bp=Blueprint('common',__name__)

@common_bp.app_errorhandler(ProjException)
def unexpectExcpet(error):
    resp=jsonify(error)
    resp.status_code=error.code
    return resp

