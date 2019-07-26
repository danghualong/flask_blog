
from flask import Blueprint

main_bp=Blueprint('main',__name__,static_folder='static',template_folder='templates')

#导入包中的其他模块
from . import controller