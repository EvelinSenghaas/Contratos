from django.urls import path
from .views import *

urlpatterns = [
    path('gestionarPersonas/',gestionarPersonas,name="gestionarPersonas"), 
    path('editarPersona/<int:id>',editarPersona,name="editarPersona"), 
    path('eliminarPersona/<int:id>',eliminarPersona,name="eliminarPersona"), 
    path('gestionarSexos/',gestionarSexos,name="gestionarSexo"), 
    path('editarSexo/<int:id>',editarSexo,name="editarSexo"), 
    path('eliminarSexo/<int:id>',eliminarSexo,name="eliminarSexo"), 
    path('auditoriaPersona/',auditoriaPersonas,name="auditoriaPersona"), 
]