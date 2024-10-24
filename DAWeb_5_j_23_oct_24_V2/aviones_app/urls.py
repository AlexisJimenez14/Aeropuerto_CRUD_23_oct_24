from django.urls import path, include
from aviones_app import views

urlpatterns = [
    path("",views.listadoAviones,name="listadoAviones")
]
