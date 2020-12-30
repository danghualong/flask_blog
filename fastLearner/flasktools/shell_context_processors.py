import os
from fastLearner.extensions import db

def init_app(app):
    if (os.getenv('FLASK_ENV', 'development') != 'development'):
        return
    @app.shell_context_processor
    def shell_context():
        return {"app":app,"db":db}