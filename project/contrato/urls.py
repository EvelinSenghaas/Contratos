from django.urls import path
from .views import *

urlpatterns = [
    path('gestionarContrato/',gestionarContrato,name="gestionarContrato"), 
    path('editarContrato/<int:id>',editarContrato,name="editarContrato"), 
    path('eliminarContrato/<int:id>',eliminarContrato,name="eliminarContrato"), 
    path('gestionarEstados/',gestionarEstados,name="gestionarEstados"),
    path('editarEstado/<int:id>',editarEstado,name="editarEstado"), 
    path('eliminarEstado/<int:id>',eliminarEstado,name="eliminarEstado"), 
    path('gestionarObjetos/',gestionarObjetos,name="gestionarObjetos"), 
    path('editarObjeto/<int:id>',editarObjeto,name="editarObjeto"), 
    path('eliminarObjeto/<int:id>',eliminarObjeto,name="eliminarObjeto"), 
    path('gestionarSolicitantes/',gestionarSolicitantes,name="gestionarSolicitantes"), 
    path('editarSolicitante/<int:id>',editarSolicitante,name="editarSolicitante"), 
    path('eliminarSolicitante/<int:id>',eliminarSolicitante,name="eliminarSolicitante"), 
    path('auditoria/',auditoriaContratos,name="auditoria"), 
]