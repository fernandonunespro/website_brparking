from django.shortcuts import render, redirect
from .forms import PessoaForm
from django.http import HttpResponse
from .models import (
    Pessoa,
    Veiculo,
    MovRotativo,
    Mensalista,
    MovMensalista
)

from .forms import (
    PessoaForm,
    VeiculoForm,
    MovRotativoForm,
    MensalistaForm,
    MovMensalistaForm
)

def home(request):
    context = {'mensagem': 'Ola mundo...'}
    return render(request, 'core/index.html', context)

def lista_pessoas(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core_lista_pessoas')
    else:
        form = PessoaForm()
    pessoas = Pessoa.objects.all()
    data = {'pessoas': pessoas, 'form': form}
    return render(request, 'core/lista_pessoas.html', data)


def pessoa_novo(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core_lista_pessoas')
    else:
        form = PessoaForm()
    return render(request, 'core/pessoa_novo.html', {'form': form})

def pessoa_update(request, id):
    pessoa = Pessoa.objects.get(id=id)
    if request.method == 'POST':
        form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            form.save()
            return redirect('core_lista_pessoas')
    else:
        form = PessoaForm(instance=pessoa)
    context = {
        'form': form,
        'pessoa': pessoa,
    }
    return render(request, 'core/pessoa_update.html', context)

def pessoa_delete(request,id ):
    pessoa = Pessoa.objects.get(id=id)
    if request.method == 'POST':
        pessoa.delete()
        return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': pessoa})

def lista_veiculos(request):
    form = VeiculoForm()
    veiculos = Veiculo.objects.all()
    data = {'veiculos': veiculos, 'form': form}
    return render(request, 'core/lista_veiculos.html', data)

def veiculo_novo(request):
    if request.method == 'POST':
        form = VeiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core_lista_veiculos')
    else:
        form = VeiculoForm()
    return render(request, 'core/veiculo_novo.html', {'form': form})



def veiculo_update(request, id):
    veiculo = Veiculo.objects.get(id=id)
    if request.method == 'POST':
        form = VeiculoForm(request.POST, instance=veiculo)
        if form.is_valid():
            form.save()
            return redirect('core_lista_veiculos')
    else:
        form = VeiculoForm(instance=veiculo)
    context = {
        'form': form,
        'veiculo': veiculo,
    }
    return render(request, 'core/veiculo_update.html', context)

def veiculo_delete(request,id ):
    veiculo = Veiculo.objects.get(id=id)
    if request.method == 'POST':
        veiculo.delete()
        return redirect('core_lista_veiculos')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': veiculo})

def lista_movrotativos(request):
    mov_rot = MovRotativo.objects.all()
    form = MovRotativoForm()
    data = {'form': form, 'mov_rot': mov_rot}
    return render(
        request, 'core/lista_movrotativos.html', data)

def movrotativos_novo(request):
    form = MovRotativoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_movrotativos')

def movrotativos_update(request, id):
    mov_rotativo = MovRotativo.objects.get(id=id)
    if request.method == 'POST':
        form = MovRotativoForm(request.POST, instance=mov_rotativo)
        if form.is_valid():
            form.save()
            return redirect('core_lista_movrotativos')
    else:
        form = MovRotativoForm(instance=mov_rotativo)
    context = {
        'form': form,
        'mov_rotativo': mov_rotativo,
        'mov_rot': MovRotativo.objects.all(),
    }
    return render(request, 'core/movrotativos_update.html', context)

def movrotativos_delete(request,id ):
    mov_rotativo = MovRotativo.objects.get(id=id)
    if request.method == 'POST':
        mov_rotativo.delete()
        return redirect('core_lista_movrotativos')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': mov_rotativo})

def lista_mensalista(request):
    mensalistas = Mensalista.objects.all()
    form = MensalistaForm()
    data = {'mensalistas': mensalistas, 'form': form}
    return render(request, 'core/lista_mensalistas.html', data)

def mensalista_novo(request):
    if request.method == 'POST':
        form = MensalistaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core_lista_mensalista')
    else:
        form = MensalistaForm()
    return render(request, 'core/mensalista_novo.html', {'form': form})

def mensalista_update(request, id):
    mensalista = Mensalista.objects.get(id=id)
    if request.method == 'POST':
        form = MensalistaForm(request.POST, instance=mensalista)
        if form.is_valid():
            form.save()
            return redirect('core_lista_mensalista')
    else:
        form = MensalistaForm(instance=mensalista)
    context = {
        'form': form,
        'mensalista': mensalista,
        'mensalistas': Mensalista.objects.all(),
    }
    return render(request, 'core/mensalista_update.html', context)

def mensalista_delete(request,id ):
    mensalista = Mensalista.objects.get(id=id)
    if request.method == 'POST':
        mensalista.delete()
        return redirect('core_lista_mensalista')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': mensalista})

def lista_movmensalista(request):
    mov_mensalistas = MovMensalista.objects.all()
    form = MovMensalistaForm()
    data = {'form': form, 'mov_mensalistas': mov_mensalistas}
    return render(
        request, 'core/lista_movmensalistas.html', data)

def movmensalista_novo(request):
    if request.method == 'POST':
        form = MovMensalistaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core_lista_movmensalista')
    else:
        form = MovMensalistaForm()
    mov_mensalistas = MovMensalista.objects.all()
    return render(request, 'core/mov_mensal_novo.html',
                  {'form': form, 'mov_mensalistas': mov_mensalistas})

def movmensalista_update(request, id):
    mov_mensalista = MovMensalista.objects.get(id=id)
    if request.method == 'POST':
        form = MovMensalistaForm(request.POST, instance=mov_mensalista)
        if form.is_valid():
            form.save()
            return redirect('core_lista_movmensalista')
    else:
        form = MovMensalistaForm(instance=mov_mensalista)
    context = {
        'form': form,
        'mov_mensalista': mov_mensalista,
        'mov_mensalistas': MovMensalista.objects.all(),
    }
    return render(request, 'core/movmensalista_update.html', context)


def movmensalista_delete(request,id ):
    mov_mensalista = MovMensalista.objects.get(id=id)
    if request.method == 'POST':
        mov_mensalista.delete()
        return redirect('core_lista_movmensalista')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': mov_mensalista})
