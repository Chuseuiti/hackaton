from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
import json
# Create your views here.
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from registration.models import Token
from information.models import Documents, Security

def document_encrypt(request):

    body = request.GET

    username = body.get('username')
    token = body.get('token')

    try:
        Token.objects.filter(username=username,token=token)
    except:
        return HttpResponse(json.dumps({'response':'Token not registered'}), status = 200)
    # Save encrypt information in database
    return HttpResponse(json.dumps({'response':'Documents encrypted saved on the database.'}), status = 200)

def document_raw(request):
    body = request.GET

    username = body.get('username')
    token = body.get('token')

    try:
        Token.objects.filter(username=username,token=token)
    except:
        return HttpResponse(json.dumps({'response':'Token not registered'}), status = 200)
    # generate private/public key pair
    key = rsa.generate_private_key(backend=default_backend(), public_exponent=65537, \
    key_size=2048)

    # Get public key in OpenSSH format
    public_key = key.public_key().public_bytes(serialization.Encoding.OpenSSH, \
    serialization.PublicFormat.OpenSSH)
    print(public_key.decode('utf-8'))
    # Get private Key 
    private_key = key.private_bytes(encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption())
    print(private_key.decode('utf-8'))

    # Get private key from the database for the user
    message = b"Example of the encrypted information provide by the client upon "
    ciphertext = key.public_key().encrypt(
         message,
         padding.OAEP(
             mgf=padding.MGF1(algorithm=hashes.SHA1()),
             algorithm=hashes.SHA1(),
             label=None
         )
    )

    # Decrypt information
    plaintext = key.decrypt(
         ciphertext,
         padding.OAEP(
             mgf=padding.MGF1(algorithm=hashes.SHA1()),
             algorithm=hashes.SHA1(),
             label=None
         )
     )
    print(plaintext)    
    q = Documents(username=username, document=plaintext)
    q.save()
    return HttpResponse(json.dumps({'response':'Documents correctly unencrypted.'}), status = 200)

def information_request(request):
    body = request.GET

    username = body.get('username')
    token = body.get('token')
    try:
        Token.objects.filter(username=username,token=token)
    except:
        return HttpResponse(json.dumps({'response':'Token not registered'}), status = 200)

    # generate private/public key pair
    key = rsa.generate_private_key(backend=default_backend(), public_exponent=65537, \
    key_size=2048)

    # Get public key in OpenSSH format
    public_key = key.public_key().public_bytes(serialization.Encoding.OpenSSH, \
    serialization.PublicFormat.OpenSSH)
    print(public_key.decode('utf-8'))
    # Get private Key 
    private_key = key.private_bytes(encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption())
    print(private_key.decode('utf-8'))

    # Save in database
    q = Security(username=username,private_key=private_key.decode('utf-8'),public_key=public_key.decode('utf-8'))
    q.save()
    return HttpResponse(json.dumps({'response':'home_address', 'message':'Please provide the information requested.','public_key':public_key.decode('utf-8')}), status = 200)


