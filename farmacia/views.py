from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from django.db.models import Sum

from .models import Produto, Venda


# ============================
# LOGIN
# ============================
def login_view(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"]
        )
        if user:
            login(request, user)
            return redirect("/caixa/")
    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect("/")


# ============================
# CAIXA (DASHBOARD)
# ============================
@login_required
def area_caixa(request):
    hoje = now().date()
    total = Venda.objects.filter(data__date=hoje).aggregate(Sum("total"))["total__sum"] or 0

    return render(request, "caixa_dashboard.html", {
        "vendas_hoje": total
    })

# imports no topo
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from django.db.models import Sum
from .models import Produto, Venda


# login
def login_view(request):
    ...


def logout_view(request):
    ...


# Caixa (dashboard)
@login_required
def area_caixa(request):
    ...


# 👇 NOVA VENDA vem aqui em baixo
@login_required
def nova_venda(request):
    ...

