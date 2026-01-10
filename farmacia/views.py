from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Página de login
def login_view(request):
    if request.method == "POST":
        user = authenticate(
            username=request.POST["username"],
            password=request.POST["password"]
        )
        if user:
            login(request, user)
            return redirect("/")
        else:
            return render(request, "login.html", {"error": "Login inválido"})
    return render(request, "login.html")

# Página principal (HOME) protegida
@login_required(login_url="/login/")
def home(request):
    return render(request, "home.html")
