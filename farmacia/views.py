from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Produto, Venda

# ---------- LOGIN ----------
def login_view(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"]
        )
        if user:
            login(request, user)

            if user.groups.filter(name="CAIXA").exists():
                return redirect("caixa")

            return redirect("/admin/")
        else:
            return render(request, "login.html", {"error": "Credenciais inválidas"})

    return render(request, "login.html")

def logout_view(request):
    logout(request)
    return redirect("login")

# ---------- CAIXA ----------
@login_required
def caixa_dashboard(request):
    return render(request, "caixa_dashboard.html")

@login_required
def nova_venda(request):
    produtos = Produto.objects.all()

    if request.method == "POST":
        produto = Produto.objects.get(id=request.POST["produto"])
        quantidade = int(request.POST["quantidade"])
        cliente = request.POST.get("cliente", "")
        forma = request.POST["forma"]

        total = produto.preco * quantidade

        Venda.objects.create(
            produto=produto,
            quantidade=quantidade,
            preco_unitario=produto.preco,
            total=total,
            cliente=cliente,
            forma_pagamento=forma,
            operador=request.user
        )

        produto.stock -= quantidade
        produto.save()

        return redirect("historico_vendas")

    return render(request, "nova_venda.html", {"produtos": produtos})

@login_required
def historico_vendas(request):
    vendas = Venda.objects.order_by("-data")
    return render(request, "historico_vendas.html", {"vendas": vendas})

@login_required
def emitir_recibo(request, venda_id):
    venda = get_object_or_404(Venda, id=venda_id)
    return render(request, "recibo.html", {"venda": venda})
