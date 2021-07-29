class ApiResult:
    
    content = {
        'data':{},
        'isSuccess':True,
        'statusCode':0,
        'message':"ok", 
    }
    content_pagination = {
        'data':{},
        'isSuccess':True,
        'statusCode':0,
        'message':"ok", 
        'next': None,
        'previous': None,
        'count': None,
    }
    status = {
        'isSuccess':True,
        'statusCode':0,
        'message':"ok", 
    }
    Badstatus = {
        'isSuccess':False,
        'statusCode':1,
        'message':"Bad Request", 
    }


def convert_to_timestamp(Time):
    try :
        t=int(Time.timestamp())
        return t
    except:
        return 0