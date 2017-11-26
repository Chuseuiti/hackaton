from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
import random
import json
import time
# Create your views here.
from registration.models import Authorization, Token

def register(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    username = body['username']
    password = body['password']
    # Save into the system
    try:
        q = Authorization(username=username,password=password)
        q.save()
    except:
        return HttpResponse(json.dumps({'response':'User already in the system.'}), status = 200)
    q.save()
    return HttpResponse(json.dumps({'response':'User registered into the system.'}), status = 200)

def authentication(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    username = body['username']
    password = body['password']
    try:
        Authorization.objects.filter(username=username,password=password)
    except:
        return HttpResponse(json.dumps({'response':'User not in the system'}), status = 200)
    #Random number generator
    hexdigits = "0123456789ABCDEF"
    random_digits = "".join([ hexdigits[random.randint(0,0xF)] for _ in range(64) ])
    #Save into the database: Token + Timestamp + Time in seconds
    timestamp = time.time()
    expire = 3600 # seconds
    #Forward to the client
    q = Token(username=username,token=random_digits,timestamp=timestamp,expire=expire)
    return HttpResponse(json.dumps({'response':random_digits}), status = 200)
