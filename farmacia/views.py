from .models import Venda, ItemVenda, Produto
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
from django.http import HttpResponse

from .models import Produto, Venda, ItemVenda


# ======================
# LOGIN
# ======================
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


# ======================
# CAIXA
# ======================
@login_required
def area_caixa(request):
    hoje = timezone.now().date()
    total = Venda.objects.filter(data__date=hoje).aggregate(total=models.Sum("total"))["total"] or 0

    return render(request, "caixa.html", {"total_hoje": total})


# ======================
# NOVA VENDA
# ======================
@login_required
def nova_venda(request):
    produtos = Produto.objects.all()

    if request.method == "POST":
        produto_id = request.POST.get("produto")
        qtd = int(request.POST.get("quantidade", 1))

        venda_id = request.session.get("venda_id")

        if not venda_id:
            venda = Venda.objects.create(usuario=request.user)
            request.session["venda_id"] = venda.id
        else:
            venda = Venda.objects.get(id=venda_id)

        produto = Produto.objects.get(id=produto_id)

        ItemVenda.objects.create(
            venda=venda,
            produto=produto,
            quantidade=qtd,
            preco=produto.preco,
        )

        return redirect("nova_venda")

    venda = None
    itens = []

    if "venda_id" in request.session:
        venda = Venda.objects.get(id=request.session["venda_id"])
        itens = venda.itens.all()

    return render(request, "nova_venda.html", {"produtos": produtos, "itens": itens})


# ======================
# FINALIZAR VENDA
# ======================
@login_required
def finalizar_venda(request):
    venda_id = request.session.get("venda_id")

    if not venda_id:
        return redirect("nova_venda")

    venda = Venda.objects.get(id=venda_id)
    venda.calcular_total()
    venda.finalizada = True
    venda.save()

    del request.session["venda_id"]

    return redirect("emitir_recibo", venda_id=venda.id)


# ======================
# HISTÓRICO
# ======================
@login_required
def historico_vendas(request):
    vendas = Venda.objects.order_by("-data")
    return render(request, "historico_vendas.html", {"vendas": vendas})


# ======================
# RECIBO
# ======================
@login_required
def emitir_recibo(request, venda_id):
    venda = get_object_or_404(Venda, id=venda_id)
    return render(request, "recibo.html", {"venda": venda})
