
class NormalResult(object):
    def __init__(self, payload,code=200,message=None):
        self.payload = payload
        self.code = code
        self.message = message

class DHLException(Exception):
    def __init__(self,message,code=500):
        self.message=message[0] if message and len(message)>0 else ''
        self.code=code