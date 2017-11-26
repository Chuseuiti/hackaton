from django.db import models

# Create your models here.

class Authorization(models.Model):

    username = models.CharField(primary_key=True,max_length=32)
    password = models.CharField(max_length=32)

class Token(models.Model):
    #username = models.ForeignKey(Authorization, on_delete=models.CASCADE)
    username = models.CharField(primary_key=True,max_length=32)
    token = models.CharField(max_length=64)
    timestamp = models.IntegerField(default=0)
    expiration = models.IntegerField(default=3600)

