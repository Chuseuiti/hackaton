from django.db import models
from registration.models import Authorization
# Create your models here.

class Security(models.Model):
    #username = models.ForeignKey(Authorization, on_delete=models.CASCADE)
    username = models.CharField(primary_key=True,max_length=32)
    private_key = models.CharField(max_length=500)
    public_key = models.CharField(max_length=500)

class Documents(models.Model):
    #username = models.ForeignKey(Authorization, on_delete=models.CASCADE)
    username = models.CharField(primary_key=True,max_length=32)
    document = models.CharField(max_length=2000)
