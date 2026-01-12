from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Produto, Venda


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


@login_required
def caixa_home(request):
    return render(request, "caixa.html")


@login_required
def nova_venda(request):
    produtos = Produto.objects.all()

    if request.method == "POST":
        produto = Produto.objects.get(id=request.POST["produto"])
        quantidade = int(request.POST["quantidade"])
        cliente = request.POST.get("cliente", "")
        forma = request.POST["forma"]

        total = produto.preco * quantidade
        produto.stock -= quantidade
        produto.save()

        Venda.objects.create(
            produto=produto,
            quantidade=quantidade,
            preco_unitario=produto.preco,
            total=total,
            cliente=cliente,
            forma_pagamento=forma,
            operador=request.user
        )

        return redirect("/caixa/historico/")

    return render(request, "nova_venda.html", {"produtos": produtos})


@login_required
def historico_vendas(request):
    vendas = Venda.objects.all().order_by("-data")
    return render(request, "historico_vendas.html", {"vendas": vendas})


@login_required
def emitir_recibo(request, venda_id):
    venda = get_object_or_404(Venda, id=venda_id)
    return render(request, "recibo.html", {"venda": venda})
