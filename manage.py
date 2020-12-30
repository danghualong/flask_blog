from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from fastLearner import createApp
from fastLearner.extensions import db


def buildManager():
    app = createApp()
    # compare_type 比较列中属性变化  
    # compare_server_type 比较默认值变化
    migrate = Migrate(app, db, compare_type=True, compare_server_default=True)
    manager = Manager(app)
    manager.add_command('db', MigrateCommand)
    return manager

if __name__ == "__main__":
    manager = buildManager()
    manager.run()