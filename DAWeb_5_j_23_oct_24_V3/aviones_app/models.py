from django.db import models

# Create your models here.
class Aviones(models.Model): #creas modelo de tu tabla con tu campo
    codigo= models.CharField(primary_key=True, max_length=6) 
    nombre=models.CharField(max_length=50)
    npasajeros= models.IntegerField()
    
    def __str__(self) -> str:
        return self.nombre
    
    
    
    
    