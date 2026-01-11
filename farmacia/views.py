from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/dashboard/")
        else:
            return render(request, "login.html", {"error": "Utilizador ou senha inválidos"})

    return render(request, "login.html")


@login_required
def dashboard(request):
    user = request.user

    if user.groups.filter(name="CAIXA").exists():
        return redirect("/caixa/")

    if user.groups.filter(name="FARMACEUTICO").exists():
        return redirect("/farmaceutico/")

    if user.groups.filter(name="GERENTE").exists():
        return redirect("/gerente/")

    return redirect("/admin/")


@login_required
def caixa(request):
    return render(request, "caixa.html")


@login_required
def farmaceutico(request):
    return render(request, "farmaceutico.html")


@login_required
def gerente(request):
    return render(request, "gerente.html")
