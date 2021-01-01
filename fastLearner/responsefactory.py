from flask import make_response
from fastLearner.tools.serializer import DHLEncoder
from fastLearner.viewmodels import NormalResult
import json

def create_response(payload):
    result = NormalResult(payload)
    content = json.dumps(result, cls=DHLEncoder, ensure_ascii=False)
    resp = make_response(content)
    resp.mimetype = "application/json"
    return resp