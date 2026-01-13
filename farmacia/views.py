from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from .models import Produto, Venda, ItemVenda


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
    return render(request, "farmacia/login.html")


def logout_view(request):
    logout(request)
    return redirect("/login/")


@login_required
def area_caixa(request):
    total = Venda.objects.filter(data__date=now().date()).aggregate(t=models.Sum("total"))["t"] or 0
    return render(request, "farmacia/caixa.html", {"total": total})


@login_required
def nova_venda(request):
    produtos = Produto.objects.all()
    return render(request, "farmacia/nova_venda.html", {"produtos": produtos})


@login_required
def finalizar_venda(request):
    if request.method == "POST":
        venda = Venda.objects.create(
            operador=request.user,
            pagamento=request.POST["pagamento"],
            total=0
        )

        total = 0
        for p in request.POST.getlist("produto"):
            qtd = int(request.POST.get(f"qtd_{p}"))
            prod = Produto.objects.get(id=p)
            ItemVenda.objects.create(
                venda=venda,
                produto=prod,
                quantidade=qtd,
                preco=prod.preco
            )
            total += prod.preco * qtd

        venda.total = total
        venda.save()

        return redirect("/emitir-recibo/?venda=" + str(venda.id))

    return redirect("/caixa/")


@login_required
def historico_vendas(request):
    vendas = Venda.objects.order_by("-data")
    return render(request, "farmacia/historico_vendas.html", {"vendas": vendas})


@login_required
def emitir_recibo(request):
    venda = Venda.objects.get(id=request.GET.get("venda"))
    itens = ItemVenda.objects.filter(venda=venda)
    return render(request, "farmacia/emitir_recibo.html", {"venda": venda, "itens": itens})
