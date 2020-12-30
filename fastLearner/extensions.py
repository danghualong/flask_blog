from flask_caching import Cache
from flask_sqlalchemy import SQLAlchemy

cache = Cache()
db = SQLAlchemy()

def init_app(app):
    cache.init_app(app)
    db.init_app(app)