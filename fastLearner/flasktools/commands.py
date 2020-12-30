import click,os
from fastLearner.extensions import db

# 自定义Flask命令
def init_app(app):
    if (os.getenv('FLASK_ENV', 'development') != 'development'):
        return
    @app.cli.command("initdb")
    @click.option('--drop', help="是否删除旧数据库", is_flag=True)
    def initdb(drop):
        # 删除数据库
        if drop:
            db.drop_all()
            click.echo("delete tables successfully")
        # 创建数据库
        db.create_all()
        click.echo("create tables successfully")
