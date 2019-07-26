
from flask import Flask,render_template
from fastLearner.blueprints.circle import circle_bp
from fastLearner.blueprints.main import main_bp
from .extensions import cache


def createApp():
    app=Flask(__name__)
    app.config.from_pyfile('config.py')
    initBlueprints(app)
    initErrorHandlers(app)
    initExtensions(app)
    return app

def initBlueprints(app):
    app.register_blueprint(main_bp)
    app.register_blueprint(circle_bp,url_prefix='/circle')

def initErrorHandlers(app):
    @app.errorhandler(404)
    def nofound(code):
        return render_template('nofound.html'),404

def initExtensions(app):
    cache.init_app(app)
    
        