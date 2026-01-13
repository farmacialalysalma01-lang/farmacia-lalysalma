from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.utils.timezone import now

from .models import Produto, Venda, ItemVenda


# ---------- LOGIN ----------
def login_view(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST.get("username"),
            password=request.POST.get("password"),
        )
        if user:
            login(request, user)
            return redirect("caixa")
    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect("login")


# ---------- CAIXA ----------
@login_required
def area_caixa(request):
    total = (
        Venda.objects.filter(data__date=now().date())
        .aggregate(total=Sum("total"))["total"]
        or 0
    )

    return render(request, "caixa.html", {
        "total_hoje": total
    })


# ---------- NOVA VENDA ----------
@login_required
def nova_venda(request):
    produtos = Produto.objects.all()
    return render(request, "nova_venda.html", {"produtos": produtos})


# ---------- FINALIZAR VENDA ----------
@login_required
def finalizar_venda(request):
    if request.method != "POST":
        return redirect("nova_venda")

    produtos_ids = request.POST.getlist("produto")
    quantidades = request.POST.getlist("quantidade")

    venda = Venda.objects.create(usuario=request.user)

    total = 0

    for pid, qtd in zip(produtos_ids, quantidades):
        produto = get_object_or_404(Produto, id=pid)
        qtd = int(qtd)

        subtotal = produto.preco * qtd
        total += subtotal

        ItemVenda.objects.create(
            venda=venda,
            produto=produto,
            quantidade=qtd,
            preco=produto.preco
        )

        produto.stock -= qtd
        produto.save()

    venda.total = total
    venda.save()

    return redirect("emitir_recibo")


# ---------- HISTÓRICO ----------
@login_required
def historico_vendas(request):
    vendas = Venda.objects.all().order_by("-data")
    return render(request, "historico_vendas.html", {"vendas": vendas})


# ---------- RECIBO ----------
@login_required
def emitir_recibo(request):
    venda = Venda.objects.last()
    itens = ItemVenda.objects.filter(venda=venda)
    return render(request, "recibo.html", {
        "venda": venda,
        "itens": itens
    })
