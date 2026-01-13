from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Produto, Venda
from django.db.models import Sum
from django.utils.timezone import now


@login_required
def area_caixa(request):
    total = Venda.objects.aggregate(soma=Sum("total"))["soma"] or 0
    return render(request, "caixa.html", {"total": total})


@login_required
def nova_venda(request):
    produtos = Produto.objects.all()
    return render(request, "nova_venda.html", {"produtos": produtos})


@login_required
def finalizar_venda(request):
    if request.method == "POST":
        total = float(request.POST.get("total"))
        pagamento = request.POST.get("pagamento")

        Venda.objects.create(
            total=total,
            pagamento=pagamento,
            data=now()
        )

        return redirect("/historico-vendas/")


@login_required
def historico_vendas(request):
    vendas = Venda.objects.all().order_by("-data")
    return render(request, "historico_vendas.html", {"vendas": vendas})


@login_required
def emitir_recibo(request):
    venda = Venda.objects.last()
    return render(request, "emitir_recibo.html", {"venda": venda})
