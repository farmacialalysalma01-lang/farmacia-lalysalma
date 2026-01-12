from django.contrib import admin
from .models import Produto, EntradaStock, SaidaStock, Venda


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("nome", "preco", "stock")
    search_fields = ("nome",)


@admin.register(EntradaStock)
class EntradaStockAdmin(admin.ModelAdmin):
    list_display = ("produto", "quantidade", "fornecedor", "data")
    list_filter = ("data",)


@admin.register(SaidaStock)
class SaidaStockAdmin(admin.ModelAdmin):
    list_display = ("produto", "quantidade", "motivo", "data")
    list_filter = ("data",)


@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "produto",
        "quantidade",
        "preco_unitario",
        "total",
        "forma_pagamento",
        "operador",
        "data",
    )
    list_filter = ("forma_pagamento", "data")
    search_fields = ("produto__nome", "cliente")
