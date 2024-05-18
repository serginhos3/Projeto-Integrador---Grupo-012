from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .decorators import unauthenticated_user
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm

@login_required()
def home(request):
    return render(request, "authentication/home.html")

@unauthenticated_user
def signup(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name=request.POST.get('grupos'))
            user.groups.add(group)
            messages.success(request, 'A conta foi criada com sucesso')

    context = {'form':form}
    return render(request, "authentication/signup.html", context)

@unauthenticated_user
def signin(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Usuário ou senha errados")
        
    return render(request, "authentication/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Deslogado")
    return redirect('signin')

@login_required()
def administrador(request):
    ##context = {'form': PdfForm()}
    return render(request, "authentication/administrador.html")

@login_required()
def treinamentos(request):
    return render(request, "authentication/treinamentos.html")

@login_required()
def perfil(request):
    return render(request, "authentication/perfil.html")

@login_required()
def termos(request):
    return render(request, "authentication/termos.html")

@login_required()
def suporte(request):
    return render(request, "authentication/suporte.html")