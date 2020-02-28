
class ProjException(Exception):
    status_code=600
    def __init__(self,message,status_code=None,payload=None):
        self.message=message
        if(status_code is not None):
            self.status_code=status_code
        self.payload=payload
    
    def to_dict(self):
        result={}
        result['message']=self.message
        result['code']=self.status_code
        return result

