
class ProjException(Exception):
    def __init__(self,message,code=500):
        self.message=message
        self.code=code

class NormalResult(object):
    def __init__(self, payload,code=200,message=None):
        self.payload = payload
        self.code = code
        self.message = message

    


