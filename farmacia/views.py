from .models import Medicamento

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "home.html")

def login_view(request):
    erro = ""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("dashboard")
        else:
            erro = "Utilizador ou palavra-passe inválidos"

    return render(request, "login.html", {"erro": erro})

@login_required
def dashboard(request):
    total = Medicamento.objects.count()
    stock_baixo = Medicamento.objects.filter(quantidade__lte=5).count()
    total_qtd = sum(m.quantidade for m in Medicamento.objects.all())

    return render(request, "dashboard.html", {
        "total": total,
        "stock_baixo": stock_baixo,
        "total_qtd": total_qtd
    })
