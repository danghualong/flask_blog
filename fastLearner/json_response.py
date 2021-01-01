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

class DHLException(Exception):
    def __init__(self,message,code=500):
        self.message=message[0] if message and len(message)>0 else ''
        self.code=code





    


