from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Sum
from .models import Produto, Venda, ItemVenda
from django.utils import timezone


# =========================
# ÁREA DO CAIXA
# =========================
@login_required
def area_caixa(request):
    hoje = timezone.now().date()

    total = Venda.objects.filter(data__date=hoje).aggregate(Sum('total'))['total__sum']
    total = total if total else 0

    return render(request, "caixa.html", {
        "total_hoje": total
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
        forma_pagamento = request.POST.get("forma_pagamento")
        itens = request.POST.getlist("produtos[]")
        quantidades = request.POST.getlist("quantidades[]")

        if not itens:
            return redirect("nova_venda")

        venda = Venda.objects.create(
            usuario=request.user,
            forma_pagamento=forma_pagamento,
            total=0
        )

        total = 0

        for i in range(len(itens)):
            produto = Produto.objects.get(id=itens[i])
            qtd = int(quantidades[i])

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

        return redirect("emitir_recibo", venda_id=venda.id)


# =========================
# HISTÓRICO
# =========================
@login_required
def historico_vendas(request):
    vendas = Venda.objects.order_by("-data")
    return render(request, "historico.html", {"vendas": vendas})


# =========================
# RECIBO
# =========================
@login_required
def emitir_recibo(request, venda_id):
    venda = get_object_or_404(Venda, id=venda_id)
    itens = ItemVenda.objects.filter(venda=venda)

    return render(request, "recibo.html", {
        "venda": venda,
        "itens": itens
    })
