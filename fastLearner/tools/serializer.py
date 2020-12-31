from sqlalchemy.orm import class_mapper

def serialize(model):
    if (isinstance(model, list) or isinstance(model,tuple)):
        result = []
        for item in model:
            result.append(serialize(item))
        return result
    else:
        columnNames = [c.key for c in class_mapper(model.__class__).columns]
        t=[]
        for c in columnNames:
            data = getattr(model, c)
            if(_isRegularData(data)):
                t.append((c, data))
            else:
                t.append((c, serialize(data)))
        return dict(t)

def _isRegularData(item):
    return (isinstance(item, int) or
    isinstance(item, float) or
    isinstance(item, type(None)) or
    isinstance(item, str) or
    isinstance(item, bool))