from .cache_ext import cache
from .db_ext import db

def init_app(app):
    cache.init_app(app)
    db.init_app(app)