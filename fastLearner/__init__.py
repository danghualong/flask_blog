
import os
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask,render_template
from fastLearner.blueprints.circle import circle_bp
from fastLearner.blueprints.main import main_bp
from fastLearner.blueprints.common import common_bp
from .extensions import cache,db
from .settings import configs

baseDir=os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

def createApp(configName=None):
    app=Flask(__name__)
    if configName is None:
        configName=os.getenv('FLASK_ENV','development')
    app.config.from_object(configs[configName])
    registerLogging(app)
    registerBlueprints(app)
    registerErrorHandlers(app)
    registerExtensions(app)
    registerAfterRequest(app)
    return app

def registerLogging(app):
    formatter = logging.Formatter('[%(asctime)s][%(levelname)s] %(filename)s--%(funcName)s(%(lineno)s):%(message)s')
    fh=RotatingFileHandler(os.path.join(baseDir,'logs/mylog.log'),maxBytes=10*1024*1024,backupCount=5)
    fh.setLevel(logging.INFO)
    fh.setFormatter(formatter)
    app.logger.addHandler(fh)

def registerBlueprints(app):
    app.register_blueprint(common_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(circle_bp,url_prefix='/circle')

def registerErrorHandlers(app):
    @app.errorhandler(404)
    def nofound(code):
        return render_template('nofound.html'),404

def registerExtensions(app):
    cache.init_app(app)
    db.init_app(app)

def registerAfterRequest(app):
    @app.after_request
    def afterRequest(resp):
        resp.headers['Access-Control-Allow-Origin'] = '*'
        # resp.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, DELETE"
        resp.headers["Access-Control-Allow-Headers"] = "token,userId,openUserId,xcm_admin_token,Content-Type,x-requested-with"
        return resp
        