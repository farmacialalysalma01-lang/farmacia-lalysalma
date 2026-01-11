from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Produto, Venda


# -------------------------
# LOGIN
# -------------------------
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect("home")
        else:
            return render(request, "login.html", {"error": "Login inválido"})

    return render(request, "login.html")


# -------------------------
# HOME
# -------------------------
@login_required
def home(request):
    return render(request, "home.html")


# -------------------------
# ÁREA CAIXA
# -------------------------
@login_required
def area_caixa(request):
    return render(request, "caixa.html")


# -------------------------
# NOVA VENDA
# -------------------------
@login_required
def nova_venda(request):
    produtos = Produto.objects.all()

    if request.method == "POST":
        produto_id = request.POST.get("produto")
        quantidade = int(request.POST.get("quantidade"))

        produto = Produto.objects.get(id=produto_id)

        total = produto.preco * quantidade

        Venda.objects.create(
            produto=produto,
            quantidade=quantidade,
            preco_unitario=produto.preco,
            total=total,
            operador=request.user
        )

        produto.quantidade -= quantidade
        produto.save()

        return redirect("caixa")

    return render(request, "nova_venda.html", {"produtos": produtos})


# -------------------------
# LOGOUT
# -------------------------
def sair(request):
    logout(request)
    return redirect("login")
