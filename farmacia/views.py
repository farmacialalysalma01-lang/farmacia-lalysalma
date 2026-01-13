from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.utils.timezone import now

from .models import Produto, Venda


# =========================
# LOGIN
# =========================

def login_view(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST.get("username"),
            password=request.POST.get("password"),
        )
        if user:
            login(request, user)
            return redirect("/caixa/")
    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect("/login/")


# =========================
# CAIXA
# =========================

@login_required
def area_caixa(request):
    total_hoje = (
        Venda.objects.filter(data__date=now().date())
        .aggregate(total=models.Sum("total"))
        .get("total")
        or 0
    )

    return render(request, "caixa.html", {
        "total_hoje": total_hoje
    })


# =========================
# NOVA VENDA
# =========================

@login_required
def nova_venda(request):
    produtos = Produto.objects.all()
    return render(request, "nova_venda.html", {"produtos": produtos})


# =========================
# FINALIZAR VENDA
# =========================

@login_required
def finalizar_venda(request):
    if request.method == "POST":
        produto_id = request.POST.get("produto")
        qtd = int(request.POST.get("quantidade", 1))

        produto = Produto.objects.get(id=produto_id)
        total = produto.preco * qtd

        Venda.objects.create(
            produto=produto,
            quantidade=qtd,
            total=total,
            data=now()
        )

        produto.stock -= qtd
        produto.save()

        return redirect("/caixa/")

    return redirect("/caixa/")
