from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


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
def gestor(request):
    return render(request, "gestor.html")


@login_required
def home(request):
    return render(request, "home.html")
