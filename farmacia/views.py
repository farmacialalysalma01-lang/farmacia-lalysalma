from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from .models import Produto, Venda, ItemVenda

def login_view(request):
    if request.method == "POST":
        user = authenticate(
            username=request.POST["username"],
            password=request.POST["password"]
        )
        if user:
            login(request, user)
            return redirect("caixa")
    return render(request, "login.html")


@login_required
def area_caixa(request):
    total = Venda.objects.aggregate(Sum("total"))["total__sum"] or 0
    return render(request, "caixa.html", {"total": total})


@login_required
def nova_venda(request):
    produtos = Produto.objects.all()
    return render(request, "nova_venda.html", {"produtos": produtos})


@login_required
def finalizar_venda(request):
    if request.method == "POST":
        pagamento = request.POST["pagamento"]
        venda = Venda.objects.create(
            operador=request.user,
            total=0,
            pagamento=pagamento
        )

        total = 0
        for key in request.POST:
            if key.startswith("produto_"):
                pid = key.replace("produto_", "")
                qtd = int(request.POST[key])
                produto = Produto.objects.get(id=pid)

                ItemVenda.objects.create(
                    venda=venda,
                    produto=produto,
                    quantidade=qtd,
                    preco=produto.preco
                )

                produto.stock -= qtd
                produto.save()

                total += produto.preco * qtd

        venda.total = total
        venda.save()

        return redirect("emitir_recibo", venda.id)


@login_required
def historico_vendas(request):
    vendas = Venda.objects.all().order_by("-data")
    return render(request, "historico_vendas.html", {"vendas": vendas})


@login_required
def emitir_recibo(request, venda_id):
    venda = get_object_or_404(Venda, id=venda_id)
    return render(request, "recibo.html", {"venda": venda})
