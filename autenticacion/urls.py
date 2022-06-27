from django.urls import path

from .views import VRegistro, cerrar_sesion, log



urlpatterns = [
    
    path('', VRegistro.as_view(), name="Autenticacion"),

    path('cerrar_sesion', cerrar_sesion, name="cerrar_sesion"),

    path('log', log, name="log"),


]


