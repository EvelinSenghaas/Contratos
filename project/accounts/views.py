from django.shortcuts import render

# accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponse
from django.http import JsonResponse


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
    

# def validarNombre(request):
#     nombre = request.GET.get('nombre')
#     data = {
#         'is_taken': CustomUser.objects.filter(username=nombre).exists()
#     }
#     if data['is_taken']:
#         data['error_message']  = 'Este nombre de Usuario ya existe, por favor elige otro nombre'
#     return JsonResponse(data)
