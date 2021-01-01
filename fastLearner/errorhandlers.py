from flask import render_template, Blueprint,make_response
from .tools.serializer import DHLEncoder
from .viewmodels import DHLException
import json

def init_app(app):
    @app.errorhandler(404)
    def nofound(code):
        return render_template('nofound.html'), 404

    @app.errorhandler(DHLException)
    def unexpectExcpet(error):
        resp=json.dumps(error,cls=DHLEncoder,ensure_ascii=False)
        resp = make_response(resp)
        resp.mimetype = 'application/json'
        # resp.status_code=error.code
        return resp
