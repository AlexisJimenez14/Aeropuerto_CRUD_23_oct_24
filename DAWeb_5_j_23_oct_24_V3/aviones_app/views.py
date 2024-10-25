from django.shortcuts import render
from .models import Aviones#importas
# Create your views here.
def listadoAviones(request):
    losaviones=Aviones.objects.all()
    return render(request,"gestionarAviones.html",{"misaviones":losaviones})