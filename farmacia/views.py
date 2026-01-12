from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from django.db.models import Sum
from .models import Produto, Venda
from .models import VendaItem


# ============================
# LOGIN
# ============================
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
    return redirect("/login/")


# ============================
# CAIXA (DASHBOARD)
# ============================
@login_required
def area_caixa(request):
    hoje = now().date()
    total = Venda.objects.filter(data__date=hoje).aggregate(Sum("total"))["total__sum"] or 0

    return render(request, "caixa_dashboard.html", {
        "vendas_hoje": total
    })


# ============================
# NOVA VENDA
# ============================
@login_required
def nova_venda(request):
    produtos = Produto.objects.all()
    carrinho = request.session.get("carrinho", [])

    if request.method == "POST":
        produto_id = request.POST.get("produto")
        quantidade = int(request.POST.get("quantidade"))

        produto = Produto.objects.get(id=produto_id)

        carrinho.append({
            "id": produto.id,
            "nome": produto.nome,
            "preco": float(produto.preco),
            "quantidade": quantidade,
            "total": float(produto.preco) * quantidade
        })

        request.session["carrinho"] = carrinho
        return redirect("/nova-venda/")

    total = sum(item["total"] for item in carrinho)

    return render(request, "nova_venda.html", {
        "produtos": produtos,
        "carrinho": carrinho,
        "total": total
    })
