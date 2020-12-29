from fastLearner.blueprints.circle import circle_bp
from fastLearner.blueprints.main import main_bp
from fastLearner.blueprints.common import common_bp

def init_app(app):
    app.register_blueprint(common_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(circle_bp,url_prefix='/circle')