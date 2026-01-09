from django.contrib import admin
from .models import Medicamento

@admin.register(Medicamento)
class MedicamentoAdmin(admin.ModelAdmin):
    list_display = ("nome", "categoria", "quantidade", "preco_venda", "data_validade")
    search_fields = ("nome", "categoria")
    list_filter = ("categoria",)
