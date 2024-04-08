from functools import wraps
import time
from django.contrib.sessions.models import Session 
from django.http import JsonResponse

def check_session(func):
    @wraps(func) 
    def wrapper(*args, **kwargs):
        msg= {"success": False, "message": None}

        args[0].session.clear_expired() 
        
        if 'ID' not in args[0].session.keys() : 
            msg["message"]="Unauthorized. Please login or register first!"
            return JsonResponse(msg,safe=False)
        else :  
            try :
                s = Session.objects.get(pk=args[0].session.session_key)   
                    
                if len(s.get_decoded().keys())>0:
                    result = func(*args, **kwargs)
                    return result
                else :
                    msg["message"]="Unauthorized. Please login or register first!"
                    return JsonResponse(msg,safe=False)  

            except Exception as e :
                print(e)
                msg["message"]="Something went wrong, please try again"
                return JsonResponse(msg,safe=False)               
                               
    return wrapper

