from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required

def gestionarPersonas(request):
    if request.method == 'POST':
        persona_form = PersonaForm(request.POST)
        if persona_form.is_valid():
            persona_form.changeReason="Creacion"
            persona_form.save()
        else:
            print('error')
    persona_form = PersonaForm()
    personas = Persona.objects.all()
    context = {'persona_form':persona_form,'personas':personas}
    return render(request,'gestionarPersonas.html',context)

def editarPersona(request,id):
    persona=Persona.objects.get(id=id)
    if request.method == 'GET':
        persona_form = PersonaForm(instance = persona)
        context = {'persona_form':persona_form}
        return render(request,'editarPersona.html',context)
    else:
        persona_form=PersonaForm(request.POST,instance=persona)
        if persona_form.is_valid():
            persona=persona_form.save(commit=False)
            persona.changeReason="Modificacion"
            persona.save()
    return redirect('/personas/gestionarPersonas')

def eliminarPersona(request,id):
    persona=Persona.objects.get(id=id)
    persona.changeReason="Eliminacion"
    persona.delete()
    return redirect('/personas/gestionarPersonas')

def gestionarSexos(request):
    if request.method == 'POST':
        sexo_form = SexoForm(request.POST)
        if sexo_form.is_valid():
            sexo_form.changeReason="Creacion"
            sexo_form.save()
        else:
            print('error')
    sexo_form = SexoForm()
    sexos = Sexo.objects.all()
    context = {'sexo_form':sexo_form,'sexos':sexos}
    return render(request,'gestionarSexos.html',context)

def editarSexo(request,id):
    sexo=Sexo.objects.get(id=id)
    if request.method == 'GET':
        sexo_form = SexoForm(instance = sexo)
        context = {'sexo_form':sexo_form}
        return render(request,'editarSexo.html',context)
    else:
        sexo_form=SexoForm(request.POST,instance=sexo)
        if sexo_form.is_valid():
            sexo=sexo_form.save(commit=False)
            sexo.changeReason="Modificacion"
            sexo.save()
    return redirect('/personas/gestionarSexos')

def eliminarSexo(request,id):
    sexo=Sexo.objects.get(id=id)
    sexo.changeReason="Eliminacion"
    sexo.delete()
    return redirect('/personas/gestionarSexos')

def auditoriaPersonas(request):
    if permiso(request, 42):
        auditoria_persona = Contrato.history.all()
        context = {'auditoria_persona': auditoria_persona}
        return render(request, 'sistema/auditoriaPersonas.html', context)
    else:
        return redirect('home')