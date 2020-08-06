from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
#In delete i don't have validations
#@login_required
def Home(request):
    #Tengo que ver de recuperar el ultimo registro de asistencia por reunion, si pasaron mas de 7 dias 
    #y no hubo un registro, ponerle falta al encargado
    #usuario = request.user
    #context = {'usuario':usuario}
    #return render(request,'index.html',context)
    return render(request,'index.html')

def gestionarContrato(request):
    if request.method == 'POST':
        if 'btn-agregar' in request.POST:
            contrato_form = ContratoForm(request.POST)
            if contrato_form.is_valid():
                contrato_form.changeReason="Creacion"
                contrato_form.save()
                print('guarde')
            else:
                print('error')
    contrato_form = ContratoForm()
    contratos=Contrato.objects.all()
    context = {'contrato_form':contrato_form,'contratos':contratos}
    return render(request,'gestionarContrato.html',context)

def editarContrato(request,id):
    contrato=Contrato.objects.get(id=id)
    if request.method == 'GET':
        contrato_form = ContratoForm(instance = contrato)
        context = {'contrato_form':contrato_form}
        return render(request,'editarContrato.html',context)
    else:
        contrato_form=ContratoForm(request.POST,instance=contrato)
        if contrato_form.is_valid():
            contrato=contrato_form.save(commit=False)
            contrato.changeReason="Modificacion"
            contrato.save()
    return redirect('/contratos/gestionarContrato')

def eliminarContrato(request,id):
    contrato=Contrato.objects.get(id=id)
    contrato.changeReason="Eliminacion"
    contrato.delete()
    return redirect('/contratos/gestionarContrato')

def gestionarSolicitantes(request):
    if request.method == 'POST':
        solicitante_form = SolicitanteForm(request.POST)
        if solicitante_form.is_valid():
            solicitante_form.changeReason="Creacion"
            solicitante_form.save()
        else:
            print('error')
    solicitante_form = SolicitanteForm()
    solicitantes=Solicitante.objects.all()
    context = {'solicitante_form':solicitante_form,'solicitantes':solicitantes}
    return render(request,'gestionarSolicitantes.html',context)

def editarSolicitante(request,id):
    solicitante=Solicitante.objects.get(id=id)
    if request.method == 'GET':
        solicitante_form = SolicitanteForm(instance = solicitante)
        context = {'solicitante_form':solicitante_form}
        return render(request,'editarSolicitante.html',context)
    else:
        solicitante_form=SolicitanteForm(request.POST,instance=solicitante)
        if solicitante_form.is_valid():
            solicitante=solicitante_form.save(commit=False)
            solicitante.changeReason="Modificacion"
            solicitante.save()
    return redirect('/contratos/gestionarSolicitantes')

def eliminarSolicitante(request,id):
    solicitante=Solicitante.objects.get(id=id)
    solicitante.changeReason="Eliminacion"
    solicitante.delete()
    return redirect('/contratos/gestionarSolicitantes')

def gestionarObjetos(request):
    if request.method == 'POST':
        objeto_form = ObjetoForm(request.POST)
        if objeto_form.is_valid():
            objeto_form.changeReason="Creacion"
            objeto_form.save()
        else:
            print('error')
    objeto_form = ObjetoForm()
    objetos=Objeto.objects.all()
    context = {'objeto_form':objeto_form,'objetos':objetos}
    return render(request,'gestionarObjetos.html',context)

def editarObjeto(request,id):
    objeto=Objeto.objects.get(id=id)
    if request.method == 'GET':
        objeto_form = ObjetoForm(instance = objeto)
        context = {'objeto_form':objeto_form}
        return render(request,'editarObjeto.html',context)
    else:
        objeto_form=ObjetoForm(request.POST,instance=objeto)
        if objeto_form.is_valid():
            objeto=objeto_form.save(commit=False)
            objeto.changeReason="Modificacion"
            objeto.save()
    return redirect('/contratos/gestionarObjetos')

def eliminarObjeto(request,id):
    objeto=Objeto.objects.get(id=id)
    objeto.changeReason="Eliminacion"
    objeto.delete()
    return redirect('/contratos/gestionarObjetos')

def gestionarEstados(request):
    if request.method == 'POST':
        estado_form = EstadoForm(request.POST)
        if estado_form.is_valid():
            estado_form.changeReason="Creacion"
            estado_form.save()
        else:
            print('error')
        
    estado_form = EstadoForm()
    estados = Estado.objects.all()
    context = {'estado_form':estado_form,'estados':estados}
    return render(request,'gestionarEstados.html',context)

def editarEstado(request,id):
    estado=Estado.objects.get(id=id)
    if request.method == 'GET':
        estado_form = EstadoForm(instance = estado)
        context = {'estado_form':estado_form}
        return render(request,'editarEstado.html',context)
    else:
        estado_form=EstadoForm(request.POST,instance=estado)
        if estado_form.is_valid():
            estado=estado_form.save(commit=False)
            estado.changeReason="Modificacion"
            estado.save()
    return redirect('/contratos/gestionarEstados')

def eliminarEstado(request,id):
    estado=Estado.objects.get(id=id)
    estado.changeReason="Eliminacion"
    estado.delete()
    return redirect('/contratos/gestionarEstados')

def auditoriaContratos(request):
    if permiso(request, 42):
        auditoria_contrato = Contrato.history.all()
        context = {'auditoria_contrato': auditoria_contrato}
        return render(request, 'sistema/auditoriaContratos.html', context)
    else:
        return redirect('home')