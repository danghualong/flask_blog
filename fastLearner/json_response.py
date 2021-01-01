from flask import make_response
import fastLearner.tools.serializer as serializer
import json

def build_response(payload):
    result = NormalResult(payload)
    resp = make_response(json.dumps(result, cls=serializer.DHLEncoder,ensure_ascii=False))
    resp.mimetype = "application/json"
    return resp

class NormalResult(object):
    def __init__(self, payload,code=200,message=None):
        self.payload = payload
        self.code = code
        self.message = message




    


