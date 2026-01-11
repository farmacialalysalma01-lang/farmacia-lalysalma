from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Produto, Venda


# ---------------- LOGIN ----------------
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)

            # Redirecionar conforme grupo
            if user.groups.filter(name="CAIXA").exists():
                return redirect("/caixa/")
            if user.groups.filter(name="GERENTE").exists():
                return redirect("/gerente/")
            if user.groups.filter(name="FARMACEUTICO").exists():
                return redirect("/farmaceutico/")
            if user.is_superuser:
                return redirect("/admin/")

        return render(request, "login.html", {"error": "Credenciais inválidas"})

    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect("/")


# ---------------- ÁREAS ----------------
@login_required
def caixa(request):
    return render(request, "caixa.html")


@login_required
def gerente(request):
    return render(request, "gerente.html")


@login_required
def farmaceutico(request):
    return render(request, "farmaceutico.html")


# ---------------- VENDAS ----------------
@login_required
def nova_venda(request):
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Produto, Venda
from django.utils import timezone

@login_required
def nova_venda(request):
    produtos = Produto.objects.filter(stock__gt=0)

    if request.method == "POST":
        produto_id = request.POST.get("produto")
        quantidade = int(request.POST.get("quantidade"))

        produto = Produto.objects.get(id=produto_id)

        # Verificar stock
        if quantidade > produto.stock:
            return render(request, "nova_venda.html", {
                "produtos": produtos,
                "erro": "Stock insuficiente!"
            })

        # Calcular preço
        total = quantidade * produto.preco

        # Criar venda
        Venda.objects.create(
            produto=produto,
            quantidade=quantidade,
            preco_unitario=produto.preco,
            total=total,
            operador=request.user,
            data=timezone.now()
        )

        # Atualizar stock
        produto.stock -= quantidade
        produto.save()

        return redirect("/caixa/")

    return render(request, "nova_venda.html", {"produtos": produtos})

