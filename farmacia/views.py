from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect


@csrf_protect
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # Redirecionamento por grupo
            if user.groups.filter(name="CAIXA").exists():
                return redirect("/admin/farmacia/entradastock/")

            if user.groups.filter(name="FARMACEUTICO").exists():
                return redirect("/admin/farmacia/produto/")

            if user.groups.filter(name="GERENTE").exists():
                return redirect("/admin/")

            # Superuser
            if user.is_superuser:
                return redirect("/admin/")

            return redirect("/admin/")
        else:
            return render(request, "login.html", {"error": "Utilizador ou senha inválidos"})

    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect("/")
