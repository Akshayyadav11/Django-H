from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=120)
    email=  models.EmailField( max_length=254)
    phone=  models.CharField(max_length=10)
    description =  models.TextField(max_length=200)
        