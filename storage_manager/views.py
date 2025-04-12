from django.shortcuts import render
from django.http import HttpResponse
from .forms import *




# Create your views here.

def manager(request):
    if request.method == 'POST':
        form = StorageForm(request.POST)
        if form.is_valid():
            form.save()
            print('SALVO COM SUCESSO!')
        else:
            print(form.errors)  # Mostra os erros do form

    return render(request, 'pages/manager.html', {'form_storage': StorageForm()})



def register_user(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            print('USUÁRIO SALVO COM SUCESSO!')
            
        else:
            print(form.errors)  # Mostra os erros do form

    return render(request, 'pages/register_user.html', {'form_login': ClienteForm()})


