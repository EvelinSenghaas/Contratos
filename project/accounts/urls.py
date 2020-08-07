from django.urls import path
from .views import *
from . import views
urlpatterns = [
    path('signup/',views.SignUp.as_view(),name="signup"), 
    # path('validarNombre/',validarNombre,name="validarNombre"), 
]