from django.db import models

# Create your models here.
class Aviones(models.Model):
    codigo= models.CharField(primary_key=True, max_length=6) 
    nombre=models.CharField(max_length=50)
    noasajeros= models.IntegerField()
    
    
    
    