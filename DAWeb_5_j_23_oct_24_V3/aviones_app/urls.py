from django.urls import path, include
from aviones_app import views #importas la vista

urlpatterns = [
    path("",views.listadoAviones,name="listadoAviones")
]
