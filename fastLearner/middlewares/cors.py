
def init_app(app):
    @app.after_request
    def afterRequest(resp):
        resp.headers['Access-Control-Allow-Origin'] = '*'
        # resp.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, DELETE"
        resp.headers["Access-Control-Allow-Headers"] = "token,userId,openUserId,xcm_admin_token,Content-Type,x-requested-with"
        return resp