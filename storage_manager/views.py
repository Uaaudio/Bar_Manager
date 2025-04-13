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


from django.contrib.auth import authenticate, login, logout

def login_user(request):
    error = ''

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['usuario']
            senha = form.cleaned_data['senha']

            if Cliente.objects.filter(usuario=usuario, senha=senha).exists():
                return redirect('manager/')  # substitui pelo nome da página de destino
            else:
                error = 'Usuário ou senha inválidos.'
                return render(request, 'pages/login_user.html', {'form_login': form, 'error': error})

        else:
            print(form.errors)

    
    return render(request, 'pages/login_user.html', {
        'form_login': LoginForm(),
        'erro': error
    })

