from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from .models import Produto, Venda


# LOGIN
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


# ÁREA DO CAIXA
@login_required
def area_caixa(request):
    total_hoje = Venda.objects.aggregate(Sum("total"))["total__sum"] or 0
    return render(request, "caixa.html", {"total": total_hoje})


# NOVA VENDA
@login_required
def nova_venda(request):
    produtos = Produto.objects.all()
    return render(request, "nova_venda.html", {"produtos": produtos})


# FINALIZAR VENDA (💥 ESTA É A PARTE CRÍTICA)
@login_required
def finalizar_venda(request):
    if request.method == "POST":

        produto_id = request.POST.get("produto")
        quantidade = int(request.POST.get("quantidade"))

        produto = Produto.objects.get(id=produto_id)

        if quantidade > produto.stock:
            return redirect("/nova-venda/")

        total = produto.preco * quantidade

        venda = Venda.objects.create(
            produto=produto,
            quantidade=quantidade,
            total=total
        )

        produto.stock -= quantidade
        produto.save()

        request.session["ultima_venda_id"] = venda.id

        return redirect("/emitir-recibo/")

    return redirect("/caixa/")


# HISTÓRICO
@login_required
def historico_vendas(request):
    vendas = Venda.objects.order_by("-data")
    return render(request, "historico.html", {"vendas": vendas})


# RECIBO
@login_required
def emitir_recibo(request):
    venda_id = request.session.get("ultima_venda_id")
    venda = Venda.objects.get(id=venda_id)
    return render(request, "recibo.html", {"venda": venda})
