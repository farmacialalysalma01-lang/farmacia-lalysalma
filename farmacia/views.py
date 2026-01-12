from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Produto, Venda
from django.utils.timezone import now
from decimal import Decimal

# ---------------------------
# LOGIN
# ---------------------------
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
        else:
            messages.error(request, "Login inválido")
    return render(request, "login.html")

def logout_view(request):
    logout(request)
    return redirect("/")

# ---------------------------
# CAIXA
# ---------------------------
@login_required
def area_caixa(request):
    total = Venda.objects.filter(data__date=now().date()).aggregate(
        total=models.Sum("total")
    )["total"] or 0

    return render(request, "caixa_dashboard.html", {
        "total": total
    })

# ---------------------------
# NOVA VENDA
# ---------------------------
@login_required
def nova_venda(request):
    produtos = Produto.objects.all()
    return render(request, "nova_venda.html", {
        "produtos": produtos
    })

# ---------------------------
# FINALIZAR VENDA (MULTI PRODUTO)
# ---------------------------
@login_required
def finalizar_venda(request):
    if request.method != "POST":
        return redirect("/caixa/")

    produtos_ids = request.POST.getlist("produto[]")
    quantidades = request.POST.getlist("quantidade[]")
    forma = request.POST.get("forma_pagamento")

    if not produtos_ids:
        messages.error(request, "Nenhum produto selecionado")
        return redirect("/nova-venda/")

    for i in range(len(produtos_ids)):
        produto = Produto.objects.get(id=produtos_ids[i])
        quantidade = int(quantidades[i])

        if produto.stock < quantidade:
            messages.error(request, f"Stock insuficiente: {produto.nome}")
            return redirect("/nova-venda/")

        total = Decimal(produto.preco) * Decimal(quantidade)

        # cria venda
        Venda.objects.create(
            produto=produto,
            quantidade=quantidade,
            preco_unitario=produto.preco,
            total=total,
            forma_pagamento=forma,
            operador=request.user
        )

        # baixa stock
        produto.stock -= quantidade
        produto.save()

    messages.success(request, "Venda registada com sucesso")
    return redirect("/caixa/")
