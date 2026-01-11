from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Produto, Venda


@login_required
def home(request):
    return render(request, "home.html")


@login_required
def caixa(request):
    return render(request, "caixa.html")


@login_required
def nova_venda(request):
    produtos = Produto.objects.all()

    if request.method == "POST":
        produto_id = request.POST.get("produto")
        quantidade = int(request.POST.get("quantidade"))

        produto = Produto.objects.get(id=produto_id)

        Venda.objects.create(
            produto=produto,
            quantidade=quantidade,
            preco_unitario=produto.preco
        )

        produto.quantidade -= quantidade
        produto.save()

        return redirect("/caixa/")

    return render(request, "nova_venda.html", {"produtos": produtos})
