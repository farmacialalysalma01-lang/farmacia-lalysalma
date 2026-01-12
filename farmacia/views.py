from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Produto, Venda


# 🔐 LOGIN
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)

            if user.groups.filter(name="CAIXA").exists():
                return redirect("caixa")
            elif user.groups.filter(name="GERENTE").exists():
                return redirect("gerente")
            elif user.groups.filter(name="FARMACEUTICO").exists():
                return redirect("farmaceutico")
            else:
                return redirect("admin:index")

        return render(request, "login.html", {"erro": "Credenciais inválidas"})

    return render(request, "login.html")


# 🚪 LOGOUT
def logout_view(request):
    logout(request)
    return redirect("login")


# 🧾 CAIXA
@login_required
def caixa(request):
    return render(request, "caixa.html")


# 💰 NOVA VENDA
@login_required
def nova_venda(request):
    produtos = Produto.objects.filter(quantidade__gt=0)

    if request.method == "POST":
        produto_id = request.POST["produto"]
        quantidade = int(request.POST["quantidade"])
        cliente = request.POST["cliente"]
        forma_pagamento = request.POST["forma_pagamento"]

        produto = Produto.objects.get(id=produto_id)

        total = quantidade * produto.preco

        Venda.objects.create(
            produto=produto,
            quantidade=quantidade,
            preco_unitario=produto.preco,
            total=total,
            cliente=cliente,
            forma_pagamento=forma_pagamento,
            operador=request.user
        )

        produto.quantidade -= quantidade
        produto.save()

        return redirect("historico_vendas")

    return render(request, "nova_venda.html", {"produtos": produtos})


# 📜 HISTÓRICO
@login_required
def historico_vendas(request):
    vendas = Venda.objects.all().order_by("-data")
    return render(request, "historico_vendas.html", {"vendas": vendas})
