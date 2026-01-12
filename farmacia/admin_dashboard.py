from django.utils.timezone import now
from django.db.models import Sum
from .models import Venda, Produto

def dashboard_data(request):
    hoje = now().date()

    vendas_hoje = Venda.objects.filter(data__date=hoje).aggregate(total=Sum('total'))['total'] or 0
    vendas_mes = Venda.objects.filter(data__month=hoje.month).aggregate(total=Sum('total'))['total'] or 0

    produtos = Produto.objects.count()
    em_falta = Produto.objects.filter(stock__lte=5).count()

    return {
        "vendas_hoje": vendas_hoje,
        "vendas_mes": vendas_mes,
        "produtos": produtos,
        "em_falta": em_falta,
    }
