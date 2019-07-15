from flask import Flask,render_template
from blueprints.circle import circle_bp

def createApp():
    app=Flask(__name__)
    initBlueprints(app)
    initErrorHandlers(app)
    return app

def initBlueprints(app):
    app.register_blueprint(circle_bp,url_prefix='/circle')

def initErrorHandlers(app):
    @app.errorhandler(404)
    def nofound(code):
        return render_template('nofound.html'),404

if __name__=='__main__':
    app=createApp()
    app.run()