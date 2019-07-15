from flask import Blueprint,render_template
from . import circle_bp
import os

#circle_bp=Blueprint('circle',__name__,static_folder='circleStatic',template_folder='templates')

@circle_bp.route('/')
def index():
    return render_template('circle/index2.html')