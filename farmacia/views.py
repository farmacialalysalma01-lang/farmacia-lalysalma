from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from .models import Produto, Venda, ItemVenda


# =======================
# LOGIN / LOGOUT
# =======================

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect("caixa")

    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect("login")


# =======================
# CAIXA
# =======================

@login_required
def area_caixa(request):
    return render(request, "caixa.html")


# =======================
# NOVA VENDA
# =======================

@login_required
def nova_venda(request):
    produtos = Produto.objects.all()

    if request.method == "POST":
        produto_id = request.POST.get("produto")
        quantidade = int(request.POST.get("quantidade"))

        carrinho = request.session.get("carrinho", {})

        if produto_id in carrinho:
            carrinho[produto_id] += quantidade
        else:
            carrinho[produto_id] = quantidade

        request.session["carrinho"] = carrinho
        return redirect("nova_venda")

    carrinho = request.session.get("carrinho", {})
    itens = []
    total = 0

    for pid, qtd in carrinho.items():
        produto = Produto.objects.get(id=pid)
        subtotal = produto.preco * qtd
        total += subtotal
        itens.append({
            "produto": produto,
            "quantidade": qtd,
            "subtotal": subtotal
        })

    return render(request, "nova_venda.html", {
        "produtos": produtos,
        "itens": itens,
        "total": total
    })


# =======================
# FINALIZAR VENDA
# =======================

@login_required
def finalizar_venda(request):
    carrinho = request.session.get("carrinho", {})

    if not carrinho:
        return redirect("nova_venda")

    venda = Venda.objects.create(data=now(), total=0)

    total = 0
    for pid, qtd in carrinho.items():
        produto = Produto.objects.get(id=pid)
        subtotal = produto.preco * qtd

        ItemVenda.objects.create(
            venda=venda,
            produto=produto,
            quantidade=qtd,
            preco=produto.preco
        )

        produto.stock -= qtd
        produto.save()

        total += subtotal

    venda.total = total
    venda.save()

    request.session["carrinho"] = {}

    return redirect("emitir_recibo", venda_id=venda.id)


# =======================
# HISTÓRICO DE VENDAS
# =======================

@login_required
def historico_vendas(request):
    vendas = Venda.objects.all().order_by("-data")
    return render(request, "historico_vendas.html", {"vendas": vendas})


# =======================
# EMITIR RECIBO
# =======================

@login_required
def emitir_recibo(request, venda_id):
    venda = get_object_or_404(Venda, id=venda_id)
    itens = ItemVenda.objects.filter(venda=venda)

    return render(request, "emitir_recibo.html", {
        "venda": venda,
        "itens": itens
    })
