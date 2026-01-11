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

            # Redireciona conforme grupo
            if user.groups.filter(name="CAIXA").exists():
                return redirect("/caixa/")
            elif user.groups.filter(name="FARMACEUTICO").exists():
                return redirect("/farmaceutico/")
            elif user.groups.filter(name="GERENTE").exists():
                return redirect("/gerente/")
            else:
                return redirect("/admin/")

        return render(request, "login.html", {"error": "Credenciais inválidas"})

    return render(request, "login.html")

from django.contrib.auth.decorators import login_required

@login_required
def caixa_dashboard(request):
    return render(request, "caixa.html")

@login_required
def farmaceutico_dashboard(request):
    return render(request, "farmaceutico.html")

@login_required
def gerente_dashboard(request):
    return render(request, "gerente.html")
