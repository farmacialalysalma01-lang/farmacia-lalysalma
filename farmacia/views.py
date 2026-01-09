from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

def login_view(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST.get("username"),
            password=request.POST.get("password"),
        )
        if user is not None:
            login(request, user)
            return redirect("/admin/")
        return HttpResponse("Login inválido")

    return render(request, "login.html")
