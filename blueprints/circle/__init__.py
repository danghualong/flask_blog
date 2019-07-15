
from flask import Blueprint

circle_bp=Blueprint('circle',__name__,static_folder='circleStatic',template_folder='templates')

#导入包中的其他模块
from . import controller