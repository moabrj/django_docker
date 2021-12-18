from django.db import models

# Create your models here.
class User(models.Model):
    idUser = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=30, blank=False, default='')
    lastName = models.CharField(max_length=70, blank=False, default='')
    cpf = models.CharField(max_length=11, blank=False, default='')
    phone = models.CharField(max_length=11, blank=False, default='')
    email = models.CharField(max_length=200, blank=False, default='')
    addressStreet = models.CharField(max_length=40, blank=False, default='')
    addressNumber = models.CharField(max_length=8, blank=False, default='')
    addressCity = models.CharField(max_length=20, blank=False, default='')
    addressState = models.CharField(max_length=2, blank=False, default='')
    password = models.CharField(max_length=32, blank=False, default='1234')
