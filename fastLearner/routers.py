from fastLearner.blueprints.circle import circle_bp
from fastLearner.blueprints.main import main_bp
from fastLearner.blueprints.api import api_bp

def init_app(app):
    app.register_blueprint(api_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(circle_bp,url_prefix='/circle')