from django.shortcuts import render, redirect
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
from django.utils.timezone import now
from django.db.models import Sum
from .models import Venda

def area_caixa(request):
    hoje = now().date()
    total = Venda.objects.filter(data__date=hoje).aggregate(Sum('total'))['total__sum'] or 0

    return render(request, "caixa_dashboard.html", {
        "vendas_hoje": total
    })


@login_required
def nova_venda(request):
    produtos = Produto.objects.filter(stock__gt=0)

    if request.method == "POST":
        produto = Produto.objects.get(id=request.POST["produto"])
        quantidade = int(request.POST["quantidade"])
        cliente = request.POST.get("cliente", "")
        forma = request.POST["forma_pagamento"]

        if quantidade > produto.stock:
            return render(request, "nova_venda.html", {
                "produtos": produtos,
                "erro": "Stock insuficiente"
            })

        total = quantidade * produto.preco

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

        return redirect("/caixa/historico/")

    return render(request, "nova_venda.html", {"produtos": produtos})


@login_required
def historico_vendas(request):
    vendas = Venda.objects.all().order_by("-data")
    return render(request, "historico_vendas.html", {"vendas": vendas})


from .models import Venda

def lista_recibos(request):
    vendas = Venda.objects.all().order_by("-data")
    return render(request, "lista_recibos.html", {"vendas": vendas})


def emitir_recibo(request, venda_id):
    venda = Venda.objects.get(id=venda_id)
    return render(request, "recibo.html", {"venda": venda})

