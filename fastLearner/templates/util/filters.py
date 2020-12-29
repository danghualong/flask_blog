
def init_app(app):
    @app.template_filter('uppercase')
    def uppercase(text):
        return text.upper()
    