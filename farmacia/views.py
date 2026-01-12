from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .models import Produto, Venda, ItemVenda


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
def area_caixa(request):
    total = Venda.objects.all().aggregate(models.Sum("total"))["total__sum"] or 0
    return render(request, "caixa.html", {"total": total})


@login_required
def nova_venda(request):
    produtos = Produto.objects.all()
    carrinho = request.session.get("carrinho", [])

    if request.method == "POST":
        produto_id = request.POST.get("produto")
        qtd = int(request.POST.get("quantidade", 1))
        carrinho.append({"produto": produto_id, "quantidade": qtd})
        request.session["carrinho"] = carrinho
        return redirect("/nova-venda/")

    return render(request, "nova_venda.html", {
        "produtos": produtos,
        "carrinho": carrinho
    })


@login_required
@transaction.atomic
def finalizar_venda(request):
    carrinho = request.session.get("carrinho", [])

    if not carrinho:
        return redirect("/nova-venda/")

    venda = Venda.objects.create(usuario=request.user, total=0)
    total = 0

    for item in carrinho:
        produto = Produto.objects.get(id=item["produto"])
        qtd = item["quantidade"]

        if produto.stock < qtd:
            raise Exception("Stock insuficiente")

        produto.stock -= qtd
        produto.save()

        ItemVenda.objects.create(
            venda=venda,
            produto=produto,
            quantidade=qtd,
            preco=produto.preco
        )

        total += produto.preco * qtd

    venda.total = total
    venda.save()

    request.session["carrinho"] = []

    return redirect("/emitir-recibo/")


@login_required
def historico_vendas(request):
    vendas = Venda.objects.all().order_by("-data")
    return render(request, "historico.html", {"vendas": vendas})


@login_required
def emitir_recibo(request):
    venda = Venda.objects.last()
    return render(request, "recibo.html", {"venda": venda})
