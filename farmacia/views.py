from django.http import HttpResponse

def home(request):
    return HttpResponse("Sistema de Gestão da Farmácia Lalysalma – Online")
