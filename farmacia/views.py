from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.contrib import messages
from .models import Produto, Venda
from decimal import Decimal


def login_view(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST.get("username"),
            password=request.POST.get("password")
        )
        if user:
            login(request, user)
            return redirect("/caixa/")
        else:
            messages.error(request, "Credenciais inválidas")

    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect("/")


@login_required
def area_caixa(request):
    total = Venda.objects.aggregate(s=Sum("total"))["s"] or 0

    return render(request, "caixa.html", {
        "total": total,
        "user": request.user
    })


@login_required
def nova_venda(request):
    produtos = Produto.objects.all()
    carrinho = request.session.get("carrinho", [])

    return render(request, "nova_venda.html", {
        "produtos": produtos,
        "carrinho": carrinho
    })


@login_required
def adicionar_produto(request):
    produto_id = request.POST.get("produto")
    quantidade = int(request.POST.get("quantidade", 1))

    produto = Produto.objects.get(id=produto_id)

    carrinho = request.session.get("carrinho", [])

    carrinho.append({
        "id": produto.id,
        "nome": produto.nome,
        "preco": float(produto.preco),
        "quantidade": quantidade
    })

    request.session["carrinho"] = carrinho

    return redirect("/nova-venda/")


@login_required
def finalizar_venda(request):
    carrinho = request.session.get("carrinho", [])

    if not carrinho:
        messages.error(request, "Carrinho vazio")
        return redirect("/nova-venda/")

    for item in carrinho:
        produto = Produto.objects.get(id=item["id"])
        quantidade = int(item["quantidade"])
        preco = Decimal(str(item["preco"]))

        if produto.stock < quantidade:
            messages.error(request, f"Stock insuficiente para {produto.nome}")
            return redirect("/nova-venda/")

        produto.stock -= quantidade
        produto.save()

        Venda.objects.create(
            produto=produto,
            quantidade=quantidade,
            preco_unitario=preco,
            total=preco * quantidade,
            operador=request.user
        )

    request.session["carrinho"] = []

    return redirect("/caixa/")
