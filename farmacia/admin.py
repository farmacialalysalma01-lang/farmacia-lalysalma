from django.contrib import admin
from .models import Categoria, Medicamento


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)


@admin.register(Medicamento)
class MedicamentoAdmin(admin.ModelAdmin):
    list_display = (
        "nome",
        "categoria",
        "quantidade",
        "stock_minimo",
        "preco_venda",
        "data_validade",
    )

    list_filter = ("categoria", "data_validade")

    search_fields = ("nome",)

    ordering = ("nome",)
