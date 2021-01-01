import click,os
from fastLearner.extensions import db
from fastLearner.models import *
import time

# 自定义Flask命令
def init_app(app):
    if (os.getenv('FLASK_ENV', 'production') == 'production'):
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
        fakedata()
        click.echo("data faked successfully")


    def fakedata():
        if (User.query.count() != 0):
            return
        user = User(id=1,username='admin', password='123456')
        category = Category(id=11, name="食品")
        create_time=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
        post = Post(id=101, title="有机食品的营养分析", body="有机食品和普通食品的营养差异有哪些？可以通过测试发现结果",
        create_time=create_time, user_id=1, category_id=11)
        comment=Comment(id=1001,body="一派胡言",post_id=101)
        db.session.add_all([user, category, post, comment])
        db.session.commit()
