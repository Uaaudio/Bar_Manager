from django.shortcuts import render,redirect
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
            return redirect('login/')
            
        else:
            print(form.errors)  # Mostra os erros do form

    return render(request, 'pages/register_user.html', {'form_register': ClienteForm()})


from django.contrib.auth import authenticate, login, logout


def login_user (request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            
            return render(request,'pages/login_user.html')
            
        else:
            print(form.errors)  # Mostra os erros do form

    return render(request, 'pages/login_user.html', {'form_login': LoginForm()})




