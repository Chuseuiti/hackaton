from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
import random
import json
import time
# Create your views here.


def register(request):

    # Save into the system

    return HttpResponse(json.dumps({'response':'User registered into the system'}), status = 200)

def authentication(request):

    #Random number generator
    hexdigits = "0123456789ABCDEF"
    random_digits = "".join([ hexdigits[random.randint(0,0xF)] for _ in range(64) ])
    #Save into the database: Token + Timestamp + Time in seconds
    timestamp = time.time()
    expire = 3600 # seconds
    #Forward to the client
    return HttpResponse(json.dumps({'response':random_digits}), status = 200)
