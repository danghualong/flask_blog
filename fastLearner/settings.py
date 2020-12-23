
import os,sys
baseDir=os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

isWin=sys.platform.startswith('win')
if isWin:
    prefix='sqlite:///'
else:
    prefix='sqlite:////'


class BaseConfig(object):
    CSRF_ENABLED=True
    SECRET_KEY = os.getenv('SECRET_KEY', 'Zench')
    CACHE_TYPE='simple'
    SQLALCHEMY_TRACK_MODIFICATIONS=False


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI=prefix+os.path.join(baseDir,'data_dev.db')
    
class TestConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI=prefix+os.path.join(baseDir,'data_test.db')

class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', prefix + os.path.join(baseDir, 'data.db'))

configs={
    'development':DevelopmentConfig,
    'test':TestConfig,
    'production':ProductionConfig
}


