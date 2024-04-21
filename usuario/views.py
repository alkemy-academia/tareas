from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect(reverse("index"))
        else:
            return render(request, 'usuario/login.html', {"msj": "Credenciales incorrectas"})
    return render(request, 'usuario/login.html')


def logout_view(request):
    logout(request)
    return redirect(reverse('index'))

