import os
from flask import Flask
from . import logger
from .settings import configs
from .middlewares import cors,loginchecker
from . import routers
from . import extensions
from . import models
from . import errorhandlers
from .templates.util import tests,filters
from .flasktools import commands as cmd, shell_context_processors as scp


def createApp(configName=None):
    app=Flask(__name__)
    if configName is None:
        configName=os.getenv('FLASK_ENV','development')
    app.config.from_object(configs[configName])
    logger.init_app(app)
    routers.init_app(app)
    errorhandlers.init_app(app)
    loginchecker.init_app(app)
    cors.init_app(app)
    extensions.init_app(app)
    filters.init_app(app)
    tests.init_app(app)
    cmd.init_app(app)
    scp.init_app(app)
    return app
