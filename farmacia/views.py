from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test


def is_caixa(user):
    return user.groups.filter(name="CAIXA").exists()

def is_gerente(user):
    return user.groups.filter(name="GERENTE").exists()

def is_farmaceutico(user):
    return user.groups.filter(name="FARMACEUTICO").exists()

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if user.is_superuser:
                return redirect("/admin/")

            if user.groups.filter(name="CAIXA").exists():
                return redirect("/caixa/")

            if user.groups.filter(name="FARMACEUTICO").exists():
                return redirect("/farmaceutico/")

            if user.groups.filter(name="GERENTE").exists():
                return redirect("/gerente/")

            return redirect("/")

        else:
            return render(request, "login.html", {"error": "Login inválido"})

    return render(request, "login.html")


@login_required
def caixa(request):
    return render(request, "caixa.html")


@login_required
def farmaceutico(request):
    return render(request, "farmaceutico.html")


@login_required
def gerente(request):
    return render(request, "gerente.html")


@login_required
def home(request):
    return render(request, "home.html")

from .models import Produto, Venda


@login_required
@user_passes_test(is_caixa)
def nova_venda(request):
    produtos = Produto.objects.all()

    if request.method == "POST":
        produto_id = request.POST.get("produto")
        quantidade = int(request.POST.get("quantidade"))

        produto = Produto.objects.get(id=produto_id)

        if produto.quantidade >= quantidade:
            total = produto.preco * quantidade

            Venda.objects.create(
                produto=produto,
                quantidade=quantidade,
                total=total,
                vendedor=request.user
            )

            produto.quantidade -= quantidade
            produto.save()

    return render(request, "nova_venda.html", {"produtos": produtos})

