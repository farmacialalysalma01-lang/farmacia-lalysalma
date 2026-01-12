from django.contrib import admin
from .models import Produto, Venda


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("nome", "preco", "stock")


@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "produto",
        "quantidade",
        "total",
        "forma_pagamento",
        "operador",
        "data",
    )

    list_filter = ("forma_pagamento", "data")
