from .models import Medicamento
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "home.html")

def login_view(request):
    erro = ""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("dashboard")
        else:
            erro = "Utilizador ou palavra-passe inválidos"

    return render(request, "login.html", {"erro": erro})

@login_required
def dashboard(request):
    from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    medicamentos = Medicamento.objects.all()

    nomes = [m.nome for m in medicamentos]
    quantidades = [m.quantidade for m in medicamentos]

    total = medicamentos.count()
    stock_baixo = Medicamento.objects.filter(quantidade__lte=5).count()
    total_qtd = sum(quantidades)

    return render(request, "dashboard.html", {
        "nomes": nomes,
        "quantidades": quantidades,
        "total": total,
        "stock_baixo": stock_baixo,
        "total_qtd": total_qtd,
    })

from reportlab.pdfgen import canvas
from django.http import HttpResponse

def recibo_pdf(request, venda_id):
    venda = Venda.objects.get(id=venda_id)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="recibo_{venda_id}.pdf"'

    p = canvas.Canvas(response)
    p.drawString(100, 800, "Farmácia Lalysalma")
    p.drawString(100, 780, f"Recibo Nº {venda.id}")
    p.drawString(100, 760, f"Data: {venda.data.strftime('%d/%m/%Y')}")

    y = 720
    for item in venda.itens.all():
        linha = f"{item.medicamento.nome} - {item.quantidade} x {item.preco}"
        p.drawString(100, y, linha)
        y -= 20

    p.drawString(100, y-20, f"TOTAL: {venda.total} MZN")

    p.showPage()
    p.save()
    return response

from django.contrib.auth.decorators import user_passes_test

def is_admin(user):
    return user.groups.filter(name="Administrador").exists()

@user_passes_test(is_admin)
def dashboard(request):
    ...
