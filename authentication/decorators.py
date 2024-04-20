from functools import wraps
from django.http import  JsonResponse 
import jwt
from django.conf import settings 


def has_role(roles):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            token = request.GET.get('token')
            if token:
                try:
                    payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
                    role = payload.get('roles')
                    if role == roles:
                        return view_func(request,*args, **kwargs)
                    else:
                        return JsonResponse({'error':'Insufficient Permission'},status=403)
                except jwt.ExpiredSignatureError:
                    return JsonResponse({'error':'Token has expired'},status=401)
                except jwt.InvalidTokenError:
                    return JsonResponse({'error':'Token is invalid'},status=401) 
            else:
                return JsonResponse({'error':'Token is missing'},status=401)
        return wrapper
    return decorator           

