from flask import render_template

def init_app(app):
    @app.errorhandler(404)
    def nofound(code):
        return render_template('nofound.html'),404
