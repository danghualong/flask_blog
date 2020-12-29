
def init_app(app):
    @app.template_test('biggerThan')
    def biggerThan(a, b):
        return a>b