from django.contrib import admin
from .models import Medicamento

@admin.register(Medicamento)
class MedicamentoAdmin(admin.ModelAdmin):
    list_display = (
        "nome",
        "quantidade",
        "preco_venda",
        "data_validade",
    )
    search_fields = ("nome",)
    list_filter = ("data_validade",)
