from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from rest_framework.decorators import api_view
import json

from .business_logic import *

# Create your views here.

@api_view(["GET"])
def index(request):
    try:
        data = getUsers()
        return HttpResponse(data, content_type='application/json')
    except Exception as e:
        return HttpResponse(f'Ann error occured: {str(e)}', status=500)

@api_view(["POST"])
def register(request):
    try:
        data = json.loads(request.body.decode("utf-8"))
        registerUser(data)
        return HttpResponse(status=204)
    except ValueError as e:
        return HttpResponse(str(e), status=409)
    except Exception as e:
        return HttpResponse(f'An error occured: {str(e)}', status=500)
    
@api_view(['POST'])
def login(request):
    try:
        data = json.loads(request.body.decode("utf-8"))
        loginUser(data)
        return HttpResponse(status=204)
    except ValueError as e:
        return HttpResponse(f'These fields are empty: {str(e)} ', status=400)
    except ValidationError as e:
        return HttpResponse('Credentials are incorrect, please check if you entered the correct username or password!', status=401)
    except ObjectDoesNotExist as e:
        return HttpResponse('User with the given username does not exist', status=404)
    except Exception as e:
         return HttpResponse(f'An error occured: {str(e)}', status=500)

