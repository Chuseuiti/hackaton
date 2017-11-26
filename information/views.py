from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
import json
# Create your views here.


def document_encrypt(request):

	return HttpResponse(json.dumps({'response':'Documents encrypted saved on the database.'}), status = 200)

def document_raw(request):

	return HttpResponse(json.dumps({'response':'Documents correctly unencrypted.'}), status = 200)

def information_request(request):

	return HttpResponse(json.dumps({'response':'home_address', 'message':'Please provide the information requested.','public_key':'nuascgb3unugnun2348743n6234084nciin'}), status = 200)


