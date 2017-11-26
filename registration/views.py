from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.


def register(request):

	return HttpResponse(json.dumps({'response':'User registered into the system'}), status = 200)

def authentication(request):

	return HttpResponse(json.dumps({'response':'nsackueynw8c9y8cn134cnc4n8cmpq'}), status = 200)
